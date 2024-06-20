import sys
import requests

try:
    if len(sys.argv)<2:
        sys.exit("Missing command-line argument")
    else:
        if sys.argv[1].isalpha()==True:
           sys.exit("Command-line argument is not a number")
        else:
            response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', auth=('user', 'pass'))
            usdRate=float(response.json()['bpi']['USD']['rate'].replace(",",""))
            price=usdRate*float(sys.argv[1])
            print(f"${price:,.4f}")
except requests.RequestException:
    pass