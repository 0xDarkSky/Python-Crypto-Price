import requests
import time
import sys
import os

#os.system("clear")
os.system('cls' if os.name == 'nt' else 'clear')

LICENSE = """
MIT License

Copyright (c) 2021 QL0R

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contributors: QL0R

Licensed under the MIT License
"""

logo = """
   ░██████╗░██╗░░░░░░█████╗░██████╗░  ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░
   ██╔═══██╗██║░░░░░██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗
   ██║██╗██║██║░░░░░██║░░██║██████╔╝  ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║
   ╚██████╔╝██║░░░░░██║░░██║██╔══██╗  ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║
   ░╚═██╔═╝░███████╗╚█████╔╝██║░░██║  ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝
   ░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░\n
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def slow_type(y):
    for a in y:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.05)

def logo_type(v):
    for p in v:
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.005)


def fast_type(z):
    for x in z:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.02)


logo_type(logo)


slow_type("Time between responses (seconds)?\n")
x = input("")
sx = float(x)


def get_price_eur():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    specific_data = (data["bpi"]["EUR"]["rate"])
    print(specific_data)
    
    
def get_price_usd():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    otherspecific_data = (data["bpi"]["USD"]["rate"])
    print(otherspecific_data)
    

def choose_currency():
    slow_type("Choose currency to display (EUR - 1  or USD - 2)? \n")
    eurusd = input("")
    if eurusd == "1":
       unlimited_eur()
    elif eurusd == "2":
       unlimited_usd()
    else: 
       fast_type("Wrong answer, please choose 1 or 2!\n")
       neweurusd = input("")
       if neweurusd == "1":
          unlimited_eur()
       elif neweurusd == "2":
          unlimited_usd()
       else:
          fast_type("Wrong answer again!\n")
          exit()  

def unlimited_eur():
    while True:
        try:
           get_price_eur() 
           time.sleep(sx) 
        except KeyboardInterrupt:
           print("\nExit by user input\n")
           time.sleep(0.5)
           os.system('cls' if os.name == 'nt' else 'clear')
           exit()


def unlimited_usd():
     while True:
        try:
           get_price_usd() 
           time.sleep(sx) 
        except KeyboardInterrupt:
           fast_type("\nExit by user input\n")
           time.sleep(0.5)
           os.system('cls' if os.name == 'nt' else 'clear')
           exit()


choose_currency()
