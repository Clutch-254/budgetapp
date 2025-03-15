class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]
            items += f"{description:<23}{amount:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total withdrawals for each category
    spent = []
    names = []
    
    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])
        spent.append(category_spent)
        names.append(category.name)
    
    # Calculate percentages
    total_spent = sum(spent)
    percentages = [int((amount / total_spent) * 100) // 10 * 10 for amount in spent]
    
    # Create chart header
    chart = "Percentage spent by category\n"
    
    # Add percentage bars
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    # Add horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Add category names vertically
    max_name_length = max(len(name) for name in names)
    for i in range(max_name_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"
    
    return chart


# Test Cases
def run_tests():
    print("Running test cases...")
    
    # Test 1: The deposit method should create a specific object in the ledger instance variable
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    print("Test 1:", food.ledger[0]["amount"] == 1000 and food.ledger[0]["description"] == "initial deposit")
    
    # Test 2: Calling the deposit method with no description should create a blank description
    entertainment = Category("Entertainment")
    entertainment.deposit(1000)
    print("Test 2:", entertainment.ledger[0]["description"] == "")
    
    # Test 3: The withdraw method should create a specific object in the ledger instance variable
    food.withdraw(10.15, "groceries")
    print("Test 3:", food.ledger[1]["amount"] == -10.15 and food.ledger[1]["description"] == "groceries")
    
    # Test 4: Calling the withdraw method with no description should create a blank description
    food.withdraw(100)
    print("Test 4:", food.ledger[2]["description"] == "")
    
    # Test 5: The withdraw method should return True if the withdrawal took place
    print("Test 5:", food.withdraw(20))
    
    # Test 6: Calling food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') should return a balance of 854.33
    food_balance = Category("Food Balance")
    food_balance.deposit(900, "deposit")
    food_balance.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    print("Test 6:", abs(food_balance.get_balance() - 854.33) < 0.01)
    
    # Test 7: Calling the transfer method on a category object should create a specific ledger item in that category object
    food_transfer = Category("Food Transfer")
    clothing = Category("Clothing")
    food_transfer.deposit(1000, "initial deposit")
    food_transfer.transfer(50, clothing)
    print("Test 7:", food_transfer.ledger[1]["amount"] == -50 and food_transfer.ledger[1]["description"] == "Transfer to Clothing")
    
    # Test 8: The transfer method should return True if the transfer took place
    food_transfer_2 = Category("Food Transfer 2")
    food_transfer_2.deposit(200, "deposit")
    print("Test 8:", food_transfer_2.transfer(100, clothing))
    
    # Test 9: Calling transfer on a category object should reduce the balance in the category object
    food_transfer_3 = Category("Food Transfer 3")
    food_transfer_3.deposit(100, "deposit")
    food_transfer_3.transfer(50, clothing)
    print("Test 9:", food_transfer_3.get_balance() == 50)
    
    # Test 10: The transfer method should increase the balance of the category object passed as its argument
    food_transfer_4 = Category("Food Transfer 4")
    clothing_transfer = Category("Clothing Transfer")
    food_transfer_4.deposit(100, "deposit")
    initial_clothing_balance = clothing_transfer.get_balance()
    food_transfer_4.transfer(50, clothing_transfer)
    print("Test 10:", clothing_transfer.get_balance() - initial_clothing_balance == 50)
    
    # Test 11: The transfer method should create a specific ledger item in the category object passed as its argument
    food_transfer_5 = Category("Food Transfer 5")
    clothing_transfer_2 = Category("Clothing Transfer 2")
    food_transfer_5.deposit(100, "deposit")
    food_transfer_5.transfer(50, clothing_transfer_2)
    print("Test 11:", clothing_transfer_2.ledger[0]["amount"] == 50 and clothing_transfer_2.ledger[0]["description"] == "Transfer from Food Transfer 5")
    
    # Test 12: The check_funds method should return False if the amount passed to the method is greater than the category balance
    check_funds = Category("Check Funds")
    check_funds.deposit(100, "deposit")
    print("Test 12:", not check_funds.check_funds(200))
    
    # Test 13: The check_funds method should return True if the amount passed to the method is not greater than the category balance
    print("Test 13:", check_funds.check_funds(50))
    
    # Test 14: The withdraw method should return False if the withdrawal didn't take place
    withdraw_test = Category("Withdraw Test")
    withdraw_test.deposit(100, "deposit")
    print("Test 14:", not withdraw_test.withdraw(200))
    
    # Test 15: The transfer method should return False if the transfer didn't take place
    transfer_test = Category("Transfer Test")
    transfer_target = Category("Transfer Target")
    transfer_test.deposit(100, "deposit")
    print("Test 15:", not transfer_test.transfer(200, transfer_target))
    
    # Test 16: Printing a Category instance should give a different string representation of the object
    print_test = Category("Print Test")
    print_test.deposit(100, "deposit")
    print_test.withdraw(50, "withdraw")
    print("\nTest 16 (Category print representation):")
    print(print_test)
    
    # Tests 17-24: create_spend_chart tests
    food_chart = Category("Food")
    food_chart.deposit(900, "deposit")
    food_chart.withdraw(105.55)
    entertainment_chart = Category("Entertainment")
    entertainment_chart.deposit(900, "deposit")
    entertainment_chart.withdraw(33.40)
    business_chart = Category("Business")
    business_chart.deposit(900, "deposit")
    business_chart.withdraw(10.99)
    
    print("\nTest 17-24 (create_spend_chart output):")
    chart = create_spend_chart([food_chart, entertainment_chart, business_chart])
    print(chart)


if __name__ == "__main__":
    run_tests()
    
    
    