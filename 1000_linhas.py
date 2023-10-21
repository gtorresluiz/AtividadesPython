arquivo = open('cadastro.txt', 'w')

nome = input("qual seu nome? ")
idade = input("qual sua idade? ")

arquivo.write(f"nome = {nome}\n")
arquivo.write(f"idade = {int(idade)}")
arquivo.close()