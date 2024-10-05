from P_virtual_account.virtual_account import *


MTA = Virtual_Account()
MTA.load_assets()
MTA.verbose = True

def main():
    print(MTA.assets)
    

if __name__ == "__main__":
    main()

