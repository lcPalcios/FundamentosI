texto = raw_input("Escriba el texto a cifrar")

indice =0
letra =""
codigo =""
textoCifrado = ""
for indice in range(0,len(texto)):
    letra = texto[indice]
    codigo = ord(letra)+3
    textoCifrado += chr(codigo)

print "El texto cifrado es: %s" %textoCifrado
