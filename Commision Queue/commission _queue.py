import collections

class Commission:
    def __init__(self):
        self.commissionList = collections.deque()

    def add_commission(self):
        new_name = input("Name: ")
        new_project_type = input("Project type: ")
        new_price = input("Commission price: ")
        commission = [new_name, new_project_type, new_price]
        self.commissionList.append(commission)
    
    def add_commission_prioity(self):
        new_name = input("Name: ")
        new_project_type = input("Project type: ")
        new_price = input("Commission price: ")
        commission = [new_name, new_project_type, new_price]
        self.commissionList.appendleft(commission)
        
    def display_commissions(self):
        print(self.commissionList())

    def remove_commission(self):
        if self.commissionList.count(0) == 0:
            self.commissionList.popleft()


def main():
    

    c = Commission()
    canLoop = True
    while canLoop == True:
        print("Options are as follows:")
        print("\tADD to add a commission")
        print("\t!! to add a prioity commission")
        print("\tDISPLAY to display the commissions")
        print("\tREMOVE to remove a commission from the top of the list")
        print("\tQUIT to exit")

        responce = input(">")
        if responce in ["ADD", "add", "Add", "a", "A"]:
            c.add_commission()
        elif responce in ["!!", "!"]:
            c.add_commission_prioity()
        elif responce in ["Display","DISPLAY", "display", "d","D"]:
            c.display_commissions()
        elif responce in ["QUIT", "quit","Quit","q","Q"]:
            print("Thank you!")
            canLoop = False
        elif responce in ["REMOVE","remove","Remove","r","R"]:
            c.remove_commission()
        else:
            print("Invalid input")
            responce = input(">")

    
main()

