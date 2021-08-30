Wallet = 50
greeting =("Hello %s, welcome to Millys Phillys. Here is todays menu %s")
print(greeting)

menu =("Super Philly cheesteak $ 13.50\nChicago Philly cheesesteak $12.50\nSuperCombo Philly with wings $19.00\nCheesesticks and philly $17.00\nUltimate Philly combo $21.50")


name_of_customer = input("Can i have a name for your order? ")
lenght_of_order = input("Thank you, what can i get for you today? ")
print("Anything else?")






class Moes:
    def __init__(self, customer, menu = ["Ultimate Philly combo $21.50,"], order = {}, total_price = 0, fufilled = False):
        self.customer = customer
        self.menu = menu
        self.order = order
    def add_customer_name(self, name):
        self.customer["name"] = name
    def add_menu(self, menu):
        self.menu.append("food_option")