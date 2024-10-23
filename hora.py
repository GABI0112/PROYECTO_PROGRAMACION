from datetime import datetime

nombre = "Gabriel"
hora = datetime. now().hour

def Saluda (nombre):
    if (hora > 3 and hora <= 12):
        saludo = "Buenos Dias"
    elif (hora > 12 and hora < 19):
        saludo = "Buenas Tardes"
    elif (hora > 19 and hora <=3):
        saludo = "Buenas Noches"
    else:
        saludo = "Buen Dia"
    return saludo , nombre
    

print (Saluda(nombre))