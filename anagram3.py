import random

print("Bem Vind(o/a)! Queres um anagrama? Então..")
#print("São de borla, por isso faz os que quiseres!")

def palavra_input():
    palavra = input("Escreve uma palavra: ").lower()
    palavra = [letra for letra in palavra]
    
    return palavra
    
def anagrama_rng():
    anagrama = ""
    for letra in range(len(palavra)):
        anagrama = anagrama + palavra.pop(random.randrange(len(palavra)))

    print('\n--> ', anagrama)
    return anagrama
    
def anagrama_regen(anagrama):
    anagrama = [letra for letra in anagrama]
    novo_anagrama = ""
    for letra in range(len(anagrama)):
        novo_anagrama = novo_anagrama + anagrama.pop(random.randrange(len(anagrama)))

    print('\n--> ', novo_anagrama)
    return novo_anagrama
    
palavra = palavra_input()
anagrama = anagrama_rng()

decisao = input("\nQueres outro com esta palavra? (sim/nao): ").casefold()

if decisao == "sim" or decisao == "s" or decisao == "y":
    anagrama_regen(anagrama)

else:
    print("\nAdeus")



input('\nCarrega ENTER para fechar a janela.')
