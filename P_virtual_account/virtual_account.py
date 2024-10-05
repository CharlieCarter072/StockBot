import json


class Virtual_Account:
    def __init__(self):
        self.balance = 1000
        self.assets = {
            "balance": self.balance,
            "stocks": {}
        }
        self.verbose = False
    
    def load_assets(self):
        with open("P_virtual_account/virtual_account_data.json", "r") as save_file:
            self.assets = json.load(save_file)

    def save_assets(self):
        self.assets["balance"] = self.balance
        with open("P_virtual_account/virtual_account_data.json", "w") as save_file:
            save_file.write(json.dumps(self.assets))

    def buy(self, symbol, shares, price):
        self.balance = round(self.balance - shares * price, 2)
        if symbol in self.assets["stocks"]:
            self.assets["stocks"][symbol]["shares"] += shares
        else:
            self.assets["stocks"][symbol] = {
                "shares": shares
            }
        self.save_assets()
        if self.verbose:
            print(f"{shares} shares of {symbol} bought at {price} (-{round(price * shares, 2)})")
    
    def sell(self, symbol, shares, price): # non-functional
        if symbol in self.assets["stocks"] and self.assets["stocks"][symbol]["shares"] >= shares:
            self.assets["stocks"][symbol]["shares"] -= shares
            self.balance = round(self.balance + shares * price, 2)
            if self.verbose:
                print(f"{shares} shares of {symbol} sold at {price} (+{round(price * shares, 2)})")
            self.save_assets()
        else:
            raise Exception("Cannot sell unowned shares of stock")
        

class Test_Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = 50

