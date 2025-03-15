# Budget App

A Python application for tracking personal budget categories and visualizing spending patterns.

## Description

The Budget App helps users manage their finances by tracking spending and deposits across multiple budget categories. It provides a clear way to monitor balances and see where money is being spent through visual representation.

## Features

- **Multiple Budget Categories**: Create separate budget categories (e.g., Food, Clothing, Entertainment)
- **Transaction Tracking**: Record deposits and withdrawals with descriptions
- **Balance Management**: Check current balances for each category
- **Fund Transfers**: Move money between different budget categories
- **Spending Visualization**: Generate bar charts showing percentage spent by category

## Usage

### Creating Categories

```python
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")
```

### Managing Transactions

```python
# Make deposits
food.deposit(1000, "initial deposit")
clothing.deposit(500, "monthly budget")

# Make withdrawals
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant")
clothing.withdraw(25.55, "t-shirt")

# Check balances
food_balance = food.get_balance()  # Returns current balance
```

### Transferring Funds

```python
# Transfer money from one category to another
food.transfer(50, clothing)  # Transfers $50 from food to clothing
```

### Viewing Category Details

```python
print(food)  # Displays formatted category information
```

Output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant              -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

### Visualizing Spending

```python
# Generate spending chart for multiple categories
chart = create_spend_chart([food, clothing, entertainment])
print(chart)
```

Output:
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  E  
     o  l  n  
     o  o  t  
     d  t  e  
        h  r  
        i  t  
        n  a  
        g  i  
           n  
           m  
           e  
           n  
           t  
```

## Class Methods

### Category Class

- `__init__(name)`: Creates a new budget category
- `deposit(amount, description="")`: Adds funds with optional description
- `withdraw(amount, description="")`: Removes funds if available
- `get_balance()`: Returns current category balance
- `transfer(amount, destination)`: Moves funds to another category
- `check_funds(amount)`: Verifies if funds are available
- `__str__()`: Returns formatted string representation

### Functions

- `create_spend_chart(categories)`: Generates a bar chart showing percentage spent in each category

## Technical Details

- The ledger for each category is stored as a list of dictionaries
- Each transaction is recorded with an amount and description
- Withdrawals are stored as negative values
- The spending chart only considers withdrawals (not deposits) when calculating percentages
- Chart bars are rounded down to the nearest 10%
