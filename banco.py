#classe cliente
class cliente:
    nome = ""
    sobrenome = ""
    email = ""
    telefone = 0
    endereco = ""
    nascimento = ""
    cpf = 0
    numero_cc = 0
    saldo = 0
    limite = 1000

banco_clientes_global = []
#1. função para adicionar um novo cliente
def adiciona_cliente(banco_clientes_local):
	cadastro = cliente()
	cadastro.nome = input("Nome: ")
	abc=cadastro.nome.isalpha()
	if abc == False:
		print('opção inválida, altere esse dado no cadastro')
	cadastro.sobrenome = input("Sobrenome: ")
	abc=cadastro.sobrenome.isalpha()
	if abc == False:
		print('opção inválida, altere esse dado no cadastro')
	cadastro.email = input("Email: ")
	cadastro.telefone = input("Telefone: ")
	cadastro.endereco = input("Endereço: ")
	cadastro.nascimento = input("Nascimento: ")
	cadastro.cpf = int(input("Apenas os números do CPF: "))
	cadastro.numero_cc = int(input("Número da Conta Corrente: "))
	cadastro.saldo = int(input("Saldo da Conta: "))
	banco_clientes_local.append(cadastro)
	return banco_clientes_local

#2. função para alterar os dados do cliente
def altera_cliente(banco_clientes_local):
    while True:
        if len(banco_clientes_local) != 0:
            cpf = int(input("Digite o CPF do cliente: "))
            aux = 0
            for posicao_lista in range(len(banco_clientes_local)):
                if banco_clientes_local[posicao_lista].cpf == cpf:
                    aux = 1
                    while True:
                        print("O que você deseja alterar:")
                        print("1.Nome")
                        print("2.Sobrenome")
                        print("3.Email")
                        print("4.Telefone")
                        print("5.Endereço")
                        print("6.Nascimento")
                        print("7.CPF")
                        print("8.Voltar para o menu")
                        opcao = int(input("Opção: "))
                        if opcao == 1:
                            banco_clientes_local[posicao_lista].nome = input("Digite o novo nome: ")
                        if opcao == 2:
                            banco_clientes_local[posicao_lista].sobrenome = input("Digite o novo sobrenome: ")
                        if opcao == 3:
                            banco_clientes_local[posicao_lista].email = input("Digite o novo email: ")
                        if opcao == 4:
                            banco_clientes_local[posicao_lista].telefone = input("Digite o novo telefone: ")
                        if opcao == 5:
                            banco_clientes_local[posicao_lista].endereco = input("Digite o novo endereço: ")
                        if opcao == 6:
                            banco_clientes_local[posicao_lista].nascimento = input("Digite o novo nascimento: ")
                        if opcao == 7:
                            banco_clientes_local[posicao_lista].cpf = input("Digite o novo CPF: ")
                        if opcao == 8:
                            break
                    break
            if aux == 0:
                print("CPF não encontrado.")
            else:
                break
        else:
            print("A lista está vazia.")
            break
    return banco_clientes_local

def exclui_cliente(banco_clientes_local):
    while True:
        if len(banco_clientes_local) != 0:
            cpf = int(input("Digite o CPF do cliente: "))
            aux = 0
            for posicao_lista in range(len(banco_clientes_local)):
                if banco_clientes_local[posicao_lista].cpf == cpf:
                    aux = 1
                    banco_clientes_local.pop(posicao_lista)
                    print("Cliente excluído com sucesso!")
                    break
            if aux == 0:
                print("CPF não encontrado.")
            else:
                break
        else:
            print("A lista está vazia.")
            break
    return banco_clientes_local

#4. função para listar os clientes
def listar_cliente(banco_clientes_local):
    while True:
        if len(banco_clientes_local) != 0:
            cpf = int(input("Digite o CPF do cliente: "))
            aux = 0
            for posicao_lista in range(len(banco_clientes_local)):
                if banco_clientes_local[posicao_lista].cpf == cpf:
                    aux = 1
                    print("Nome: ",banco_clientes_local[posicao_lista].nome)
                    print("Sobrenome: ",banco_clientes_local[posicao_lista].sobrenome)
                    print("Email: ",banco_clientes_local[posicao_lista].email)
                    print("Telefone: ",banco_clientes_local[posicao_lista].telefone)
                    print("Endereço: ",banco_clientes_local[posicao_lista].endereco)
                    print("Nascimento: ",banco_clientes_local[posicao_lista].nascimento)
                    print("CPF: ",banco_clientes_local[posicao_lista].cpf)
                    print("Número da Conta Corrente: ",banco_clientes_local[posicao_lista].numero_cc)
                    print("Saldo: ",banco_clientes_local[posicao_lista].saldo)
                    break
            if aux == 0:
                print("CPF não encontrado.")
            else:
                break
        else:
            print("A lista está vazia.")
            break
    return banco_clientes_local

#5. função para alterar o saldo do cliente
def alterar_saldo(banco_clientes_local):
	while True:
		if len(banco_clientes_local) != 0:
			cpf = int(input("Digite o CPF do cliente: "))
			aux = 0
			for posicao_lista in range(len(banco_clientes_local)):
				if banco_clientes_local[posicao_lista].cpf == cpf:
					aux = 1
					print("Selecione a opção")
					print("1. Depositar")
					print("2. Sacar")
					opcao = int(input("Opção"))
					if opcao == 1:
                        			valor = int(input("Valor para depositar: "))
                        			banco_clientes_local[posicao_lista].saldo += valor
					elif opcao == 2:
						valor= int(input("Valor para ser sacado: "))
						if valor > banco_clientes_local[posicao_lista].saldo:
                            				print("Seu saldo é insuficiente.")
						elif valor < banco_clientes_local[posicao_lista].saldo:
							banco_clientes_local[posicao_lista].saldo -= valor
					elif opcao != 1 and opcao != 2:
						print('Opção inválida')
				print("O seu saldo é: R$",banco_clientes_local[posicao_lista].saldo)
				break
			if aux == 0:
				print("CPF não encontrado.")
			else:
				break
		else:
			print("A lista está vazia.")
			break
	return banco_clientes_local

while True:
    #menu de seleção da operação
		print ("Menu:")
		print ("1.Inserir cliente")
		print ("2.Alterar dados do cliente")
		print ("3.Excluir cliente")
		print ("4.Listar clientes")
		print ("5.Movimentar valor financeiro")
		print ("6.Sair")
    #print para o gerente selecionar operação
		inicio=int(input("Opção:"))
		if inicio == 1:
			banco_clientes_global = adiciona_cliente(banco_clientes_global)
			print("Cadastro realizado com sucesso.")
		print('')
		print('')
		if inicio == 2:
			banco_clientes_global = altera_cliente(banco_clientes_global)
			print("Cadastro alterado com sucesso.")
		print('')
		print('')
		if inicio == 3:
			banco_clientes_global = exclui_cliente(banco_clientes_global)
		if inicio == 4:
			listar_cliente(banco_clientes_global)
		print('')
		print('')
		if inicio == 5:
			banco_clientes_global = alterar_saldo(banco_clientes_global)
		if inicio == 6:
			break
		if inicio < 1:
			print('Opção inválida')
		if inicio > 6:
			print('Opção inválida')
