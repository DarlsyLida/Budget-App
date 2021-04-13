class Budget:
    """
        This is Budget class that has methods like withdraw, deposit and calculate balance.
        It also transfer balance in the given categories
    """
    def __init__(self, category: str, amount):
        self.category= category
        self.amount= amount

    def deposit(self, amnt):
        print("You have deposited {} in {} category".format(amnt, self.category))
        self.amount = self.amount + amnt
        
        

    def withdraw(self, amnt):
        if amnt <= self.amount:
            print("You have withdrawn {} in {} category".format(amnt, self.category))
            self.amount = self.amount - amnt
        else:
            print("Sorry, Current balance in {} category is less than {}".format(self.category, amnt))
            

    def Calculate_bal(self):
        print("The current balance  is {}.\n \n \n".format( self.amount))

    def Transfer_Bal(self):
        return self.amount
       
        
        
        
        

food= Budget('Food', 0)
food.deposit(500)
food.withdraw(100)
food.Calculate_bal()

clothing= Budget('Clothing', food.Transfer_Bal())
clothing.deposit(5000)
clothing.withdraw(10000)
clothing.Calculate_bal()

enter = Budget('Entertainment', clothing.Transfer_Bal())
enter.deposit(1000)
enter.withdraw(500)
enter.Calculate_bal()