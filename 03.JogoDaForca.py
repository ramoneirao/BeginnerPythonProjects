import requests
import re
from lxml import html  
import csv,os,json
import string 

def carrega_palavra():
    url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1"
    resposta = requests.get(url)
    elemento = html.fromstring(resposta.content)
    palavra_secreta = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
    palavra_secreta = palavra_secreta[0].strip()
    return palavra_secreta


def forca():
    palavra = carrega_palavra().upper()
    letras_palavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()
    tentativas = 6

    while len(letras_palavra) > 0 and tentativas > 0: 
        print('Letras usadas: ', ' '.join(letras_usadas))
        print(f'Você tem {tentativas} tentativas!')
        lista_palavra = [letra if letra in letras_usadas else '-' for letra in palavra]
        print('Palvra atual: ', ' '.join(lista_palavra))

        letra_usuario = input('Tente uma letra: ').upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in letras_palavra:
                letras_palavra.remove(letra_usuario) 
            
            else:
                tentativas = tentativas - 1 
                print('Essa letra não está na palavra!')

        elif letra_usuario in letras_usadas:
            print('Você já escolheu essa letra anteriormente!')

        else:
            print('Caracter inválido!')

    if tentativas == 0:
        print(f'Você morreu, a palavra era {palavra}')
    print(f'Você acertou a palavra {palavra}. Parabéns!')

forca()