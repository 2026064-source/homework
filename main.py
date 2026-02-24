class Car:
    def __init__(self, brand, model, year, ):
        self.brand = brand 
        self.model = model
        self.year = year 
    def about_Car(self):
      print(f"Self:{self.brand}.\nmodel:{self.model}.\nyear:{self.year}")
car1 = Car("Toyota","Corolla",2025)
car2 = Car("BMW", "X5", 2022)
car3 = Car("Tesla", "Model3", 2019)
print(car1.brand , car2.model)
print(car2.year , car2.brand)