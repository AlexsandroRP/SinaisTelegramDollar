import requests
from rich import print
from datetime import datetime
from time import sleep
import os


def send_img(link_imagens, chat_id, caption):
    token = '6283454675:AAH4zKUvNkuUwSeBhly_r8HXrNtZiIMwXdA'
    for link in link_imagens:
        requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')

def get_msgs(only_last_msg=False):
    update_id = None
    token = '6283454675:AAH4zKUvNkuUwSeBhly_r8HXrNtZiIMwXdA'
    data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    if len(data.json()['result']) > 0:
        if only_last_msg == True:
            update_id = data.json()['result'][-1]['update_id']
            data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}')
        print(data.json())
        print('#'*10)
    else:
        print(data.json())    
        print('#'*10)        


while True:
    result = requests.get('https://economia.awesomeapi.com.br/json/last/USD-MXN')
    current_amount = float(result.json()['USDMXN']['ask'])
    current_date = datetime.today().strftime('%d/%m/%Y - %H:%m')
    if current_amount <= 19:
        images = ['https://i.ibb.co/Fmr3M8j/dolar.webp']

        msg = f'💲Dólar: $ {current_amount}{os.linesep}🕑Date: {current_date}{os.linesep}💳Buy now: www.buydollar.com'
        send_img(link_imagens=images, 
        chat_id='-1001736449922', caption=msg)  
    else:
        pass   
    sleep(30)        
