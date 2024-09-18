from computer import Computer
from typing import Dict, Optional, Union

# class made for management of all methods related to the computers in the shop
class ResaleShop:

    inventory : list 
    
    #initialization of the constructor
    def __init__(self):
        self.inventory = []
    
    #adding new computer to the list of options for selling 
    def buy(self, computer: Computer):
        self.inventory.append(computer)
    
    #selling the computer from the shop 
    def sell(self, computer: Computer) -> None:
        if computer in self.inventory:
            self.inventory.remove(computer) #removing computer from the list of available options  
            print("Item", computer, "sold!")
        else: 
            print("Item", computer, "not found. Please select another item to sell.")

    #printing the inventory 
    def print_inventory(self) -> None:
        if self.inventory:
            print(self.inventory)
        else:
            print("No inventory to display.")

    #method to update the price and/or of the computer
    def refurbish(self, computer: Computer, new_os: Optional[str] = None) -> None:
        if computer in self.inventory: # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff
            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", computer, "not found. Please select another item to refurbish.")

# main method made for testing the program
def main():
    comp = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2016, 1000)
    shop = ResaleShop()
    shop.buy(comp)
    shop.refurbish(comp, "Windows 12")
    print(comp.operating_system)
    print(comp.price)
    comp.update_price(1500)
    print(comp.price)
    shop.print_inventory()
    shop.sell(comp)
    shop.print_inventory()
    shop.refurbish(comp)

if __name__ == "__main__": main()