import sys

def main():
    while True:
        print("Hello! Welcome to TigerWallet")
        print("\t1) Login")
        print("\t2) Create Account")
        print("\t3) Quit")
        choice = int(input())
        if choice == 1:
            #login()
            pass
        elif choice == 2:
            #create_account()
            pass
        elif choice == 3:
            sys.exit(0)
    


if __name__ == "__main__":
    main()