# Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.
# Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

# implement a program that:
# Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
# import requests

#try:
#     ...
#except requests.RequestException:
#    ...

# Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.

# Importing request and sys
import requests
import sys

# Checking that the command-line-arguments be 2
if len(sys.argv) == 2:
    # Using a try except to verify that user is giving a number
    try:
        val = float(sys.argv[1])
    except:
        print("Command-line argument is not a number ")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    # Getting the information of the webpage 
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # With .json we will convert what we get from request in a dictionary
    response = r.json()
    # Getting inside the data to retrieve the amount in USD that a bitcoin is
    bitcoin_to_USD = response['bpi']['USD']['rate']
    bitcoin_to_USD = bitcoin_to_USD.replace(",","")
    # Getting the amount converted and printing it
    amount = float(bitcoin_to_USD) * float(sys.argv[1])
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("Request Exception")
    sys.exit(1)