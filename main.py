# Python3 Telegram Bot
# Crawls the KUHS website and triggers a message on Telegram when the result is announced
import requests
import re
import time
from bs4 import BeautifulSoup
import operator
from collections import Counter


def telegram_bot_sendtext(bot_message):
    bot_token = '' #Enter Telegram Bot Token
    bot_chatID = '' #Enter Telgram Chat ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def start(url):

    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')
    searched_word = 'Third Professional MBBS Degree Part II Supplementary Examinations'

    results = soup.findAll(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    print(results)
    if(len(results)!= 0):
        #print('Result Announced') 
        my_message = 'Result Announced'
        telegram_bot_sendtext(my_message)



if __name__ == '__main__':
    start("http://14.139.185.154/kuhs_new/index.php/25-kuhs-exam-sec/exam-results/medical-results")
