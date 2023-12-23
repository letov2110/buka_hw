import time


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        return "move"

    def stop(self):
        return "stop"

    def birthday(self):
        return self.age + 1


#####
class Truck(Auto):
    def __init__(self, brand, age, mark, color, weight, max_load):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        return f"attention {super().move()}"

    def load(self):
        time.sleep(1)
        a = "load"
        time.sleep(1)

        return a


truck_1 = Truck("bigcar", 10, "model_1", "red", 2200, 100)
truck_2 = Truck("bigcar_2", 20, "model_2", "Blue", 2000, 333)
print(
    f'\n{"name brand".ljust(20)} {(truck_1.brand).ljust(10)} vs {truck_2.brand.rjust(10)}\n'
    f'{"age truck".ljust(20)} {truck_1.age} years {truck_2.age:>9} years\n'
    f'{"truck color".ljust(20)} {(truck_1.color).ljust(10)} {truck_2.color.rjust(9)}\n'
    f'{"mark of truck".ljust(20)} {(truck_1.mark).ljust(10)} {truck_2.mark.rjust(12)}\n'
    f'{"weight of truck".ljust(20)} {truck_1.weight} kg  {truck_2.weight:>11} kg\n'
    f'{"max load".ljust(20)} {truck_1.max_load} ton {truck_2.max_load:>11} ton\n'
)
print(f"truck 1 can {truck_1.move()} and truck 2 can {truck_2.move()}")
print(f"truck 1 can {truck_1.stop()} and truck 2 can {truck_2.stop()}")
print(
    f"age of truck 1 +1 year = {truck_1.birthday()} years age of truck 2 +1 year = {truck_2.birthday()} years"
)
print(f"truck 1 can: {truck_1.load()} and truck 2 can: {truck_2.load()}")


#########
class Car(Auto):
    def __init__(self, brand, age, mark, color, max_speed):
        super().__init__(brand, age, color, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        return f"max speed {self.max_speed}"


car_1 = Car("jigyli", 50, "black", "model_3", 200)
car_2 = Car("pobeda", 40, "White", "model_4", 250)

print(
    f'\n{"name brand".ljust(15)} {car_1.brand.ljust(9)} vs {car_2.brand.rjust(7)}\n'
    f'{"age car".ljust(15)} {car_1.age} years{car_2.age:>8} years \n'
    f'{"car color".ljust(15)} {car_1.color} {car_2.color.rjust(13)} \n'
    f'{"mark of car".ljust(15)} {car_1.mark} {car_2.mark.rjust(13)}\n'
    f'{"max speed".ljust(15)} {car_1.max_speed} {car_2.max_speed:>13} km\h'
)
print(f"jiguli have {car_1.move()} km\h and pobeda have {car_2.move()} km\h")
print(f"jiguli can {car_1.stop()} and pobeda can {car_2.stop()}")
print(
    f"age jigyli +1 year = {car_1.birthday()} years and age poeda + 1 year = {car_2.birthday()} years"
)


####### zadanie 3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def sravn(self, circle_2):
        if self.radius == circle_2.radius:
            return Point(self.x, self.y)
        else:
            sravn_radius = abs(self.radius - circle_2.radius)
            return Circle(self.x, self.y, sravn_radius)


circle_1 = Circle(10, 4, 6)
circle_2 = Circle(6, 7, 5)
a = circle_1.sravn(circle_2)
if isinstance(a, Point):
    print(
        f"радиусы окружностей {circle_1.radius} и {circle_2.radius} равны\n"
        f"реультатом будет точка с координатами х={circle_1.x-circle_2.x} у={circle_1.y-circle_2.y}" )
else:
    print(
        f"радуы окружнстей {circle_2.radius} и {circle_1.radius} неравны\n"
        f"результатм будет окружность с точками x={circle_1.x-circle_2.x} y={circle_1.y-circle_2.y}  и радиусом {a.radius}"
    )
