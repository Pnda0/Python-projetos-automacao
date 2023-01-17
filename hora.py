from calendar import month
from datetime import date, datetime, timedelta
import locale
from threading import local
from datetime import time


while True:
    # Data e hora de hoje de acordo com seu sistema operacional
    agora = datetime.now()
    # Definindo a variável tempo e formatando somente com o desejado, no nosso caso hora e minuto
    t = agora.strftime('%H:%M')
    # Agora substituindo a hora atual com a hora que desejamos 
    t2 = agora.replace(hour=21, minute=4)
    t_simplificado = t2.strftime('%H:%M')

    if t >= t_simplificado:
        print('Se acabou')
        break