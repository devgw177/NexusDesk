# NexusDesk - Sistema de gerenciamento de chamados de TI
# Versão 0.3 - Validação de dados dos chamados


# NexusDesk - Sistema de gerenciamento de chamados

print("=== NEXUSDESK | SUPORTE DE TI ===")

contador = 1
continuar = "sim"

while continuar == "sim":

    # Entrada de dados
    nome = input("Nome do solicitante: ").strip()

    # validação do nome 
    while nome == "":
        print("erro, nome é obrigatorio")
        nome = input("digite seu nome novamente: ").strip()


    problema = input("Descreva o problema: ").strip()

    # Validação do problema
    while problema =="": 
        print("erro, problema é obrigatorio")
        problema = input("digite seu problema novamente: ").strip()


    prioridade = input("Prioridade (baixa, média ou alta): ").strip().lower()

    while prioridade not in ("baixa", "média", "media", "alta"):
        print("erro, prioridade invalida")
        prioridade = input("digite a prioridade:" ).strip().lower()

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
