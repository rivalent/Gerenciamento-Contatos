# Aplicação de Gerenciamento de Contatos

## Descrição

Esta é uma aplicação de linha de comando desenvolvida em Python para gerenciar contatos. Utilizando SQLite como banco de dados, a aplicação permite criar, visualizar, atualizar e deletar contatos. Além disso, ela realiza a importação e tratamento de dados a partir de um arquivo CSV, garantindo que apenas contatos válidos sejam armazenados.

## Estrutura do Projeto

- **Configuração do Banco de Dados:** 
  - O banco de dados SQLite é configurado automaticamente ao iniciar a aplicação. A tabela `contacts` é criada caso não exista.
  
- **Funções CRUD:**
  - **Criar:** Adicionar novos contatos ao banco de dados.
  - **Visualizar:** Exibir todos os contatos armazenados no banco de dados.
  - **Atualizar:** Modificar informações de contatos existentes.
  - **Deletar:** Remover contatos do banco de dados.

- **Interface de Linha de Comando:**
  - A aplicação é controlada via CLI (Command Line Interface), onde o usuário pode selecionar as opções desejadas.

## Funcionalidades

### Comandos Disponíveis:
1. **Adicionar Contatos:** Permite ao usuário inserir novos contatos no banco de dados.
2. **Visualizar Contatos:** Exibe todos os contatos cadastrados no banco de dados.
3. **Atualizar Contatos:** Permite atualizar as informações de um contato existente.
4. **Deletar Contatos:** Remove um contato específico do banco de dados.

### Importação de Dados a Partir de CSV

- A aplicação lê um arquivo CSV (`contatos_com_erros.csv`) e realiza a validação e tratamento dos dados antes de inseri-los no banco de dados.
- **Regras de Validação:**
  - **Nome:** Deve conter nome e sobrenome.
  - **Email:** Deve estar no formato válido, por exemplo, `algumacoisa@algumacoisa.com`.
  - **Telefone:** Deve conter apenas números, traços e o símbolo `+`, por exemplo, `(21) 96969-9696` ou `+1-449-222-999`.
  - **Endereço:** Deve ser uma string válida e não pode estar vazio.
- Contatos que não atendem a essas regras não são inseridos no banco de dados.

## Instalação e Execução

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. A aplicação utiliza as bibliotecas `sqlite3` e `csv`, que são bibliotecas padrão do Python e não requerem instalação adicional.

### Execução

1. Clone este repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Execute o script Python:

```bash
python gerenciamento_contatos.py
