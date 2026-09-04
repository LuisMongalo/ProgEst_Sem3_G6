#Registra las edades de n cantidades de personas y mostrar la edad mas alta y mas baja y la cantidad de personas registradas.
ages = []
def addAge(age):
    ages.append(age)
   

def getMaxAge():
    maxAge = ages[0]
    for age in ages:
        if age > maxAge:
            maxAge = age
    return maxAge

def getMinAge():
    minAge = ages[0]
    for age in ages:
        if age < minAge:
            minAge = age
    return minAge

def showSize():
    return len(ages)

def showAges():
    return ages

while True:
    try:
        age = int(input("Dime tu edad: "))
        if(age > 3):
           addAge(age)
        else:
            print("Debe ser un numero mayor a 3")
            
        answer = input("Sea ingresa otro [S - N]:")
        if answer.upper() != "S":
            break
            
            
    except ValueError:
        print("Debes ingresar un número entero.")
        
print ("Mostrar edades")
print ("Cantidad de personas registradas: ", {showSize()})
print(showAges())
print ("Edad mas alta: ", {getMaxAge()})
print ("Edad mas baja: ", {getMinAge()})
