#Idle Tycoon Game

import tkinter as tk

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
        try:
            whichstore = int(input("which store do you want to buy"))
        except:
            print("Invalid input..try again")
            return
        if whichstore >= 1 and whichstore <= len(Store.StoreList):
            store = Store.StoreList[whichstore-1]
            if store.StoreCost <= Store.Money:
                store.StoreCount +=1
                print(store.StoreCount)
                Store.Money -= store.StoreCost
            else:
                print("you dont have enough money")
        else:
            print("Enter a number between 1-3")

    @classmethod
    def NextDay(cls):
        cls.Day += 1
        for store in cls.StoreList:
            DailyProfit = store.StoreProfit + store.StoreCount
            cls.Money += DailyProfit

#name of the store, profit for the store, storecost
Store.StoreList.append(Store("Lemonade Stand", 1.50, 3))
Store.StoreList.append(Store("Record Store", 5, 0.5))
Store.StoreList.append(Store("Icecream Store", 10, 9))

root = tk.Tk()
root.mainloop()











'''
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
'''
