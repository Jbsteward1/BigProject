

greeting =("Hello %s, welcome to Millys Phillys. Here is todays menu %s")
print(greeting)

menu =("Super Philly cheesteak $ 13.50\nChicago Philly cheesesteak $12.50\nSuperCombo Philly with wings $19.00\nCheesesticks and philly $17.00\nUltimate Philly combo $21.50")

Wallet = 50

name_of_customer = input("Can i have a name for your order? ")
lenght_of_order = input("Thank you, what can i get for you today? ")
print("Anything else?")
print("Yes = 1 \n No =2")


question = input("Will that be all for you today")
Yes = 1
No = 2
if question == 1:
    print("yes id like a Chicago Philly cheesesteak")
elif question == 2:
    print("no thank you")
else:
    print("that will be all")

class Moes:
    def __init__(self, customer, menu = [], order = {}, total_price = 0, fufilled = False):
        self.customer = customer
        self.menu = menu
        self.order = order
    def add_customer_name(self, name):
        self.customer["name"] = name
    def add_menu(self, menu):
        self.menu.append("food_option")
    def add_order(self, order):
        self.add_order = order
    def get_total_price(self):
        index = 0
        total = 0
        while index < len(self.menu):
            total += self.menu[index]["price"]
            index += 1
        print(total)










