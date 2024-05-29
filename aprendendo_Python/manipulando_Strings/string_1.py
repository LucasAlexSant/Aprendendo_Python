nome = "lUcAs"

print(nome.upper()) #TUDO EM MAIUSCULO
print(nome.lower()) #TUDO EM MINUSCULO
print(nome.title()) #PRIMEIRO EM MAIUSCULO

texto = "   Ola mundo!   "

print(texto + ".")
print(texto.strip() )  
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu+ "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))
