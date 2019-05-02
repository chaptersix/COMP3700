class AccountController():
    def __init__(self):
        self.user_data = AccountEntity.load_user_data()

    def check_password(self, current_user_in, password_in):
        return(self.user_data[current_user_in] == password_in)

class AccountEntity():


    def load_user_data():
        user_data = {}
        with open("database/user_data.dat", "r") as user_file:
            for line in user_file.readlines():
                line = line.split()
                username_in = line[0]
                password_in = line[1]
                user_data[username_in] = password_in
            return user_data

    def write_user_data():
        with open("database/user_data.dat", "r") as user_file:
            for line in user_file.readlines():
                line = line.split()
                username_in = line[0]
                password_in = line[1]
                self.user_data[username_in] = password_in
        print("Bank Controller User Data: {}".format(self.user_data))
        user_file.close()