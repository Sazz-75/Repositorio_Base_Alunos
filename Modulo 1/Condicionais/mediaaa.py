
nome = input("Digite o seu nome: ")

primeira_nota = float(input("digite a primeira nota:"))
segunda_nota = float(input("digite sua sengunda nota:"))
terceira_nota = float(input("digite a terceira nota: "))

media = ( primeira_nota + segunda_nota + terceira_nota) / 3
print(media)


if media >= 7:
    print("vôce passou !")
elif media > 4:
    print("voce nao passou ")
else:
    print("voce esta reprovado !")

