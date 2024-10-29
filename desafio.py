import textwrap

def exibir_menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))


def realizar_deposito(saldo_atual, valor_deposito, historico, /):
    if valor_deposito > 0:
        saldo_atual += valor_deposito
        historico += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n❌ Operação falhou! Valor inválido.")
    
    return saldo_atual, historico


def realizar_saque(*, saldo_atual, valor_saque, historico, limite, total_saques, max_saques):
    if valor_saque > saldo_atual:
        print("\n❌ Saldo insuficiente.")
    elif valor_saque > limite:
        print("\n❌ Valor do saque excede o limite.")
    elif total_saques >= max_saques:
        print("\n❌ Número máximo de saques atingido.")
    elif valor_saque > 0:
        saldo_atual -= valor_saque
        historico += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        total_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n❌ Valor inválido.")
    
    return saldo_atual, historico


def mostrar_extrato(saldo_atual, /, *, historico):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not historico else historico)
    print(f"\nSaldo:\t\tR$ {saldo_atual:.2f}")
    print("==========================================")


def adicionar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = encontrar_usuario(cpf, usuarios)
    
    if usuario_existente:
        print("\n❌ Já existe usuário com esse CPF!")
        return
    
    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")
    
    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")


def encontrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def abrir_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n❌ Usuário não encontrado. Criação de conta encerrada.")


def listar_todas_contas(contas):
    for conta in contas:
        detalhes_conta = f"""\n
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(detalhes_conta))


def sistema_banco():
    MAX_SAQUES = 3
    CODIGO_AGENCIA = "0001"
    
    saldo_atual = 0
    limite_saque = 500
    historico_movimentacoes = ""
    total_saques = 0
    usuarios_cadastrados = []
    contas_abertas = []
    
    while True:
        escolha = exibir_menu()
        
        if escolha == "d":
            valor_deposito = float(input("Valor do depósito: "))
            saldo_atual, historico_movimentacoes = realizar_deposito(saldo_atual, valor_deposito, historico_movimentacoes)
        
        elif escolha == "s":
            valor_saque = float(input("Valor do saque: "))
            saldo_atual, historico_movimentacoes = realizar_saque(
                saldo_atual=saldo_atual,
                valor_saque=valor_saque,
                historico=historico_movimentacoes,
                limite=limite_saque,
                total_saques=total_saques,
                max_saques=MAX_SAQUES
            )
        
        elif escolha == "e":
            mostrar_extrato(saldo_atual, historico=historico_movimentacoes)
        
        elif escolha == "nu":
            adicionar_usuario(usuarios_cadastrados)
        
        elif escolha == "nc":
            numero_conta = len(contas_abertas) + 1
            nova_conta = abrir_conta(CODIGO_AGENCIA, numero_conta, usuarios_cadastrados)
            if nova_conta:
                contas_abertas.append(nova_conta)
        
        elif escolha == "lc":
            listar_todas_contas(contas_abertas)
        
        elif escolha == "q":
            break
        
        else:
            print("Operação inválida. Tente novamente.")


sistema_banco()