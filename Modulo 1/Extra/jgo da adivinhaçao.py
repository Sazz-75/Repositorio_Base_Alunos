import random

print ("supe jogo da adivinhaçao ")

numero_magico = random.randint(1,100)

numero_adivinhaçao = int(input("dgite o numero entre 1 e 100: "))

while numero_adivinhaçao != numero_magico:
    

    if numero_adivinhaçao > numero_magico:
        print("o numero é menor: ")

    else:
        print("o numero é maior")

    numero_adivinhaçao = int(input("tente novamente: "))


print("parabens voce acertou")