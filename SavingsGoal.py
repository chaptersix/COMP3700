class SavingsGoals():
    def __init__(self, name, goal_amt, exp_date):
        self.name = name
        self.goal_amount = goal_amt
        self.exp_date = exp_date

    # in order for this to be persistent across sessions and users, 
    # goals should be written to a file associated with a username
    savings_goals_list = []