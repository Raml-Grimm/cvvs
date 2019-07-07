from colorama import Fore, init
from bs4 import BeautifulSoup
from itertools import cycle
import time
import requests
import json
import threading
import hashlib
import random
import gateway1, gateway2, gateway3, os

def Main():
    banner = """
  {y}-----------------------------------------
  {y}||--------BloodHub Premium Chk---------||
  {y}||----------Python Based v3------------||
  {y}-----------------------------------------
  {b}-----------------------------------------
  {y}           - CHOOSE GATEWAY - 
  {b}-----------------------------------------
  {g}[1] {r} Gateway 1 CCV/CVV  | Stripe (2$ Charge)
  {g}[2] {r} Gateway 2 CVV 	| WorldPay (5$ Charge)
  {g}[3] {r} Gateway 3 CVV 	| Sagepay (5$ Charge)
  
  """.format(g=Fore.GREEN, b=Fore.GREEN, r=Fore.RED, y=Fore.YELLOW)
    print(banner)
    while True:
        try:
            gateway = str(input("Select > "))
        except KeyboardInterrupt:
            print(Fore.RED + '\n[-] ' + Fore.RESET + 'Recieved Exit.')
            exit(1)

        if gateway == "1":
            print()
            print(Fore.YELLOW + "[*] " + Fore.RESET + "Starting Gateway 1...")
            print()
            print("""
{re}      {ly}________________________________________________{re}
{re}     {ly}//----------{y}BloodHub Stripe Gate1{ly}--------------//{re}
{re}    {ly}//---------------{y}Termux Based v3{ly}---------------//{re}
{re}   {ly}//-------{r}Contact @BH_Adminn for checker{ly}--------//{re}
{re}  {ly}================================================ {re}
""".format(ly=Fore.GREEN, g=Fore.GREEN, y=Fore.YELLOW, r=Fore.RED, re=Fore.RESET))
            ranges = []
            try:
                with open('cc.txt', 'r') as ccs:
                    for x in ccs.read().split('\n'):
                        ranges.append(x)
                print(Fore.YELLOW + "[*] " + Fore.RESET + 'Checking ' + str(len(ranges)) + ' Credit Cards.')
                
                print(Fore.BLUE + "Start Checking at " + str(time.ctime()))
                print(Fore.RESET)
                
                cc = open('cc.txt', 'r')
                credit_cards = cc.read()
                ccEntry = 0

                if not os.path.exists("lives.txt"):
                    live = open("lives.txt", "w+")
                    live.write(" -- LIVES -- \n")
                    live.close()

                for x in credit_cards.split('\n'):
                    ccEntry += 1
                    try:
                        gateway1.StripeAutomate(x, ccEntry, 'Samsoden', "Smith")
                    except KeyboardInterrupt:
                        break
            except KeyboardInterrupt:
                pass
            print()
            print(Fore.GREEN + "[+] " + Fore.RESET + "Done on Gateway 1")
            print()

        elif gateway == "2":
            print()
            print(Fore.YELLOW + "[*] " + Fore.RESET + "Starting Gateway 2...")
            print()
            try:
                gateway2.Merchanttwo()
            except KeyboardInterrupt:
                pass
            print()
            print(Fore.GREEN + "[+] " + Fore.RESET + "Done on Gateway 2")
            print()
        elif gateway == "3":
            print()
            print(Fore.YELLOW + "[*] " + Fore.RESET + "Starting Gateway 3...")
            print()
            try:
                gateway3.Merchantthree()
            except KeyboardInterrupt:
                pass
            print()
            print(Fore.GREEN + "[+] " + Fore.RESET + "Done on Gateway 3")
            print()

Main()
