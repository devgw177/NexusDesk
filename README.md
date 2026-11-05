# NexusDesk

Sistema de gerenciamento de chamados de suporte técnico, desenvolvido em Python como projeto de aprendizado e portfólio.

## Status

**Versão 0.4.1 — cadastro e validação de múltiplos chamados, armazenamento temporário em lista de dicionários e exibição automática do histórico ao finalizar os cadastros.**

## Funcionalidades implementadas

- Cadastro do nome do solicitante, descrição do problema e prioridade.
- Exibição de um resumo numerado para cada chamado.
- Registro de vários chamados durante a mesma execução, usando `while`.
- Numeração sequencial dos chamados (1, 2, 3...).
- Pergunta para registrar outro chamado ou encerrar o programa.
- Aceita respostas como `sim`, `Sim` e `SIM` na pergunta de continuação.
- Exige uma resposta válida (`sim`, `não` ou `nao`) antes de continuar ou encerrar; entradas inválidas são solicitadas novamente.
- Impede nomes e descrições vazios ou formados apenas por espaços, solicitando novamente.
- Aceita as prioridades `baixa`, `média`, `media` e `alta`, desconsiderando maiúsculas e espaços nas extremidades.
- Padroniza a prioridade `media` para `média` antes de exibir o resumo do chamado.
- Organiza cada chamado em um dicionário com `numero`, `nome`, `problema` e `prioridade`.
- Armazena esses dicionários em uma lista `chamados` enquanto o programa está em execução.
- Exibe automaticamente ao final dos cadastros todos os chamados da execução, percorrendo a lista com `for`.

**Limitações conhecidas:** os chamados ficam apenas na memória durante a execução; não há persistência em arquivo ou banco de dados. O programa exibe o histórico completo ao terminar os cadastros, mas ainda não oferece pesquisa interativa de um chamado específico pelo número. A numeração recomeça em 1 a cada nova execução. As respostas `não` e `nao` encerram o programa.

## Como executar

Requisito: **Python 3**.

1. Clone o repositório:
   ```bash
   git clone https://github.com/devgw177/NexusDesk.git
   ```
2. Entre na pasta:
   ```bash
   cd NexusDesk
   ```
3. Execute:
   ```bash
   python main.py
   ```

No Windows, você também pode usar `py main.py`; em outros sistemas, `python3 main.py`.

### Exemplo

```text
=== NEXUSDESK | SUPORTE DE TI ===
Nome do solicitante: Gabriel
Descreva o problema: Computador não liga
Prioridade (baixa, média ou alta): Alta

=== CHAMADO REGISTRADO ===
Número do chamado: 1
Solicitante: Gabriel
Problema: Computador não liga
Prioridade: alta

Deseja registrar outro chamado? (sim/não): sim
Nome do solicitante: Ana
Descreva o problema: Internet sem conexão
Prioridade (baixa, média ou alta): MEDIA

=== CHAMADO REGISTRADO ===
Número do chamado: 2
Solicitante: Ana
Problema: Internet sem conexão
Prioridade: média

Deseja registrar outro chamado? (sim/não): não
=== CHAMADOS CADASTRADOS ===
Número: 1
Nome: Gabriel
Problema: Computador não liga
Prioridade: alta

Número: 2
Nome: Ana
Problema: Internet sem conexão
Prioridade: média

NexusDesk encerrado.
```

## Histórico de desenvolvimento

- [Issue #1 — Registrar chamado pelo terminal](https://github.com/devgw177/NexusDesk/issues/1): concluída na versão 0.1.
- [Issue #2 — Registrar múltiplos chamados com identificadores sequenciais](https://github.com/devgw177/NexusDesk/issues/2): concluída na versão 0.2.
- [Issue #3 — Validar dados dos chamados e opções de prioridade](https://github.com/devgw177/NexusDesk/issues/3): concluída na versão 0.3.
- **Versão 0.3.1:** validação da resposta de continuação (`sim`, `não` ou `nao`), com nova tentativa para entradas inválidas.
- **Versão 0.3.2:** padronização da prioridade `media` para `média` antes da apresentação do chamado.
- **Versão 0.4.0:** criação de um dicionário por chamado e armazenamento dos registros em uma lista durante a execução, sem consulta interativa ou persistência permanente.
- **Versão 0.4.1:** exibição do histórico de chamados ao terminar os cadastros, utilizando um `for` para percorrer os dicionários.

## Próximos passos planejados

- Padronizar as mensagens exibidas no terminal e melhorar o acabamento do código.
- Permitir pesquisar um chamado específico pelo número (a exibição do histórico completo já está implementada).
- Persistir os registros em arquivo ou banco de dados.
- Criar testes automatizados.
- Estruturar uma API conforme a evolução do projeto.

> O NexusDesk ainda está em desenvolvimento. Tecnologias e funcionalidades futuras não são apresentadas como concluídas.

## Licença

MIT.
