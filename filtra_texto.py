
#Deixa todos os textos agrupados e em minúsculo

def filtrar_texto(texto):
    texto = texto.lower()
    texto = texto.replace(" ","")
    return texto


texto = filtrar_texto(input("digite um texto \n"))
print(texto)