class Budget:
    '''
    A class for creating budgets.
    
    deposit() : Allowers user to allot funds for a particular category\n 
    checkBalance(): Computes a particular category balance\n
    withdraw(): Allows user to withdraw from particular category\n
    transfer():  Allows user to transfer from one category to the other\n
    getData(): Returns all data inputed for a particular category\n
    
    '''
    
    def __init__(self, category):
        self.category = category
        self.categoryData = [
            
        ]
    
    def deposit (self, amount, note=""):
        '''
        Allows user to deposit funds into a particular category
        '''
        self.categoryData.append({"Amount": amount, "Description" : note})
    
    def withdraw (self, amount, note=""):
        '''
        Allows user to withdraw from particular category
        '''
        if self.checkBalance() >= amount:
            self.categoryData.append({"Amount": -amount, "Description": note})
            return True
        return False
    
    def checkBalance (self):
        '''
        Computes a particular category balance
        '''
        total = 0 
        for item in self.categoryData:
            total += item["Amount"]
        return total
    
    def transfer (self, amount, category):
        '''
        Allows user to transfer from one category to the other
        '''
        if self.checkBalance() >= amount:
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True
        return False
        
    def getData(self): 
        '''
        Returns all data inputed for a particular category
        '''
        return self.categoryData

# CODE TEST #

#Instantiating objects 
food = Budget('Food')
car = Budget('Car')
house = Budget('New House')

#Testing deposit method
food.deposit(10000, 'To buy foodstuffs for a month')
car.deposit(200000, 'To buy my dream car')
house.deposit(1000000, 'To buy my retirement house')

#Testing the withdraw method
print(food.withdraw(4500, "For indomie"))
print(car.withdraw(50000, "First deposit at car shop"))
print(house.withdraw(500000, "First deposit at agent"))

#Testing the transfer method
print(food.transfer(2000, car))
print(house.transfer(30000, food))

#Testing the balance computation method
print(food.checkBalance())
print(car.checkBalance())
print(house.checkBalance())

#Testing the get data for category method
print(food.getData())
print(house.getData())
print(car.getData())
