#sumar dos numeros y mostrar el resultado
def getSum(number1, number2):
    return number1 + number2

#mostrar el resultado
def showResult(message, result):
    return f"{message} {result}"

print("Dime un numero: ")
num1 = float(input())
print("Dime otro numero: ")
num2 = float(input()) 
sum = getSum(num1, num2)
print(showResult("El resultado de la suma es:", sum))