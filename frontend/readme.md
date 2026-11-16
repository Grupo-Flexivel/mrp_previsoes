# Frontend — MRP Dashboard de Ponto de Ruptura

Protótipo de interface para apresentação de um resumo visual dos produtos, suas projeções de estoque e os alertas de ruptura/compra.

## Stack
- HTML, CSS e JavaScript puro — sem framework ou build.
- Header e footer são injetados via `fetch` por [`scripts/layout.js`](scripts/layout.js) (requer servir os arquivos por HTTP, ex.: Live Server).

## Estrutura

```
frontend/
├── pages/
│   └── dashboard.html        # Tela principal (única página)
├── layout/
│   ├── header/               # header.html + header.css (barra verde superior)
│   └── footer/               # footer.html + footer.css (barra verde inferior)
├── styles/
│   └── dashboard.css         # Estilos da página (importa header/footer)
├── scripts/
│   └── layout.js             # Injeta header e footer nas páginas
├── assets/                   # Ícones: box.png, warning.png, search.png, preview.png
└── readme.md                 # Este arquivo
```

## Tela principal (`pages/dashboard.html`)

- **Header**: título "Dashboard - Ponto de Ruptura".
- **Cards de resumo**: produtos cadastrados, alertas de compra e campo de pesquisa por código ou descrição.
- **Tabela de produtos**: colunas PRODUTO, INDICADORES, MÊS ATUAL, MÊS 1, MÊS 2, MÊS 3, RUPTURA e ALERTA DE COMPRA. Cada produto ocupa 3 linhas (estoque inicial previsto, demanda prevista, estoque a caminho).
- **Paginação** da tabela.
- **Footer**: identificação do protótipo.

Os valores exibidos são estáticos no protótipo; serão substituídos pelos dados do backend na integração.

## Guia tipográfico

Referência rápida das fontes, tamanhos e pesos utilizados na interface.

### Marca

| Uso | Fonte | Tamanho | Peso |
|---|---|---:|---:|
| Nome da marca | Manrope | 21px | 700 |
| Subtítulo da marca | DM Sans | 8px | 600 |

### Títulos e descrição da página

| Uso | Fonte | Tamanho | Peso |
|---|---|---:|---:|
| Eyebrow da seção | DM Sans | 10px | 800 |
| Título da página | Manrope | 22–29px | 800 |
| Descrição da seção | DM Sans | 13px | 400 |

### Cards e filtros

| Uso | Fonte | Tamanho | Peso |
|---|---|---:|---:|
| Rótulos dos cards | DM Sans | 11px | 700 |
| Números dos cards | Manrope | 30px | 700 |
| Texto auxiliar dos cards | DM Sans | 12px | 400 |
| Título do filtro | DM Sans | 15px | 600 |
| Campo de pesquisa | DM Sans | 13px | 400 |

### Tabela de produtos

| Uso | Fonte | Tamanho | Peso |
|---|---|---:|---:|
| Cabeçalho da tabela | DM Sans | 10px | 700 |
| Nome do mês | DM Sans | 9px | 800 |
| Código do produto | Manrope | 9px | 800 |
| Descrição do produto | DM Sans | 13px | 600 |
| Indicador | DM Sans | 11px | 600 |
| Valores | DM Sans | 13px | 700 |
| Unidade | DM Sans | 10px | 500 |

### Paginação e rodapé

| Uso | Fonte | Tamanho | Peso |
|---|---|---:|---:|
| Paginação | DM Sans | 11px | 400–700 |
| Footer | DM Sans | 10px | 400–600 |

> **Nota:** os estilos atuais usam `Inter` como fonte base (`font-family` em `dashboard.css`, `header.css` e `footer.css`). O guia acima define a tipografia alvo com Manrope e DM Sans.
