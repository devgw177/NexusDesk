# NexusDesk

Sistema de gerenciamento de chamados de suporte técnico, desenvolvido progressivamente em Python como projeto de aprendizado e portfólio.

## Status

**Versão 0.1 — registro de um chamado via terminal.** Funcionalidade implementada e testada com entradas de exemplo.

## Funcionalidades disponíveis

- Solicitar o nome de quem abre o chamado.
- Receber a descrição do problema.
- Receber uma prioridade informada pelo usuário.
- Exibir um resumo com os dados informados.

> **Limitações atuais:** o chamado existe apenas durante a execução. Os dados não são armazenados em arquivos ou banco de dados, e a prioridade ainda não passa por validação.

## Como executar

Requisitos: Python 3 instalado.

1. Clone o repositório ou baixe o arquivo `main.py`.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

Em alguns ambientes, o comando pode ser `python3 main.py` ou `py main.py`.

Exemplo de entrada:

```text
Nome do solicitante: Gabriel
Descreva o problema: Computador não liga
Prioridade (baixa, média ou alta): Alta
```

O programa apresenta o resumo do chamado no terminal.

## Próximas melhorias

- Validar a prioridade e as informações digitadas.
- Permitir o registro de vários chamados.
- Atribuir um identificador único a cada chamado.
- Armazenar e consultar os registros.
- Adicionar testes automatizados e, posteriormente, uma API.

## Desenvolvimento

Este repositório registra a evolução do projeto em pequenas entregas. As tarefas são acompanhadas na aba [Issues](https://github.com/devgw177/NexusDesk/issues).

## Licença

MIT.
