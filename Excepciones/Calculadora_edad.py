from colorama import Fore, Style
while True:
    try:
        edad = int(input("Edad: "))
        print("Edad Registrada: ", edad)
        break
    except ValueError:
        print(Fore.RED + "Error: Debe ingresar un número entero." + Style.RESET_ALL)
        print(Style.RESET_ALL)
print(Fore.GREEN + "Edad ingresada correctamente." + Style.RESET_ALL)