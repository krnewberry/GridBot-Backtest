import pandas as pd
import glob

list_of_files = glob.glob('DATAFILES/*.csv')
for csv in list_of_files:
    df = pd.read_csv(csv, usecols=['high','low'])
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
print("Total Revenue:",(round(sum(item['money_split'] for item in user_config),2)))
print("Total Shares:",(round(sum(item['share_split'] for item in user_config),2)),"\n")