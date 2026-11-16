# Previsão de Estoque e Ponto de Ruptura

## Sobre o projeto

O projeto apoia o planejamento de estoque e a identificação antecipada de riscos de ruptura, considerando estoque disponível, demanda prevista, recebimentos programados e lead time.

Atualmente, o repositório reúne um dashboard demonstrativo, o esqueleto inicial de uma API e uma análise exploratória em Python. A aplicação completa e a integração com dados reais ainda estão em desenvolvimento.

## Stack definida para a versão final

| Camada | Tecnologia |
|---|---|
| Banco de dados | PostgreSQL |
| Backend e API | Node.js, Express e JavaScript |
| Frontend | React e JavaScript |
| Linguagem da aplicação | JavaScript |

Na arquitetura planejada, o backend acessará o PostgreSQL e fornecerá os resultados por meio de uma API; o frontend React consumirá essa API. Essa integração ainda não está implementada.

Python não faz parte da stack principal planejada. O script em Python é um artefato de análise do protótipo.

## Estado atual

- **Frontend:** dashboard em HTML, CSS e JavaScript, com valores demonstrativos definidos na página. O JavaScript carrega os arquivos compartilhados de cabeçalho e rodapé; os dados não são carregados de uma API.
- **Backend:** esqueleto inicial em Node.js e Express, com configuração de porta via `dotenv` e execução de desenvolvimento via `nodemon`. Ainda não há endpoints, regras de negócio nem integração funcional com o banco.
- **Banco de dados:** PostgreSQL e dependência `pg` já está declarada, mas a conexão e o acesso a dados ainda não foram implementados.
- **Análise do protótipo:** script Python e arquivos CSV internos em `backend/prototipo/`.
- **Testes:** o script `npm test` é apenas um placeholder e ainda não executa testes.
- **React:** faz parte da arquitetura planejada, mas ainda não foi configurado no frontend.

## Estrutura atual

```text
.
├── backend/
│   ├── prototipo/
│   │   ├── analise.py
│   │   └── *.csv
│   ├── src/
│   │   ├── config/
│   │   │   └── db.js
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── tests/
│   │   ├── app.js
│   │   └── server.js
│   ├── .env.exemple
│   ├── package.json
│   └── spec_backend.md
│
├── frontend/
│   ├── assets/
│   ├── layout/
│   ├── pages/
│   │   └── dashboard.html
│   ├── scripts/
│   │   └── layout.js
│   ├── styles/
│   │   └── dashboard.css
│   ├── readme.md
│   └── spec_frontend.md
└── readme.md
```

## Como executar

### Backend

Requisitos: Node.js e npm instalados. Não é necessário configurar o PostgreSQL para iniciar o esqueleto atual, pois ele ainda não abre conexão com o banco.

Se o arquivo `.env` já existir, preserve as demais configurações e apenas confira o valor de `API_PORT`. Esse arquivo é local e não deve ser enviado ao repositório.

Inicie o servidor:

```powershell
npm start
```

O script atual usa `nodemon` para iniciar `src/server.js`. Para encerrar, pressione `Ctrl+C`. Como ainda não há rotas implementadas, iniciar o servidor não disponibiliza funcionalidades de negócio. 

### Frontend

O dashboard pode ser aberto por um servidor estático, como a extensão Live Server do VS Code. Abra `frontend/pages/dashboard.html` com essa extensão. O servidor é necessário porque a página carrega o cabeçalho e o rodapé com `fetch`; abrir diretamente como arquivo (`file://`) pode impedir esse carregamento.

O dashboard usa dados demonstrativos e ainda não depende do backend.

## Próximas etapas

1. Implementar e testar as rotas da API e as devidas regras de negócio.
2. Configurar a conexão e o modelo de dados do PostgreSQL.
3. Implementar o frontend React e integrá-lo à API.
4. Adicionar testes automatizados e instruções de configuração para a aplicação completa.

## Protótipo Figma

https://www.figma.com/make/ApXdy0eOAeoWHiJd6r4rEc/Dashboard-de-Previs%C3%B5es-MRP?p=f&t=RIx5b35PIKK4CPDk-0