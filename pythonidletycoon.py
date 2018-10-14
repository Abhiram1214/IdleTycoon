
class Store():
    Money = 25.00
    Day = 1
    def __init__(self):
        self.StoreName = "Lemon Stand"
        self.StoreCount = 0
        self.StoreProfit = 1.50
        self.StoreCost = 3

    @classmethod
    def DisplayGameInfo(cls):
        print("---------------------------------------------")
        print("Day #"+str(cls.Day))
        print("Money $" + str(cls.Money))
        print("---------------------------------------------")


    def StoreInfo(self):
        print("---------------------------------------------")
        print("Name of our store is " + str(self.StoreName))
        print("Money = %s" % (Store.Money))
        print("Store Count: %d" %(self.StoreCount))
        print("---------------------------------------------")



    def BuyStore(self):
        if self.StoreCost <= Store.Money:
            self.StoreCount +=1
            print(self.StoreCount)
            Store.Money -= self.StoreCost
        else:
            print("you dont have enough money")



    def NextDay(self):
        Store.Day += 1
        DailyProfit = self.StoreProfit + self.StoreCount
        Store.Money += DailyProfit

currentstore = Store()


#main game loop
while True:
    Store.DisplayGameInfo()

    print("Available options are: (N)Next Day, (B)Buy Store, (Q)Quit")
    result = input("please enter your selection: ")

    if result == 'B' or result == 'b':
        print("Current status")
        currentstore.BuyStore()
    elif result == 'N'or 'n':
        currentstore.NextDay()
        #DisplayStoreInfo()
    elif result == 'q' or 'Q':
        break
    else:
        print("Wrong input")
    currentstore.StoreInfo()

print("----ended---")
