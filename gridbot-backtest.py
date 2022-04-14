import pandas as pd
import glob

list_of_files = glob.glob('DATAFILES/*.csv')

for csv in list_of_files:
    df = pd.read_csv(csv, usecols=['high','low'])

    # User Config
    money = 2000
    shares = 0
    fee = .001
    user_config = [
        {
        'buy_price': 1,
        'sell_price': 2,
        'money_split': 0,
        'money_split_percent': 0.5,
        'share_split': 0,
        'share_split_percent': 1,
        },{
        'buy_price': 2,
        'sell_price': 4,
        'money_split': 0,
        'money_split_percent': 0.5,
        'share_split': 0,
        'share_split_percent': 1,        
        },]
     
    # Money & Share Split Calculation
    for i in range(len(user_config)):
        user_config[i]['money_split'] = money * user_config[i]['money_split_percent']
        user_config[i]['share_split'] = shares * user_config[i]['share_split_percent']
    
    for index, row in df.iterrows():
        for i in range(len(user_config)):
            if user_config[i]['share_split'] == 0:
                if row["low"] >= user_config[i]['buy_price']:
                    user_config[i]['share_split'] = (user_config[i]['money_split'] - (user_config[i]['money_split'] * fee)) / user_config[i]['buy_price'] 
                    print(f"purchased {user_config[i]['share_split']} shares at ${user_config[i]['buy_price']} with ${user_config[i]['money_split']} dollars")
                    user_config[i]['money_split'] = 0
            else:
                if row["high"] >= user_config[i]['sell_price']:
                    user_config[i]['money_split'] = user_config[i]['sell_price'] * user_config[i]['share_split']
                    user_config[i]['money_split'] = (user_config[i]['money_split'] - (user_config[i]['money_split'] * fee))
                    print(f"sold {user_config[i]['share_split']} shares at {user_config[i]['sell_price']} for ${user_config[i]['money_split']} dollars")
                    user_config[i]['share_split'] = 0  


print("\nSUCCESS...")
print(f"Total Money: {money}")
print(f"Number of Splits: {len(user_config)}")
print(f"Money Split: {user_config[0]['money_split']}")
#print(f"Buying at: {user_config['buy_price']}")
#print(f"Selling at: {user_config['sell_price']}")
#print(f"Maker/Taker Fee:", fee * 100)
#print()
#print (f"Shares Owned: {sum(share_split)}")
#print(f"Revenue: {sum(money_split)}\n")