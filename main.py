class Category:
    def __init__(self, category):
        self.category=category
        self.ledger=[]
        self.balance=0.0
        self.wd=0.0
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})  
        self.balance += amount  

    def withdraw(self, amount, description=''):
        if amount > self.balance:
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        self.wd += amount
        self.balance -= amount
        return True
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.category}'):
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False 
    
    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else:  

            return False
    
    def __repr__(self):
        tmp='*'*(15-len(self.category)//2)+f'{self.category}'+'*'*(30-15-len(self.category)//2)+'\n'
        for tr in self.ledger:
            amount=(tr['amount'])
            tmp += f"{tr['description'][:23]:<23}{amount:7.2f}\n"
        tmp += f"Total: {self.balance:.2f}"
        
        return tmp

def create_spend_chart(categories):
    #calculate sum to calculate the percentage
    total=sum(cat.wd for cat in categories)
    #calculate the percentage
    percentage=[round(cat.wd/total*100) for cat in categories]

    tmp='Percentage spent by category\n'
    for i in range(100,-1,-10):
        tmp += f"{i:3}|"
        for per in percentage:
            if per >= i:
                tmp += " o "
            else:
                tmp += "   "
        tmp += ' \n'
    tmp += '    '+'-'*(len(percentage)*3+1)+'\n'

    maxi=max(len(cat.category) for cat in categories)
    
    for i in range(maxi):
        tmp += '    '
        for cat in categories:
            try: 
                tmp += f" {cat.category[i]} "
            except:
                tmp += '   '
        if i < maxi-1:
            tmp += ' \n'
        else :
            tmp += ' '
    print(tmp)
    return tmp
    