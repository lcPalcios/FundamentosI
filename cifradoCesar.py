print "....:::: MENU DE OPCIONES ::::...."
print """
    1. Cifrar
    2. Descifrar
    3. Salir
"""
op = input("Escriba el numero correspondiente a la opcio")
textoCifrado =""
if op ==1:
    textoPlano = raw_input("Escriba el texto a cifrar: ")
    #ciclo for
    for letra in textoPlano:
        textoCifrado += chr(ord(letra)+3)
    print "El texto cifrado es: %s" %textoCifrado
elif op==2:
    textoCifrado = raw_input("Escriba el texto Cifrado")

    for letra in textoCifrado:
        textoPlano += chr(ord(letra)-3)
    print "El texto Descrifrado es: %s " %textoPlano
else:
    print "App Finalizada"
