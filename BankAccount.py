class BankAccountEntity():
    def __init__(self):
        pass

    def load_account_data(self):
        account_data = []
        with open("database/bank_username_account.dat", "r") as bank_file:
            for line in bank_file.readlines():
                line = line.split()
                bank = line[0]
                user = line[1]
                account = line[2]
                acct_type = line[3]
                balance = line[4]
                account_data.append([bank, user, account, acct_type, balance])
        print("Load Bank Accounts:\n{}".format(account_data))
        return account_data

    def write_active_accounts(self, account_data_in):
        outStr = ""
        for line in account_data_in:
            outStr += "{} {} {} {} {}\n".format(line[0], line[1], line[2], line[3], line[4])
            print(line)
        with open("database/bank_username_account.dat", "w") as bank_file:
            bank_file.write(outStr)

        print("Write Bank Accounts:\n{}".format(outStr))


class BankAccountController:
    def __init__(self):
        self.account_data = BankAccountEntity().load_account_data()
        self.user_data = {}

    def is_account_active(self, account_number):
            for  account in self.account_data:
                if account[2] == account_number:
                    return True
            return False

    def add_account(self, bank_in, account_number_in, current_user_in, account_type_in, balance_in):
        if not bank_in or not account_number_in or " " in bank_in or " " in account_number_in:
            return False
        self.account_data = BankAccountEntity().load_account_data()
        bank_in = bank_in.lower()
        if  not self.is_account_active(account_number_in):
            self.account_data.append([bank_in, current_user_in, account_number_in, account_type_in, balance_in])
            BankAccountEntity().write_active_accounts(self.account_data)
            return True
        return False

    def remove_account(self, account_number_in, current_user_in):
        self.account_data = BankAccountEntity().load_account_data()
        for index, account in  enumerate(self.account_data):
            if account[1] == current_user_in and account[2] == account_number_in:
                del self.account_data[index]
                BankAccountEntity().write_active_accounts(self.account_data)
                return True
        return False


    def load_user_data(self):
        with open("database/user_data.dat", "r") as user_file:
            for line in user_file.readlines():
                line = line.split()
                username_in = line[0]
                password_in = line[1]
                self.user_data[username_in] = password_in
        print("Bank Controller User Data: {}".format(self.user_data))
        user_file.close()


