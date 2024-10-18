from time import sleep
from helium import *
import os 
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

driver = start_firefox('https://www.cpfl.com.br/login')

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

#Signin
click('Entrar')


#load the page complete.
sleep(7)

element_label_option = driver.find_elements(By.CLASS_NAME, "option")


#click in the element 'ativa'
for element in element_label_option:
    element.click()

#wait seconds to appear the button 'Avançar'
sleep(2)

#find element 'Avançar'
next = driver.find_element(By.ID, "btn-buscar")

#scrool until button 'Avançar'
driver.execute_script("arguments[0].scrollIntoView(true);", next)

#wait to after scroll to element.
sleep(0.8)

#click the element.
next.click()
        


        





