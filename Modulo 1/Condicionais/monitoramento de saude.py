peso = float(input("escreva seu peso: "))
altura = float(input("escreva sua altura: "))

imc = peso / (altura * altura)

print(imc)


if imc < 18.5:
    print("abaixo do peso !")

elif imc < 24.9:
    print("peso nomal ")
elif imc < 29.9:
    print("sobrepeso")
elif imc < 34.9:
    print("obesidade grau 1")
elif imc < 39.9:
    print("obesidade grau 2")
else:
    print("obesidade grau 3")



