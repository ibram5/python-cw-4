def my_name(name):
    print(f"my name is {name}")
my_name("ibram")

def my_meal(food,drink):
    print(f"I like to eat {food} and while drinking {drink}")
my_meal("kfc","pepsi")

def cube(number):
    return number*number*number

def by_three(number):
    if number % 3 == 0:
      print(cube(number))
    else : 
        print(False)
by_three(int(input("enter the number :")))