import json


class Test_Account:
    def __init__(self):
        self.balance = 1000
        self.assets = {
            "balance": self.balance,
            "stocks": {}
        }
    
    def load_assets(self):
        with open("P_test_account/test_account_data.json", "r") as save_file:
            self.assets = json.load(save_file)

    def save_assets(self):
        self.assets["balance"] = self.balance
        with open("P_test_account/test_account_data.json", "w") as save_file:
            save_file.write(json.dumps(self.assets))

    def buy(self, symbol, shares, price): # may break shares if multiple are bought
        self.balance = round(self.balance - price * shares, 2)
        self.assets["stocks"][symbol] = {
            "shares": shares
        }
        self.save_assets()
        print(f"{shares} shares of {symbol} bought at {price} (-{price * shares})")
    
    def sell(self, symbol, shares, price): # non-functional
        pass

    def get_asset_index(self, symbol):
        for i in self.assets:
            print(i)
        

class Test_Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = 50

