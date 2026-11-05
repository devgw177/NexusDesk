# NexusDesk - Sistema de gerenciamento de chamados de TI
# Versão 0.4.0 - Validação de dados dos chamados


print("=== NEXUSDESK | SUPORTE DE TI ===")

contador = 1
continuar = "sim"
chamados = []

while continuar == "sim":

    # Entrada de dados
    nome = input("Nome do solicitante: ").strip()

    # validação do nome 
    while nome == "":
        print("Erro, nome é obrigatorio")
        nome = input("digite seu nome novamente: ").strip()

    problema = input("Descreva o problema: ").strip()

    # Validação do problema
    while problema =="": 
        print("Erro, problema é obrigatório")
        problema = input("digite seu problema novamente: ").strip()

    prioridade = input("Prioridade (baixa, média ou alta): ").strip().lower()

    while prioridade not in ("baixa", "média", "media", "alta"):
        print("Erro, prioridade inválida")
        prioridade = input("digite a prioridade:" ).strip().lower()

    if prioridade == "media":
        prioridade = "média"

    chamado = {"numero": contador,
                "nome": nome, 
                "problema": problema, 
                "prioridade": prioridade}
    

    # Saída de dados
    print("\n=== CHAMADO REGISTRADO ===")
    print("Número do chamado:", contador)
    print("Solicitante:", nome)
    print("Problema:", problema)
    print("Prioridade:", prioridade)

    chamados.append(chamado)

    # Atualiza o contador
    contador = contador + 1

    # Pergunta se deseja continuar
    continuar = input("\nDeseja registrar outro chamado? (sim/não): ").strip().lower()

    while continuar not in("sim", "não", "nao"):
        print("Erro, resposta inválida")
        continuar = input("deseja continuar? (sim ou não):  ").strip().lower()

    
print("\nNexusDesk encerrado.")
