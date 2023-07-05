""" 
    Escribir dos funciones que permitan calcular:
        a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
        b) La duración en horas, minutos y segundos de un intervalo dado en segundos.
"""

def segundos_dado_intervalo(horas,minutos,segundos):
    # Calcula la duración en seg dado un intervalo(hora,minuto,segundo)
    resultado= horas*3600 + minutos*60 + segundos

    print(f"La duración de {horas}h, {minutos}m y {segundos}s; son: {resultado} segundos.")
    


def intervalo_dado_segundos(segundos):
    # Calcula la duración (hora,minuto,segundo) dado un intervalo de segundos
    hora= segundos//3600
    minutos= (segundos - hora*3600) // 60
    segundo= (segundos - hora*3600) % 60

    print(f"La duración de {segundos} segundos son {hora}h, {minutos}m, {segundo}s. ")


segundos_dado_intervalo(2,35,10)
intervalo_dado_segundos(4200)
intervalo_dado_segundos(980)