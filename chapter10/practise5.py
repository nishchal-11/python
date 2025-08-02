from random import randint

class Train:

    def __init__(self,trainNo):
         self.trainNo=trainNo

    def book(self,fromm,to):
        print(f"ticket is booked in train no {self.trainNo} from {fromm} to {to}")

    def getStatus(self):
         print(f"ticket no{self.trainNo} is running on time")

    def getfare(self,fromm,to):
         print(f"ticket fare in train no {self.trainNo} from{fromm} to {to} is {randint(100,2000)}")


t=Train(1238)
t.book("delhi","blr")
t.getStatus()
t.getfare("delhi","blr")
