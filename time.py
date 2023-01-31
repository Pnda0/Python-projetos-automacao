from calendar import month
from datetime import date, datetime, timedelta
import locale
from threading import local
from datetime import time

# Print Hoje

hoje = date.today()
print(hoje)

# Escolher o dia e substitui-lo

ontem = hoje.replace(day=29)
print(ontem)

ano_passado = hoje.replace(year=2028)
print(ano_passado)

mes_passado = hoje.replace(month=5)
print(mes_passado)

# Caso a gente deseje formatar a data 

data_ifen = hoje.strftime('%d-%m-%Y')
print(data_ifen)

data_portugues = hoje.strftime('%d de %B de %Y')
print(data_portugues)

data_nome_numero = hoje.strftime('%A, %d de %B de %Y')
print(data_nome_numero)

# Data com Localidade

local_brasil = locale.setlocale(locale.LC_ALL, '')
print(local_brasil)

# Todos os locais disponíveis
todos_locais = locale.locale_alias
#print(todos_locais)

# Windows Locale, mesma coisa só que simplificado

todos_locais_windows = locale.windows_locale
#print(todos_locais_windows)

yesterday = hoje - timedelta(days=1)
print(yesterday)

tomorrow = hoje + timedelta(days=1)
print(tomorrow)

next_week = hoje + timedelta(days=7)
print(next_week)

last_month = hoje - timedelta(days=30)
print(last_month)

# Trabalhando com horas


relogio = time.fromisoformat('14:00')
print(relogio)

agora = datetime.now()
print(agora)

# Formatando hora
t = agora.strftime('%H:%M')
print(t)

# Substituindo a hora, pelo horário desejado
t2 = agora.replace(hour=15, minute=3)
print(t2)


t_simplificado = t2.strftime('%H:%M')
print(t_simplificado)

# Data de hoje

hoje = datetime.today()

# Formatando a data

data_de_hoje = hoje.strftime('%d%m%Y')

# usando o time delta para definir quantos dias desejamos somar ou subtrair

today = hoje - timedelta(days=20)

# Formatando a data de hoje após ser transformada em timedelta
data_comeco = today.strftime('%d%m%Y')

# Utilizando um while para finalizar execução do código a x hora.
while True:
    agora = datetime.now()
    t = agora.strftime('%H:%M')
    t2 = agora.replace(hour=18, minute=0)
    t_simplificado = t2.strftime('%H:%M')
    if t == t_simplificado:
        print('Se acabou')
        break












