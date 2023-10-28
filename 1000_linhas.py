arquivo =  open('1000linhas.txt', 'w')

contador = 0

while contador <= 100:
  arquivo.write(f"linha n{contador}\n")
  contador += 1

with open('1000linhas.txt', 'r') as arquivo:
    leitura = arquivo.read()
  
print(leitura) 
