#1 - Importar a biblioteca Requests 
import requests

#2 - Definir a url do site 
url = 'http://www.example.com/'

#3 - Fazer uma requisição GET para a url 
r = requests.get(url)

#4 - Salvar os cookies 
cookies = r.cookies

#5 - Definir a url de login 
url_login = 'http://www.example.com/login/'

#6 - Definir os dados para login 
data = {'username': 'user', 'password': 'pass'} 

#7 - Fazer uma requisição POST para a url de login usando os cookies 
r_login = requests.post(url_login, cookies=cookies, data=data)

#8 - Verificar se o login foi feito com sucesso 
if r_login.status_code == 200: 
    print('Login com sucesso!') 
else: 
    print('login fail')