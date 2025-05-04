import time 
import string
from unicodedata import numeric
from colorama import Fore, init

init()

color = {
    "yellow": Fore.YELLOW,
    "green": Fore.GREEN,
    "red": Fore.RED,
    "magenta": Fore.MAGENTA,
    "reset": Fore.RESET,
    "cyan": Fore.CYAN,
    "blue": Fore.BLUE, 
}

print(f"{color['yellow']}-=-{color['reset']}" * 20)

print(f"{color['magenta']}Analisar ortografica Texto")
print(f"Estará disponivel ao final do texto{color['reset']}")


print(f"{color['yellow']}-=-{color['reset']}" * 20)

print(" ")

text = input(f"{color['cyan']}Digite aqui seu texto:{color['reset']}\n").strip()


print(f"{color['yellow']}-=-{color['reset']}" * 20)

print(f"{color['green']}Gerando dados....{color['reset']}")
time.sleep(3)
print(f"{color['green']}Dados carregados{color['reset']}")

print(f"{color['yellow']}-=-{color['reset']}" * 20)



text_sem_espaco = len(''.join(text.split()))

print(" ")

print(f"Seu texto tem {text_sem_espaco} caracteres\n")

text_sem_espaco = ''.join(text.split())
total_numeros = sum(numero.isnumeric() for numero in text) 
total_letras = sum(letras.isalpha() for letras in text)
palavras = text.split()
num_palavras = len(palavras)
pontuacoes = string.punctuation
pontuacao = sum(1 for letra in text if letra in pontuacoes)

print(f"Seu texto tem {total_letras} letras\n")

print(f"{pontuacao} sinais de pontuação\n")

print(f"Seu texto tem {total_numeros} numeros\n")

print(f"Seu texto tem {num_palavras} palavras\n")

print(f"Primeira palavra: {palavras[0]}\n")

print(f"Ultima palavra: {palavras[-1]}\n")

print(f"{color['cyan']}Sendo:{color['reset']}")

print(" ")

vogais = "aeiouAEIOU"

qtd_vogais = sum(1 for letra in text if letra in vogais)

if qtd_vogais > 0:

    print(f"{qtd_vogais} vogais")
    print("São {:.2f}% do total de {}".format((qtd_vogais / total_letras) * 100, total_letras))

else:

    print("0 vogais")
    print("São {:.2f}% dp total de {}".format((qtd_vogais / total_letras) * 100, total_letras))
    print("Não há letras no texto, não é possível calcular a porcentagem de vogais.")

print(" ")

qtd_consoantes = sum( 1 for letras in text if letras not in vogais and letras.isalpha())

if qtd_consoantes > 0:

    print(f"{qtd_consoantes} consoantes")
    print("São {:.2f}% do total de {}".format((qtd_consoantes / total_letras) * 100, total_letras))

else:

    print("0 consoantes")
    print("São {:.2f}% do total de {}".format((qtd_consoantes / total_letras) * 100, total_letras))
    print("Não há letras no texto, não é possível calcular a porcentagem de consoantes.")

print(" ")

qtd_maiuscula = sum(1 for letra in text if letra.isupper())

if qtd_maiuscula > 0:
    
    print(f"{qtd_maiuscula} letras maiusculas")
    print("São {:.2f}% do total de {}".format((qtd_maiuscula / total_letras) * 100, total_letras))
    
else:

    print(" 0 letras maiusculas")
    print("São {:.2f}% do total de {}".format((qtd_maiuscula / total_letras) * 100, total_letras))
    print("Não há letras no texto, não é possível calcular a porcentagem de maiusculas.")

print(" ")

qtd_minusculas = sum(1 for letra in text if letra.islower())

if qtd_minusculas > 0:

    print(f"{qtd_minusculas} letras minusculas")
    print("São {:.2f}% do total de {}".format((qtd_minusculas / total_letras) * 100, total_letras))

else:

    print(" 0 letras minusculas")
    print("São {:.2f}% do total de {}".format((qtd_minusculas / total_letras) * 100, total_letras))
    print("Não há letras no texto, não é possível calcular a porcentagem de minusculas.")


print(" ")

print(f"{color['yellow']}-=-{color['reset']}" * 20)

letras_separadas = str(input(f"{color["cyan"]}Quantidade de uma letra especifica ?(Sim/Não){color['reset']}\n"))

if not letras_separadas.isalpha():

    print(f"{color['red']}Erro, reinicie o processo{color['reset']}")

elif letras_separadas in ["sim", "Sim", "ss", "ssim"]: 

    letra_valor = str(input(f"{color['cyan']}Qual letra:{color['reset']} "))
    print(f"Seu texto tem {letra_valor} letras {letra_valor}")

else:

    print("Ok")

print(f"{color['yellow']}-=-{color['reset']}" * 20)
    