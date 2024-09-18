class Computer:

    # What attributes will it need?
    description: str 
    processor_type: str 
    hard_drive_capacity: int 
    memory: int 
    operating_system: str 
    year_made: int 
    price: int 

    # How will you set up your constructor?
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.year_made = year_made
        self.price = price
    
    def update_price(self, new_price):
        self.price = new_price
        print ("The price is updated to: ", new_price)
    
    def update_os(self, os):
        self.operating_system = os

def main():
    my_computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    print(my_computer.description)

    if __name__ == "__main__": main()