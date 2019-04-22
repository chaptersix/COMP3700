import User

class BankAccount():
    def __init__(self, routing_number_in, account_number_in):
        self.routing_number = routing_number_in
        self.account_number = account_number_in
        self.linked_user = None
    
    def get_routing_number(self):
        return self.routing_number
    
    def get_account_number(self):
        return self.account_number

    def set_user(self, user):
        self.linked_user = user

    def set_routing_number(self, routing_number_in):
        self.routing_number = routing_number_in

    def set_account_number(self, account_number_in):
        self.account_number = account_number_in

