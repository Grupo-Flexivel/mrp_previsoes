# Backend — MRP Previsão de Estoque e Ponto de Ruptura

## Visão geral

O backend está em fase inicial. O projeto Node.js contém um servidor Express mínimo e a configuração para carregar variáveis de ambiente. A API ainda não implementa rotas, regras de negócio nem acesso ao PostgreSQL.

Separadamente, `prototipo/analise.py` contém uma análise exploratória em Python baseada nos CSVs do mesmo diretório. Esse script não é integrado ao servidor Node.js.

## Tecnologias e situação atual

- **Node.js / CommonJS:** runtime e formato de módulos configurados em `package.json`.
- **Express:** aplicação HTTP em `src/app.js`; por enquanto registra somente o middleware JSON.
- **dotenv:** carrega `API_PORT` do arquivo `.env`.
- **nodemon:** usado pelo comando `npm start` para iniciar e observar o servidor.
- **pg:** dependência declarada para PostgreSQL, mas ainda não utilizada no código.
- **Python e pandas:** usados pelo script exploratório em `prototipo/analise.py`; não há arquivo de dependências Python no backend.

No estado atual:

- `src/server.js` carrega as variáveis de ambiente e inicia o servidor na porta indicada por `API_PORT`.
- `src/config/db.js` ainda não configura uma conexão com o banco.
- Não há endpoints implementados.
- O script `npm test` é um placeholder e termina com erro; ainda não existem testes automatizados.
- Em `src/app.js`, a variável `app` é atribuída sem declaração. Recomenda-se declarar a variável explicitamente antes de ampliar a aplicação.

## Estrutura

```text
backend/
├── prototipo/
│   ├── analise.py
│   ├── codigos-em-ambos.csv
│   ├── Consulta-de-Posição-de-Estoque-por-Natureza.csv
│   └── Necessidade-por-Data-e-componente-Com-Itens-de-Revenda.csv
├── src/
│   ├── config/
│   │   └── db.js
│   ├── app.js
│   └── server.js
├── .env.exemple
├── package.json
├── package-lock.json
├── readme.md
└── spec_backend.md
```

## Executar a API

### Requisitos

- Node.js e npm.
- PostgreSQL não é necessário para iniciar o servidor enquanto a integração com o banco não estiver implementada.

### Instalação

No PowerShell, entre no diretório `backend` e instale as dependências:

```powershell
cd backend
npm install
```

Crie o arquivo `.env` a partir do exemplo, caso ainda não exista:

```powershell
if (-not (Test-Path .env)) {
    Copy-Item .env.exemple .env
}
```

Edite `.env` e defina uma porta, por exemplo:

```env
API_PORT=3000
```

Se `.env` já existir, preserve as outras variáveis e apenas confira `API_PORT`. O arquivo `.env.exemple` atual contém somente o nome da variável, sem um valor de porta.

Inicie o servidor:

```powershell
npm start
```

O script executado é `nodemon src/server.js`. Para encerrá-lo, pressione `Ctrl+C`. Como ainda não há rotas, o servidor não oferece operações da API; uma requisição à raiz pode retornar `404`.

### Testes

O comando disponível no `package.json` é:

```powershell
npm test
```

Ele ainda é apenas um placeholder (`Error: no test specified`); não há testes configurados.

## Análise exploratória em Python

`prototipo/analise.py` lê os arquivos CSV desse diretório com pandas, seleciona um produto piloto configurado no próprio script, agrega a demanda em quatro períodos mensais, calcula o estoque projetado e apresenta o ponto de ruptura e o aviso de compra. O estoque a caminho está fixado em zero nessa análise.

Para executar em um ambiente virtual PowerShell, use Python 3.12 ou superior e instale pandas:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas
python .\prototipo\analise.py
```

O script exige dados para o produto piloto e exatamente quatro períodos consecutivos de demanda. Se esses requisitos não forem atendidos, ele interrompe a execução com erro. As dependências Python ainda não estão registradas em um `requirements.txt`.

## Regras de negócio propostas

As regras completas e os pontos que ainda precisam de homologação estão em [`spec_backend.md`](./spec_backend.md). Em resumo:

- Estoque final previsto: **estoque inicial − demanda + estoque a caminho**.
- O estoque final de um período alimenta o estoque inicial do período seguinte.
- A ruptura é identificada comparando o estoque final de um período com a demanda do período seguinte, usando `<=`.
- O código da ruptura e o lead time determinam o período recomendado para a compra; o código `99` indica ausência de alerta.
- A convenção do lead time e outros pontos de negócio ainda precisam ser validados antes da implementação definitiva.

## Próximos passos

1. Validar os pontos pendentes em `spec_backend.md`.
2. Implementar a conexão PostgreSQL, o modelo de dados e as consultas necessárias.
3. Implementar as rotas e regras de negócio da API.
4. Adicionar testes automatizados para os cálculos e endpoints.
5. Registrar as dependências Python para reproduzir a análise exploratória.