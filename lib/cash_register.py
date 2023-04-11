#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount = 0) -> None:
        self.discount = discount
        self.total = 0
        self.items = list()
        self.last_transaction = list()
        pass
    
    def void_last_transaction(self):
        self.total -= self.last_transaction[1]*self.last_transaction[2]
        self.items.remove(self.last_transaction[0])
        
    def add_item(self, title, price, quant = 1):
        self.last_transaction = [title, price, quant]
        self.total += (price * quant)
        while quant > 0:
          self.items.append(title)
          quant -= 1 
    
    def apply_discount(self):
        if(self.discount == 0):
            print('There is no discount to apply.')
            return
        self.total -=  self.total * self.discount / 100
        print(f'After the discount, the total comes to $%.0f.' % (self.total))
