
from datetime import datetime 
class Student:


  def __init__(self,name,year,iq,DOB):
       self.name = name
       self.year = year
       self.iq = iq
       self.dob = DOB


  def get_name(self):
      print("Name :", self.name)

  def random_roll(self):
      
      print("name and iq :" + self.name, self.iq)


#custom methods-

  def calculate_age(self):
        today = datetime.today()
        dob = datetime.strptime(self.dob, "%d/%m/%Y")
        age = today.year - dob.year
        print("The age of the person is : ", age)








class Animal:
    def __init__(self, name, species, age):
        # Private attributes (indicated by double underscore __)
        self.__name = name
        self.__species = species
        self.__age = age
        self.__energy = 100  # Default attribute

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age









student1 = Student("Nikhil", 7, 100, "8/6/2014")
student2 = Student("Walter White", 50, 142, "9/7/1958")

student1.get_name()
student2.random_roll()
student1.calculate_age()


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def get_brand(self):
        print("The cool and random brand of the car is : ", self.brand)

    def get_speed(self):
        print("The speed of the car is : ", self.speed)

    def accelerate(self):
        self.speed += 10
        print("the acceleration is: ", self.speed)
car1 = Car("2003 Honda Civic",180)
car2 = Car("2015 Toyota Camry", 210)


car1.get_brand()
car2.get_brand()


car2.accelerate()