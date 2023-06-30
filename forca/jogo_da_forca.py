import random

def jogar():
    
    cabecalho()
    
    palavra_secreta = escolhe_palavra()
    
    letras_acertadas = ["_" for letra in palavra_secreta] 
    
    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)
    print("Dica: É uma fruta! ")
    
    while (not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip().lower()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1    
        else:
            erros += 1
            desenha_forca(erros)
       
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
            
                        
    if acertou:
        print("Você ganhou!!")
        mensagem_vencedor()
    else:
        print("Você perdeu!!")
        mensagem_perdedor(palavra_secreta)      
    print("Fim do Jogo!")
    
def cabecalho():
    print("*************************************")
    print("*** Bem Vindo ao Jogo da Forca!!! ***")
    print("*************************************")
    
def escolhe_palavra():
    arquivo = open ("palavras_forca.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era %s" %palavra_secreta)
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("  //                   \/\  ")
    print("  \|   XXXX     XXXX   | /   ")
    print("   |   XXXX     XXXX   |/     ")
    print("   |   XXX       XXX   |      ")
    print("   |                   |      ")
    print("   \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")
    
def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      . \:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
    
    print("Tentativa %d de 7" %erros)
      
if (__name__ == "__main__"):
    jogar()