class Category:
    def __init__(self, category):
        self.ledger = []
        self.title = category
        self.total = 0
        self.total_spending = 0

    def __str__(self):
        category_str = ''
        category_str += "{:*^30}".format(self.title)

        for item in self.ledger:
            amount_str = "{:.2f}".format(item['amount'])
            item_str = '\n' + "{:<23}".format(item['description'][:23]) + "{:>7}".format(amount_str)
            category_str += item_str
        category_str += '\n' + f'Total: {self.total}'

        return category_str

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount

    def withdraw(self, amount, description=''):
        if self.total >= amount:
            self.ledger.append({'amount': (amount * -1), 'description': description})
            self.total -= amount
            self.total_spending += amount
            self.total_spending = round(self.total_spending, 2)
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, target):
        if self.total >= amount:
            self.withdraw(amount, f'Transfer to {target.title}')
            target.deposit(amount, f'Transfer from {self.title}')
            return True
        else: 
            return False

    def check_funds(self, amount):
        if amount <= self.total:
            return True
        else:
            return False
    



def create_spend_chart(categories):
    length = 5 + (len(categories) * 3)
    height = 11
    chart_str = 'Percentage spent by category\n'
    

    #Find percentages
    total = 0
    percents = {}

    for category in categories:
        total += category.total_spending
        total = round(total, 2)
    
    for category in categories:
        percent = (category.total_spending / total * 100)
        percent = (percent // 10) * 10
        percents[category.title] = percent

    #Make base chart
    rows = {}
    row_percent = 100
    for row_num in range(11):
        if row_percent == 100:
            rows[row_num] = ['', row_percent, '| ']
            for i in range(length - 5):
                rows[row_num].append(' ')
            row_percent -= 10
            row_num += 1
        elif row_percent > 0:
            rows[row_num] = [' ', row_percent, '| ']
            for i in range(length - 5):
                rows[row_num].append(' ')
            row_percent -= 10
        else:
            rows[row_num] = ['  ', row_percent, '| ']
            for i in range(length - 5):
                rows[row_num].append(' ')

    #Add percentages to chart
    percent_index = 3
    for percent in percents.values():
        for row in rows.values(): 
            if percent >= row[1]:
                row[percent_index] = 'o'
        percent_index += 3

    #Make dash line
    dash_line = '    -'
    for i in range(length - 5):
        dash_line += '-'

    #Make label rows
    longest_key = 0
    label_rows = {}
    for key in percents.keys():
        if len(key) > longest_key:
            longest_key = len(key)
    for row_num in range(longest_key):
        label_rows[row_num] = ['     ']
        for i in range(length - 5):
            label_rows[row_num].append(' ')
    
    #Add labels to label rows
    label_index = 1
    for key in percents.keys():
        for i in range(len(key)):
            label_rows[i][label_index] = key[i]
        label_index += 3

    #Turn dictionaries into strings
    values_str = ''
    label_str = ''
    for value in rows.values():
        for char in value:
            values_str += str(char)
        values_str += '\n'
    values_str = values_str[:-1]

    for value in label_rows.values():
        label_str += '\n'
        for char in value:
            label_str += str(char)

    #Update chart_str
    chart_str += values_str + '\n' + dash_line + label_str
    
    #Return chart_str

    return chart_str



"""
Example usage:

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

"""


