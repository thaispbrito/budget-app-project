import math

class Category:
    """
    Represents a budget category for tracking deposits, withdrawals, and transfers.

    Attributes:
        category_type (str): The name of the budget category.
        ledger (list): A list of dictionaries recording deposits and withdrawals.

    Methods:
        deposit(amount, description=''): Adds a deposit to the ledger.
        withdraw(amount, description=''): Attempts to withdraw funds if sufficient balance exists.
        get_balance(): Returns the current balance of the category.
        transfer(amount, other_category): Transfers funds to another Category if sufficient balance exists.
        check_funds(amount): Checks if the requested amount is available in the balance.
    """
    
    # Initialize the category_type attribute with the passed-in category name
    def __init__(self, category_type):
        self.category_type = category_type

        # Initialize a list that can be accessed by all methods in this class
        self.ledger = []

    # Define the __str__ method to return a properly formatted output
    def __str__(self):
        output = []  # Create a list to store the output elements

        # Create a title line of 30 characters where the name of the category is centered 
        # in a line of '*' characters, and append it to the the output list
        output.append((f'{self.category_type}').center(30, '*'))
        
        total = 0
        # Iterate over self.ledger and append each item's description and amount to the output list
        for item in self.ledger:
            # Slice the first 23 characters, in case the description is too long
            # Right-align the amount with two decimal places and display a max of seven characters
            output.append(f"{item['description'][:23]:<23}{item['amount']:>7.2f}")
            total += item['amount']

        # Append the formatted total to the output list
        output.append(f'Total: {total:.2f}')

        # Join all elements of the output list with newline characters and return the result
        return '\n'.join(output)
        
    # Define the class methods

    # Adds a deposit to the ledger
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    # If sufficient funds, withdraws an amount from the ledger
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    # Returns the current balance by summing all amounts from the ledger
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    # Computes transfer between categories
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.category_type}')
            other_category.deposit(amount, f'Transfer from {self.category_type}')
            return True
        return False

    # Check funds using the get_balance method defined previously
    def check_funds(self, amount):  # This method is used by both the withdraw and transfer methods
        return amount <= self.get_balance()
       
def create_spend_chart(categories):
    
    """
    Generates a text-based bar chart representing the percentage of total withdrawals by category.

    Args:
        categories (list of Category): A list of Category objects to include in the chart.

    Returns:
        str: A formatted string that visually displays the percentage spent by category
        as a vertical bar chart. Category names are displayed vertically below the chart.

    The chart shows percentages in increments of 10% from 0% to 100%, with 'o' characters
    marking the spending levels for each category.
    """
    
    # Create a list to store the output lines for the chart
    output_lines = []

    # Add the chart title to the output_lines list
    output_lines.append('Percentage spent by category')

    # Compute the total amount spent per category and the grand total from all categories
    spent_by_category = [] # Create a list to store the total spent per cateogry
    grand_total = 0
    for category in categories:
        total_per_category = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_by_category.append({'category': category.category_type, 'spent': total_per_category})
        grand_total += total_per_category

    # Compute the percentage spent by category out of the withdrawals,
    # which is the amount spent for each category to the total spent for all of them
    for item in spent_by_category:
        percent = (item['spent'] / grand_total)*100

        # Round down the height of each bar to the nearest 10
        # Add the percentage of each category to the spent_by_category list
        item['percent'] = math.floor(percent/10)*10

    # Format the percentage spent by category
    # Set the labels 0 - 100 down the left side of the chart 
    for percentage in range(100, -1, -10):
        lines = f'{percentage:>3}| '  # Right-align the value, three characters wide
        line_spaces = []  # Create this list as a helper for adding some extra spaces

        # Make the 'bars' in the bar chart out of the 'o' character
        for item in spent_by_category:
            if item['percent'] >= percentage:  
                line_spaces.append('o')
            else:
                line_spaces.append(' ')

        lines += (' '*2).join(line_spaces) + (' '*2)   # Use the * operator to specify the number of spaces
        
        # Set the chart width for consistent horizontal alignment     
        chart_width = 5 + len(spent_by_category) * 3
        output_lines.append(lines.ljust(chart_width))  # Left-justify, padding it with spaces

    # Append the horizontal dashed line to the output_lines list
    # Each category column takes up three characters (one space + 'o' + another space)
    # +1 for extra '-' to make the horizontal line below the bars with two spaces past the final bar
    output_lines.append((' '*4) + '-' * (len(spent_by_category) * 3 + 1))
            
    # Get the longest category name length
    max_len = max(len(category['category']) for category in spent_by_category)

    # Set up the category names vertically below the dashed line
    for n in range(max_len):
        row = (' '*5)    # Initial spacing
        for category in spent_by_category:
            name = category['category']
            if n < len(name):
                row += name[n] + (' '*2)
            else:
                row += (' '*3)
        output_lines.append(row.ljust(chart_width))  # Append the formatted rows to the output_lines list  

    # Join all elements of the output_lines list with newline characters and return the chart
    return '\n'.join(output_lines)

### Sample Tests

# Create a 'Food' category and perform transactions
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

# Create a 'Clothing' category and perform transactions
clothing = Category('Clothing')
clothing.deposit(1000, 'deposit')
clothing.withdraw(30.75, 'pants')

# Transfer funds from Food to Clothing
food.transfer(50, clothing)

# Create an 'Auto' category and perform transactions
auto = Category('Auto')
auto.deposit(50, 'deposit')
auto.withdraw(15, 'repair')

# Print the ledger for the Food category
print(food)

# Generate and print the spending chart
chart = create_spend_chart([food, clothing, auto])
print(chart)














