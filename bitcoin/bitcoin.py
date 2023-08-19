import requests
import sys



if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

else:
    sys.exit("Missing command-line argument")
try:

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = bitcoin * value
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit
