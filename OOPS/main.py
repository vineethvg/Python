# class
# class Dog:
#     pass


# instance / object
# obj1 = Dog()


class Car:
    def show(self, model, car):
        self.model = model
        self.car = car
        print("Model is", self.model)
        print("Car is", self.car)


ob1 = Car()

ob1.show("audi 18", "audi")
ob1.show("abcd", "benz")
