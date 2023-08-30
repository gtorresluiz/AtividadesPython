# Eduardo Fedeli 550132
# Otavio Vitoriano 552012
# Sofia Coutinho 552534
# Gabriel Torres 98600
# Jéssica Brum 97944

# Função para retornar a saudação com base no horário
def msg():
    hora_atual = datetime.now().hour

    if hora_atual < 12:
        return "----- Bom dia -----!"
    elif hora_atual < 18:
        return "----- Boa tarde -----!"
    else:
        return "----- Boa noite -----!"
    
from datetime import datetime

estoqueGarrafas = {
    "1": ("Vinho tinto", 5, 149.90),
    "2": ("Vinho branco", 10, 99.90),
    "3": ("Vinho rosé", 7, 79.90),
    "4": ("Vinho do Porto", 3, 199.90),
}
estoqueRolhas = {
    "1": ("Rolha de cortiça", 100, 0.50),
    "2": ("Rolha sintética", 50, 0.30),
    "3": ("Rolha de champanhe", 20, 1.20),
}
estoqueRotulos = {
    "1": ("Rótulo clássico", 50, 1.50),
    "2": ("Rótulo vintage", 30, 2.50),
    "3": ("Rótulo artístico", 20, 3.75),
    "4": ("Rótulo personalizado", 10, 5.00),
}
estoqueCaixas = {
    "1": ("Caixa de madeira simples", 15, 9.90),
    "2": ("Caixa de madeira decorada", 5, 14.90),
    "3": ("Caixa de papelão", 30, 5.50),
}

# função que exibe o estoque completo
def exibirEstoque():
    print("----- Estoque Completo -----")
    
    print("\nEstoque de Garrafas:")
    print(estoqueGarrafas)
    
    print("\nEstoque de Rolhas:")
    print(estoqueRolhas)
    
    print("\nEstoque de Rótulos:")
    print(estoqueRotulos)
    
    print("\nEstoque de Caixas:")
    print(estoqueCaixas)

# Função para comprar vinho
def compraVinho():
    pos = ["sim", "Sim", "S", "s", "Ss", "ss"]
    neg = ["não","Não","nao", "Nao", "N", "n", "Ns", "nn"]
    usuarios = {}

    # Cadastro do usuário
    dec = None
    while dec is None:
        print("Bem-vindo ao sistema de cadastro!")
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        if usuario in usuarios:
            print("Usuário já existe. Por favor, tente novamente.")
        else:
            usuarios[usuario] = senha
            print("Usuário cadastrado com sucesso!")
            break

    # Login do usuário
    while True:
        nome = None
        while nome is None:
            nome = input("Digite seu primeiro nome: ")
            if nome == "":
                print("Por favor, preencha seu nome.")
                nome = None

        sobrenome = input("Digite seu sobrenome: ")
        if sobrenome == "":
            print("Por favor, preencha seu sobrenome.")
            sobrenome = None

        idade = None

        while idade is None:
            try:
                idade = int(input("Digite sua idade: "))
                if idade < 0:
                    print("Por favor, digite uma idade válida.")
                    idade = None
                elif idade < 18:
                    print("O site é apenas para maiores de 18 anos!")
                    print(f"Obrigado, {msg()}")  # Correção aqui
                    exit()
            except ValueError:
                print("Por favor, digite um valor numérico para a idade.")
                idade = None

        # Cadastro de endereço
        rua = None
        while rua is None:
            rua = input("Digite o nome da sua rua: ")
            if rua == "":
                print("Por favor, preencha o nome da rua.")
                rua = None

        bairro = None
        while bairro is None:
            bairro = input("Digite o bairro: ")
            if bairro == "":
                print("Por favor, preencha o nome do bairro.")
                bairro = None

        num = None
        while num is None:
            num = input("Digite o número da casa: ")
            if num == "":
                print("Por favor, preencha o número da casa.")
                num = None

        cep = None
        while cep is None:
            cep_str = input("Digite o CEP: ")
            if cep_str == "":
                print("Por favor, preencha o CEP.")
                cep = None
            else:
                try:
                    cep = int(cep_str)
                except ValueError:
                    print("Por favor, digite um CEP válido.")
                    cep = None

        comp = input("Digite o complemento (opcional): ")

        print(f"Esses são seus dados:\nNome: {nome} {sobrenome}\nIdade: {idade}\nSeus dados de endereço são:\nRua: {rua}\nBairro: {bairro}\nNúmero: {num}\nCEP: {cep}\nComplemento: {comp}\n")
     
        #fim do cadastro, seleção dos vinhos
        
        print("Agora vamos para o menu de seleção dos vinhos")
        
        opcVinhos = ["1","2","3","4"]  
        print("Vinhos individuais ou caixas de 6 e 12 unidades")
        print(" 1 - Vinho Tinto - R$149.99\n 2 - Vinho Branco - R$99,99\n 3 - Vinho Rosé - R$79.99\n 4 - Vinho do Porto - R$199,99")
    
        vinSel = None
        while vinSel is None:
            vinSel = input("Selecione qual vinho deseja: (1,2,3,4)")
        if vinSel not in opcVinhos:
            print("Por favor, digite uma opção válida (1,2,3,4)")
            vinSel = None
        else:
            print("1. Garrafas")
            print("2. Caixas")
            opcCompra = input("Deseja comprar em garrafas individuais ou em caixas de 6 ou 12 unidades? ")
            if opcCompra == "1":
                quantCompra = int(input("Quantidade desejada: "))
            elif opcCompra == "2":
                quantCaixas = int(input("Quantidade de caixas desejada: "))
                quantCompra = quantCaixas * (6 if vinSel != "4" else 12)
            
            if opcCompra in ["1", "2"]:
                if quantCompra <= 0:
                    print("Quantidade inválida. Digite um valor positivo.")
                    vinSel = None
                else:
                    valorUnitario = 0
                    if vinSel == "1":
                        valorUnitario = 149.99
                    elif vinSel == "2":
                        valorUnitario = 99.99
                    elif vinSel == "3":
                        valorUnitario = 79.99
                    elif vinSel == "4":
                        valorUnitario = 199.99

                    valorT = valorUnitario * quantCompra
                            
                    confirmaSel = input("Deseja confirmar a seleção? (Sim/Não): ")
                    if confirmaSel in pos:
                        if vinSel == "1":
                            produtoEscolhido = estoqueGarrafas
                            nomeProduto = "Vinho Tinto"
                            valorUnitario = 149.99
                        elif vinSel == "2":
                            produtoEscolhido = estoqueGarrafas
                            nomeProduto = "Vinho Branco"
                            valorUnitario = 99.99
                        elif vinSel == "3":
                            produtoEscolhido = estoqueGarrafas
                            nomeProduto = "Vinho Rosé"
                            valorUnitario = 79.99
                        elif vinSel == "4":
                            produtoEscolhido = estoqueGarrafas
                            nomeProduto = "Vinho do Porto"
                            valorUnitario = 199.99

                        if opcCompra == "1":
                            estoqueDisponivel = produtoEscolhido[vinSel][1]
                        elif opcCompra == "2":
                            caixasNecessarias = quantCompra // 6 if vinSel != "4" else quantCompra // 12
                            estoqueDisponivel = produtoEscolhido[vinSel][1] // caixasNecessarias
                            if quantCompra > estoqueDisponivel:
                                print("Não temos esta quantidade do vinho %s no estoque. Quantidade no estoque = %d" % (nomeProduto, estoqueDisponivel))
                                continue
                            else:
                                print("Quantidade disponível no estoque")
                                valor_total = valorUnitario * quantCompra
                                print("O valor total é: R$%5.2f" % valor_total)
                                
                                # Função para calcular o valor do pedido com frete
                                def valorFinal(valorT):
                                    frete = 10 + valorT * 0.1
                                    return valorT + frete + 10
                                
                                if valorT > 100:
                                    print("Valor mínimo de R$100,00 não alcançado\n Selecione mais vinhos dessa vez para realizar a compra")
                                    quantCompra = 0
                                    vinSel = None
                                else:
                                    print("O valor final com frete é R$%5.2f" % valorFinal(valorT))
                                    dataEntrega = input("Digite a data de entrega (dd/mm/aaaa): ")
                                    print("Pedido confirmado!")
                                    print("Data de entrega:", dataEntrega)
                                    print("Total a pagar: R$%5.2f" % valorFinal(valorT))
                                    print("Você comprou %d vinho(s) da categoria %s" %(quantCompra, vinSel))
                                    print("Muito obrigado pela preferência %s. Volte Sempre!" %nome)

                    elif confirmaSel in neg:
                        print("Muito bem, pode alterar seu pedido")
                        vinSel = None

                    else:
                        print("Dê uma resposta válida! (Sim/Não)")
                        confirmaSel = None

    # Função para exibir o menu e realizar as operações
def exibir_menu():
        while True:
            print(msg())
            print("----- Vinheria Agnello -----")
            print("1. Verificar estoque")
            print("2. Comprar vinho")
            print("3. Sair")
            opcao = input("Digite a opção desejada: ")

            match opcao:
                case "1":
                    exibirEstoque()
                case "2":
                    compraVinho()
                case "3":
                    print("Encerrando o programa...")
                    return
                case _:
                    print("Opção inválida! Por favor, digite uma opção válida.")

    # Executa o programa
exibir_menu()
