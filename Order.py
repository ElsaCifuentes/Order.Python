print("                 ******************************************************")
print("                                 | GUATEMALAN FOOD TAKEAWAY|")
print("                                 |      ORDERING SYSTEM    |")
print("                 ******************************************************")
print()
print("                               WELCOME TO MY APPLICATION  ") 
print()

class Order:
    def __init__(self):
        self.__itemdict = dict()
        
    def AddItem(self,Item):
        self.__Item = Item
        
    def AddMenuPrice(self,Price):
        self.__Price = Price
        
    def AddItem(self,Item,Price):
        self.__Item = Item
        self.__Price = Price
        self.__itemdict[self.__Item] = self.__Price
        
    def CalcOrder(self):
        self.__Total = 0.0
        for self.__Item,self.__Price in self.__itemdict.items():
            print(self.__Item + "\t\t\t" + str(self.__Price))
            self.__Total = self.__Total + self.__Price
        print("Total \t\t\t\t", str(self.__Total))

def FoodOptions():
    print("                 What kind of meal would you like to have today?  ")
    print("\t\t\t1. Chicken pepián\t\t\t$10")
    print("\t\t\t2. Pupusas(3)\t\t\t\t$9")
    print("\t\t\t3. Chicken Empanadas(3)\t\t\t$9")
    print("\t\t\t4. Hilachas\t\t\t\t$8")
    print("\t\t\t5. Noodle tostadas\t\t\t$7")
    print("\t\t\t6. Traditional breakfast\t\t$8")
    print("\t\t\t7. Rellenitos(4)\t\t\t$8")

def DrinkOptions():
    print("                 What kind of drink would you like to have today?  ")
    print("\t\t\t1. Coffee\t\t\t$2")
    print("\t\t\t2. Chocolate\t\t\t$3")
    print("\t\t\t3. Coca Cola\t\t\t$3")
    print("\t\t\t4. Pepsi\t\t\t$3")
    print("\t\t\t5. Licuado\t\t\t$5")
    print("\t\t\t6. Tamarindo\t\t\t$2")
    print("\t\t\t7. Atol de elote\t\t$2")

def main():
    MyOrder = Order()
    FoodOptions()
    while True:
        try:
            answer = int(input("Enter your option: "))
            print()
            if answer==1:
                Item="Chicken pepian"
                Price=10.0
                break
            elif answer==2:
                Item="Pupusas"
                Price = 9.0
                break
            elif answer==3:
                Item="Chicken Empanadas(3)"
                Price = 9.0
                break
            elif answer==4:
                Item="Hilachas"
                Price = 8.0
                break
            elif answer==5:
                Item="Noodle tostadas"
                Price = 7.0
                break
            elif answer==6:
                Item="Traditional Breakfast"
                Price = 8.0
                break
            elif answer == 7:
                Item="Rellenitos"
                Price = 8.0
                break
            else:
                print("Invalid choice. Enter 1-7")
            
        except ValueError:
            print("Invalid choice. Enter 1-7")
    print("Adding", Item, "to the cart for $", Price)

    MyOrder.AddItem(Item,Price)

    DrinkOptions()
    while True:
        try:
            answer = int(input("Enter your option: "))
            print()
            if answer==1:
                Item="Coffee"
                Price= 2.0
                break
            elif answer==2:
                Item="Chocolate"
                Price=3.0
                break
            elif answer==3:
                Item="Coca Cola"
                Price=3.0
                break
            elif answer==4:
                Item="Pepsi"
                Price=3.0
                break
            elif answer==5:
                Item="Licuado"
                Price=5.0
                break
            elif answer==6:
                Item="Tamarindo"
                Price=2.0
                break
            elif answer == 7:
                Item="Atol de elote"
                Price=2.0
                break
            else:
                print("Invalid choice. Enter 1-7")
            
        except ValueError:
            print("Invalid choice. Enter 1-7")
    print("Adding", Item, "to the cart")

    MyOrder.AddItem(Item,Price)

    MyOrder.CalcOrder()

if __name__=="__main__":
    main()
