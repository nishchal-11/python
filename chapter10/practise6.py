from random import randint

class Train:

    def __init__(slf,trainNo):
         slf.trainNo=trainNo

    def book(slf,fromm,to):
        print(f"ticket is booked in train no {slf.trainNo} from {fromm} to {to}")

    def getStatus(slf):
         print(f"ticket no{slf.trainNo} is running on time")

    def getfare(slf,fromm,to):
         print(f"ticket fare in train no {slf.trainNo} from{fromm} to {to} is {randint(100,2000)}")


t=Train(1238)
t.book("delhi","blr")
t.getStatus()
t.getfare("delhi","blr")
