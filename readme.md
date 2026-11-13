# Previsão de Estoque e Ponto de Ruptura

## Sobre o projeto

O projeto tem como objetivo apoiar o planejamento de estoque, identificar antecipadamente riscos de ruptura e indicar quando um produto precisa de atenção para reposição. A análise considera estoque disponível, demanda prevista, recebimentos programados e o lead time de cada produto.

O protótipo foi validado pela equipe. Este repositório reúne a interface inicial, uma análise exploratória em Python e as especificações do produto. A implementação final será desenvolvida com a stack definida abaixo.

## Stack definida para a versão final

| Camada | Tecnologia |
|---|---|
| Banco de dados | PostgreSQL |
| Backend e API | Node.js, Express e TypeScript |
| Frontend | React e TypeScript |
| Linguagem da aplicação | TypeScript |

O backend será responsável por acessar os dados no PostgreSQL e fornecer à aplicação os resultados de negócio por meio de uma API. O frontend consumirá essa API e apresentará as informações ao usuário.

Python não faz parte da stack principal definida. O script existente é um artefato de análise do protótipo; Gráficos interativos e em tempo real serão projetados pelo próprio React.

## Estado atual

- **Frontend:** dashboard estático em HTML, CSS e JavaScript, com dados demonstrativos.
- **Backend:** script exploratório em Python que lê arquivos CSV e calcula uma projeção para um produto selecionado.
- **Banco de dados e API:** a integração com PostgreSQL e a API Node.js ainda serão implementadas.
- **Aplicação React:** prevista para a versão final; ainda não configurada neste repositório.

O código atual serve como referência do protótipo e não representa a arquitetura final.

## Estrutura atual

```text
.
├── backend/
│   └── analise.py
├── frontend/
│   ├── pages/
│   │   └── dashboard.html
│   ├── scripts/
│   │   └── layouts.js
│   ├── styles/
│   │   └── dashboard.css
│   └── layout/
│       ├── header/ 
│       │   ├── header.html
│       │   └── header.css
│       └── footer/
│           ├── footer.html
│           └── footer.css
└── readme.md
```

## Próximas etapas

1. Definir o modelo de dados e as migrações do PostgreSQL.
2. Estruturar a API Express em TypeScript e implementar as regras de negócio no backend.
3. Implementar o frontend React em TypeScript e integrá-lo à API.
4. Definir configuração de ambiente, execução local e testes conforme a estrutura da aplicação for criada.

## Execução
Ainda não há comandos de instalação ou execução para a stack final: a configuração do projeto Node.js, do frontend React e da conexão com o PostgreSQL está pendente.

## Link do protótipo figma
https://www.figma.com/make/ApXdy0eOAeoWHiJd6r4rEc/Dashboard-de-Previs%C3%B5es-MRP?p=f&t=RIx5b35PIKK4CPDk-0