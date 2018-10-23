#Idle Tycoon Game


class Store():
    Money = 25.00
    Day = 1
    StoreList = []
    
    def __init__(self, storename, storeprofit, storecost):
        self.StoreName = storename
        self.StoreCount = 0
        self.StoreProfit = storeprofit
        self.StoreCost = storecost

    @classmethod
    def DisplayGameInfo(cls):
        print("---------------------------------------------")
        print("Day #"+str(cls.Day))
        print("Money $" + str(cls.Money))
        print("---------------------------------------------")
        print("Stores".ljust(25) + "Store Cost".ljust(15) + "Store Count")
        i =1 
        for store in cls.StoreList:
            store.StoreInfo(i)            
            i+=1
        print("---------------------------------------------")

    def StoreInfo(self, i):
        
        StoreCostStr = "${}".format(self.StoreCost).rjust(12)
        print(str(i) +")" + self.StoreName.ljust(20) + StoreCostStr.ljust(20) + str(self.StoreCount))
        
        
        

    def BuyStore(self):
        whichstore = input("which store do you want to buy")
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

Store.StoreList.append(Store("Lemonade Stand", 1.50, 3))
Store.StoreList.append(Store("Record Store", 5, 15))
Store.StoreList.append(Store("Icecream Store", 10, 9))


#main game loop
while True:
    Store.DisplayGameInfo()
    
    print("Available options are: (N)Next Day, (B)Buy Store, (Q)Quit")
    result = input("please enter your selection: ")

    if result == 'B' or result == 'b':
        print("Current status")
        Store.StoreList[0].BuyStore()
    elif result == 'N'or 'n':
        Store.StoreList[0].NextDay()
        #DisplayStoreInfo()
    elif result == 'q' or 'Q':
        break
    else:
        print("Wrong input")
    #currentstore.StoreInfo()

print("----ended---")
