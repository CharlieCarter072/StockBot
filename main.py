from P_test_account.test_account import *


MTA = Test_Account()

def main():
    MTA.buy("TSLA", 10, 2.66)
    print(MTA.assets)


if __name__ == "__main__":
    main()

