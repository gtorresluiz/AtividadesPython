import csv

dados_alunos = [
    ['Nome', 'idade','87'],
    ['joao','25','92'],
    ['maria', '30', '80'],
    ['jose', '35', '70']
]

with open('alunos.csv', 'w', newline='') as arq_csv:
    escritor = csv.writer(arq_csv)
    for linha in dados_alunos:
        escritor.writerow(linha)

novo_aluno = ['davi','23','89']

with open('alunos.csv', 'a', newline='') as arq_csv:
    escritor = csv.writer(arq_csv)
    escritor.writerow(novo_aluno)
#
with open('alunos.csv', 'r', newline='') as arq_csv:
    linhas = list(csv.reader(arq_csv))

alunos_aprovados=[]

for linha in linhas:
    if float(linha[2]) >= 90:
      alunos_aprovados.append(linha[0])
    

with open('alunos_aprovados.csv', 'w', newline='') as arq_csv: 
    escritor = csv.writer(arq_csv)
    escritor.writerow(alunos_aprovados)

##


