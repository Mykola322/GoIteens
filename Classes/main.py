class Nissan():
    car_model = "GTR"
    run = False
    fuel = False

    def fill_Up(self):
        self.fuel = True
        print("Refueling....")


    def accelerate(self):
        if self.fuel:
            print("accelerating....")
        else:
            print("Not enough fuel to start")


GTr = Nissan()
Skyline = Nissan()


#print(SkyLine.car_model)
#SkyLine.car_model = "Skyline GTR"
#print(SkyLine.car_model)


#Skyline.accelerate()
#Skyline.fill_Up()
#Skyline.accelerate()
#GTr.accelerate()



class Dodge():
    car_model = "Challenger"
    run = False
    tyre = False

    def patch_tyre(self):
        self.tyre = True
        print("Patching....")


    def accelerate(self):
        if self.tyre:
            print("accelerating....")
        else:
            print("Driving is dangerous. The tire is punctured")

Challenger = Dodge()

Challenger.accelerate()
Challenger.patch_tyre()
Challenger.accelerate()
