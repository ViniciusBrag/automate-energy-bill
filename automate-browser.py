from time import sleep
from helium import *
import os 
from dotenv import load_dotenv



load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

start_firefox('https://www.cpfl.com.br/login')

#sleep for 1.5 seconds
sleep(1)

#Clik in terms of cookies
if Text('Accept All Cookies').exists():
    click('Accept All Cookies')

## Click in signin 
click('Entrar')

#wait 1.5 seconds
sleep(1.5)

#verify if value 'e-mail' is correct.
write(login, into='Endereço de e-mail')
    
# If value is correct write password.
write(password, into='Senha')

click('Entrar')

sleep(5)
click('Ativa')




        


        





