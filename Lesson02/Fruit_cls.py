class Fruits:
    def __init__(self):
        # list of fruits
        self.fruits = [('Orangen', '2.20'), 
                       ('Papaya', '3.50'),
                       ('Kiwi', '3.50'),
                       ('Bananen', '1.90'),
                       ('Zitronen', '1.70'),
                       ('Mango', '3.90')]        

    def __str__(self):
        return f'{self.fruits}'
    
    def getFruits(self):
        # get list of fruits
        fruit_list = ', '.join([name for name, price in self.fruits])
        return fruit_list

    def getPrice(self, fruit):
        # get price of the fruit
        fruit_price = next((price for name, price in self.fruits if name == fruit), None)
        if fruit_price is not None:
            return f'{fruit} kosten pro Kilo € {fruit_price}'
        return (f'{fruit} haben wir heute nicht vorrätig')

# test example
# myfruits = Fruits()
# print(myfruits)
# print(myfruits.getPrice('Papaya'))
# print(myfruits.getFruits())