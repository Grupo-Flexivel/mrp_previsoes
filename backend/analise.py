from dataclasses import dataclass
from pathlib import Path
import pandas as pd

@dataclass(frozen=True)
class Produto:
    codigo: int
    descricao: str


def calcular_aviso_compra(codigo_ruptura: int, lead_time_meses: int) -> str:
    if lead_time_meses < 0:
        raise ValueError("O lead time não pode ser negativo.")
    if codigo_ruptura == 99:
        return "Sem alerta de compra."
    if codigo_ruptura not in range(4):
        raise ValueError(f"Código de ruptura inválido: {codigo_ruptura}.")

    periodo_compra = codigo_ruptura + 1 - lead_time_meses #o codigo de ruptura indo de 0 a 3 indicam os meses também
    if periodo_compra < 0:
        meses_atraso = abs(periodo_compra)
        return (f"Compra atrasada: deveria ter sido solicitada há {meses_atraso} {"meses" if meses_atraso > 1 else "mês"}")
    if periodo_compra == 0:
        return "Solicitar compra no mês atual."
    return f"Solicitar compra no Mês {periodo_compra}."


diretorio_script = Path(__file__).resolve().parent
estoque_produtos = pd.read_csv(diretorio_script / "Consulta-de-Posição-de-Estoque-por-Natureza.csv", skipinitialspace=True)
necessidade = pd.read_csv(diretorio_script / "Necessidade-por-Data-e-componente-Com-Itens-de-Revenda.csv", skipinitialspace=True)

estoque_produtos.columns = estoque_produtos.columns.str.strip() #remove espaços em branco do nome das colunas
necessidade.columns = necessidade.columns.str.strip()
codigo_produto_piloto = 103070006 #103130002 
lead_time_meses = 2

codigos_estoque = pd.to_numeric(estoque_produtos.iloc[:, 0], errors="coerce") #.iloc[linha, coluna]
linhas_estoque = estoque_produtos.loc[codigos_estoque.eq(codigo_produto_piloto)]
if len(linhas_estoque) != 1:
    raise ValueError(
        f"Esperada uma linha de estoque para o produto {codigo_produto_piloto}; "
        f"encontradas {len(linhas_estoque)}."
    )

produto_piloto = Produto(
    codigo=codigo_produto_piloto,
    descricao=str(linhas_estoque.iloc[0, 1]).strip(),
)

estoque_inicial_mes = pd.to_numeric(
    linhas_estoque.iloc[0]["Estoque atual"],
    errors="raise",
)

codigos_necessidade = pd.to_numeric(necessidade["Componente"], errors="coerce")
linhas_necessidade = necessidade.loc[codigos_necessidade.eq(produto_piloto.codigo)].copy()
#print(f"linhas necessidade: {linhas_necessidade.shape[0]}") 
#print(f"linhas necessidade: {linhas_necessidade}")

if linhas_necessidade.empty:
    raise ValueError(
        f"Nenhuma necessidade encontrada para o produto {produto_piloto.codigo}."
    )

linhas_necessidade["Data Necessidade"] = pd.to_datetime(
    linhas_necessidade["Data Necessidade"].astype(str).str.strip(),
    dayfirst=True,
    errors="raise",
)

#DEMANDA DO PRODUTO
linhas_necessidade["Necessidade Bruta"] = pd.to_numeric(
    linhas_necessidade["Necessidade Bruta"],
    errors="raise",
)

#AGRUPA O PERIODO MENSAL PROVINDO DA COLUNA "DATA NECESSIDADE" E SOMA A DEMANDA BRUTA PARA CADA PERIODO
linhas_necessidade["Período"] = linhas_necessidade["Data Necessidade"].dt.to_period("M")
demanda_por_periodo = (
    linhas_necessidade.groupby("Período")["Necessidade Bruta"].sum().sort_index()
)

if len(demanda_por_periodo) != 4:
    raise ValueError(
        f"Esperados quatro períodos de demanda para o produto {produto_piloto}; "
        f"encontrados {len(demanda_por_periodo)}."
    )

periodos = list(demanda_por_periodo.index)
if any(periodos[i] != periodos[i - 1] + 1 for i in range(1, len(periodos))):
    raise ValueError("Os quatro períodos de demanda não são consecutivos.")

# O estoque a caminho permanece zerado nesta análise, até os dados do BI estarem disponíveis.
estoque_a_caminho = 0.0
projecoes = []
estoque_inicial = estoque_inicial_mes
for periodo, demanda in demanda_por_periodo.items():
    estoque_final = estoque_inicial - demanda + estoque_a_caminho
    projecoes.append(
        {
            "Período": str(periodo),
            "Estoque inicial": estoque_inicial,
            "Demanda": demanda,
            "Estoque a caminho": estoque_a_caminho,
            "Estoque final": estoque_final,
        }
    )
    estoque_inicial = estoque_final

previsao = pd.DataFrame(projecoes)
estoques_finais = previsao["Estoque final"].tolist()
demandas = demanda_por_periodo.tolist()

codigos_ruptura = {
    0: "Ruptura do mês atual pra mês 1",
    1: "Ruptura do mês 1 pra mês 2",
    2: "Ruptura do mês 2 pra mês 3",
    3: "Ruptura do mês 3 pra média dos quatro meses",
    99: "Sem ruptura nos quatro períodos",
}

codigo_ruptura = 99
for i in range(3):
    if estoques_finais[i] <= demandas[i + 1]:
        codigo_ruptura = i
        break
if codigo_ruptura == 99 and estoques_finais[3] <= sum(demandas) / 4:
    codigo_ruptura = 3

resumo_produto = pd.DataFrame(
    [
        ["Estoque inicial previsto do mes", *previsao["Estoque inicial"].tolist()],
        ["Demanda prevista do mes", *previsao["Demanda"].tolist()],
        ["Estoque a caminho", *previsao["Estoque a caminho"].tolist()],
    ],
    columns=["INDICADOR", "MES ATUAL", "MES 1", "MES 2", "MES 3"],
)

print(f"\nProduto: {produto_piloto.codigo} - {produto_piloto.descricao}")
print(resumo_produto.to_string(index=False, float_format=lambda valor: f"{valor:.3f}"),"\n")
print(f"Resultado da análise: {codigos_ruptura[codigo_ruptura]}")
print(f"Requisição de compra: {calcular_aviso_compra(codigo_ruptura, lead_time_meses)}\n")

# print(codigos_estoque)
# print(linhas_necessidade["Período"])
# print(demanda_por_periodo)