#OBJECT : A "bundle" of related attributes(variable) and methods (functions)
    #Ex: phone , cup, book,etc
#CLASS : A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# class car:
#     def __init__ (self,model,year,color,for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
# car1 = car("BMW",2023,"Pink",True)
# print(car1.model)#here . is attribute access operator which is used to access the attributes of the class.
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)


#INHERITANCE
# class Animal:
#     def __init__ (self,name):
#         self.name = name
#         self.is_alive = True 
#     def eat(self):
#         print(f"{self.name} is eating.")
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# dog = Dog("Scooby")
# cat = Cat("Fluffy")
# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()
# print(dog.name)

