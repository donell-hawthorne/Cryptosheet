from coinmarketcap import Market #import coinmarketcap API to get Market ticker
coinmarketcap = Market()


import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Cryptosheet").sheet1


def coin_ticker():
#loop to pull ticker information as needed
    my_coins = ("Bitcoin", "Zcash", "Clams", "Dogecoin", "Ethereum"); #define tuple of coins to get market data for
    for coins in my_coins:
        coin_data = coinmarketcap.ticker(coins) #retrieve ticker information for coin
        stripped_coin_data = coin_data[0] #put ticker info in usable format
        for coins in my_coins:
            if coins.lower() and stripped_coin_data['id'] == "bitcoin": #identify coin and dictionary to update
                sheet.update_cell(4, 8, stripped_coin_data['price_usd'])  #update cell on Google spreadsheet
            elif coins.lower() and stripped_coin_data['id'] == "zcash":
                sheet.update_cell(5, 8, stripped_coin_data['price_usd'])
                sheet.update_cell(5, 7, stripped_coin_data['price_btc'])
            elif coins.lower() and stripped_coin_data['id'] == "clams":
                sheet.update_cell(6, 8, stripped_coin_data['price_usd'])
                sheet.update_cell(6, 7, stripped_coin_data['price_btc'])
            elif coins.lower() and stripped_coin_data['id'] == "dogecoin":
                sheet.update_cell(7, 8, stripped_coin_data['price_usd'])
                sheet.update_cell(7, 7, stripped_coin_data['price_btc'])
            elif coins.lower() and stripped_coin_data['id'] == "ethereum":
                sheet.update_cell(27, 2, stripped_coin_data['price_usd'])
            else:
                print("No Update")

coin_ticker()
