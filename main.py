# NexusDesk - Sistema de gerenciamento de chamados de TI
# Versão 0.1 - Registro de chamados no terminal


# NexusDesk - Sistema de gerenciamento de chamados

print("=== NEXUSDESK | SUPORTE DE TI ===")

contador = 1
continuar = "sim"

while continuar == "sim":

    # Entrada de dados
    nome = input("Nome do solicitante: ")
    problema = input("Descreva o problema: ")
    prioridade = input("Prioridade (baixa, média ou alta): ")

    # Saída de dados
    print("\n=== CHAMADO REGISTRADO ===")
    print("Número do chamado:", contador)
    print("Solicitante:", nome)
    print("Problema:", problema)
    print("Prioridade:", prioridade)

    # Atualiza o contador
    contador = contador + 1

    # Pergunta se deseja continuar
    continuar = input("\nDeseja registrar outro chamado? (sim/não): ").strip().lower()

print("\nNexusDesk encerrado.")
