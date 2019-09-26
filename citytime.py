from colorama import init
from colorama import Fore, Back
from datetime import datetime 
from datetime import date, time
import requests
import re

init()

def timeincity():

    #today = date.today()
    timenow = datetime.now().strftime('%H:%M:%S')

    #print('{}.{}.{} '.format(today.day, today.month, today.year))        (Просто для прикола(учился юзать datatime))

    print(Back.CYAN, Fore.BLACK, f'Hello, now in your city {timenow} but, what about, other parts of world??')

    work = True
    while work:

        zone = input('Enter continent: ')
        city = input('Enter name of city: ')

        r = requests.get(f'http://worldtimeapi.org/api/timezone/{zone.capitalize()}/{city.capitalize()}').json()
        x = re.findall("\d{2}:\d{2}:\d{2}", str(r))
        print(x)
        if x == []:
            print('Invalid continent or city.')
        else:
            print(f'Time, in {city.capitalize()}: {x[-1]}')
        end = input('If you want to exit, press any key+Enter. To contine press Enter. ')
        if end != '':
            work = False
        


timeincity()

