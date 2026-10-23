# NexusDesk

Sistema de gerenciamento de chamados de suporte técnico, desenvolvido em Python como projeto de aprendizado e portfólio.

## Status

**Versão 0.2 — cadastro de múltiplos chamados no terminal.**

## Funcionalidades implementadas

- Cadastro do nome do solicitante, descrição do problema e prioridade.
- Exibição de um resumo numerado para cada chamado.
- Registro de vários chamados durante a mesma execução, usando `while`.
- Numeração sequencial dos chamados (1, 2, 3...).
- Pergunta para registrar outro chamado ou encerrar o programa.
- Aceita respostas como `sim`, `Sim` e `SIM` na pergunta de continuação.

**Limitações conhecidas:** os dados são mantidos somente durante a execução; não há histórico, banco de dados nem validação dos campos. A numeração recomeça em 1 ao reiniciar o programa. Respostas diferentes de `sim` encerram a execução.

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
Prioridade: Alta

Deseja registrar outro chamado? (sim/não): sim
Nome do solicitante: Ana
Descreva o problema: Internet sem conexão
Prioridade (baixa, média ou alta): Média

=== CHAMADO REGISTRADO ===
Número do chamado: 2
Solicitante: Ana
Problema: Internet sem conexão
Prioridade: Média

Deseja registrar outro chamado? (sim/não): não

NexusDesk encerrado.
```

## Histórico de desenvolvimento

- [Issue #1 — Registrar chamado pelo terminal](https://github.com/devgw177/NexusDesk/issues/1): concluída na versão 0.1.
- [Issue #2 — Registrar múltiplos chamados com identificadores sequenciais](https://github.com/devgw177/NexusDesk/issues/2): concluída na versão 0.2.

## Próximos passos planejados

- Validar os campos de entrada e as opções de prioridade.
- Permitir consultar chamados registrados.
- Persistir os registros em arquivo ou banco de dados.
- Criar testes automatizados.
- Estruturar uma API conforme a evolução do projeto.

> O NexusDesk ainda está em desenvolvimento. Tecnologias e funcionalidades futuras não são apresentadas como concluídas.

## Licença

MIT.
