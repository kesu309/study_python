class Car(object):

    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        # print(f"{self.manufacturer}の{self.model_name}燃費:{self.mileage}, アクセル全開")
        print("{0.manufacturer}の{0.model_name}燃費:{0.mileage}, アクセル全開".format(self))

    def breakes(self):
        print("{0.manufacturer}の{0.model_name}(燃費:{0.mileage}), ブレーキ".format(self))

if__name__ == "__main__":
    conti_gt = Car("Bentley Continental GT", 4, "Bentley")
    prius = Car("prius", 20, "TOYOTA")
    print(prius.mileage)
    prius.gas()
    prius.gas()
    prius.breakes()
    conti_gt.gas()