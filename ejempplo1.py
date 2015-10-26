texto = raw_input("Escriba el texto a cifrar")
codigo = ""
for letra in texto:
    codigo += chr(ord(letra)+3)

print "El texto cifrado es: %s" %codigo
print ""
