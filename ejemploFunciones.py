url = input("URL: ")
port = int(raw_input("PORT: "))

print type(port) #Tipo de datos

if url.startswith("http://"):
    url = url.replace("http://","")
    print "Ud uso protocolo normal"
elif url.startswith("https://"):
    url = url.replace("https://","")
    print "Ud puede comprar en linea tranquilamente"
elif url.startswith("ftp://"): #file transfer protocol
    print "Puede subir archivos a su servidor"
print url
