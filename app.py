# Importando e iniciando a biblioteca Colorama
from colorama import *
init()
# Importando e iniciando a biblioteca Colorama

nivel = float(input("Qual o nível no reservatório? "))

# Variáveis que definem cada nível. 
# O primeiro valor [0] é a quantidade de água que estará relacionado a cada nível, o segundo [1] é a cor do texto que será exibido e o terceiro [2] é o texto que será exibido.
NIVEL_1 = [2 , Fore.RED, "Nível 1 - Muito baixo (crítico)"]
NIVEL_2 = [4 , Fore.YELLOW, "Nível 2 - Baixo"]
NIVEL_3 = [6 , Fore.GREEN, "Nível 3 - Médio"]
NIVEL_4 = [8 , Fore.CYAN, "Nível 4 - Alto"]
NIVEL_5 = [10 , Fore.BLUE, "Nível 5 - Muito alto (alerta)"]


if nivel < 0:
    print(Fore.RED + "Inválido")
elif nivel > NIVEL_5[0]:
    print(Fore.RED + "O reservatório transbordou!")
elif nivel <= NIVEL_1[0]:
    print(NIVEL_1[1] + NIVEL_1[2])
elif nivel <= NIVEL_2[0]:
    print(NIVEL_2[1] + NIVEL_2[2])
elif nivel <= NIVEL_3[0]:
    print(NIVEL_3[1] + NIVEL_3[2])
elif nivel <= NIVEL_4[0]:
    print(NIVEL_4[1] + NIVEL_4[2])
elif nivel <= NIVEL_5[0]:
    print(NIVEL_5[1] + NIVEL_5[2])