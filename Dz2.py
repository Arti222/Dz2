import random

class Student:
    def __init___(self, name):
        self.money = 60
        self.name = nick
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def rabota(self):
        if self.money <=10:
            print("nado bablo")
            self.gladness -=10
            self.money += 40
            self.progress +=0.8
        elif self.money >=10:
            self.money == money
    def to_study(self):
        print("UCHITSA")
        self.progress += 0.12
        self.gladness -= 5
        self.money += 20
    def to_sleep(self):
        print("Треснуть бы конечно не помешало")
        self.gladness += 3
        self.money -=5
    def to_chill(self):
        print("Standoff2 v prioritete")
        self.gladness += 5
        self.progress -= 0.1
        self.money -=20
    def  mega_chil(self):
        print("Tik Tooooook")
        self.gladness += 10
        self.progress -= 0.2
        self.money -=25
    def is_alive(self):
        if self.progress < -0.5:
            self.money == 0
            print("OTCHISLENO")
            self.alive = False
        elif self.gradness  <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("EXTERN")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {round(self.money, 3)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "suffering"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        if live_cube == 3:
            self.to_chill()
            self.and_of_day()
            self.is_alive()

nick = Student(name = "Artemka")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
