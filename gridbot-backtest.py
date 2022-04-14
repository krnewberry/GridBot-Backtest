import pandas as pd
import glob

list_of_files = glob.glob('DATAFILES/*.csv')

for csv in list_of_files:
    df = pd.read_csv(csv, usecols=['high','low'])

    # Starting Balances & Fee & Splits
    money = 2000
    shares = 0
    fee = .001
    split_range = 2

    # First Buy
    first_buy = 1
    first_buy_money_percent = .5
    # First Sell
    first_sell = 2
    first_sell_share_percent = 1
    # Second Buy
    second_buy = 2
    second_buy_money_percent = .5
    # Second Sell
    second_sell = 4
    second_sell_share_percent = 1

    # LISTS
    buy_price = [first_buy, second_buy]
    sell_price = [first_sell, second_sell]
    money_split = [0,0]
    money_split_percent = [first_buy_money_percent,second_buy_money_percent]
    share_split = [0,0]
    share_split_percent = [first_sell_share_percent, second_sell_share_percent]

    # Money & Share Split Calculation
    for i in range(split_range):
        money_split[i] = money * money_split_percent[i]
        share_split[i] = shares * share_split_percent[i]

    print("GRID-BOT BACKTEST")
    print(f"Money Split: {money_split}\n")
    
    for index, row in df.iterrows():

        if share_split[0] == 0:
            if row["low"] >= buy_price[0]:
                share_split[0] = (money_split[0] - (money_split[0] * fee)) / buy_price[0]                  
                print(f"purchased {share_split[0]} shares at ${buy_price[0]} with ${money_split[0]} dollars")
                money_split[0] = 0                          

        if share_split[1] == 0:
            if row["low"] >= buy_price[1]:
                share_split[1] = (money_split[1] - (money_split[1] * fee)) / buy_price[1]
                print(f"purchased {share_split[1]} shares at ${buy_price[1]} with ${money_split[1]} dollars")
                money_split[1] = 0

        else:
            if row["high"] >= sell_price[0]:
                money_split[0] = sell_price[0] * share_split[0]
                money_split[0] = (money_split[0] - (money_split[0] * fee))
                print(f"sold {share_split[0]} shares at {sell_price[0]} for ${money_split[0]} dollars")
                share_split[0] = 0     

            if row["high"] >= sell_price[1]:
                money_split[1] = sell_price[1] * share_split[1]
                money_split[1] = (money_split[1] - (money_split[1] * fee))
                print(f"sold {share_split[1]} shares at {sell_price[1]} for ${money_split[1]} dollars")
                share_split[1]= 0    

total_shares = share_split[0] + share_split[1]
total_money = money_split[0] + money_split[1]

print (f"Shares Owned: {total_shares}")
print(f"Revenue: {total_money}\n")