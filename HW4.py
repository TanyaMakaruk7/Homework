class Car:
    __id = 0
    __brand = ' '
    __model = ' '
    __year_of_release = ' '
    __colour = ' '
    __price = ' '
    __registration_number = ' '

    def __init__(self, brand0, model0, year_of_release0, colour0, price0, ):
        self.__brand = brand0
        self.__model = model0
        self.__year_of_release = year_of_release0
        self.__colour = colour0
        self.__price = price0
        print('Новая запись создана')

    def get_id(self):
        return self.__id
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_year_of_release(self):
        return self.__year_of_release
    def get__colour(self):
        return self.__colour
    def get_price(self):
        return self.__price
    def get__registration_number(self):
        return self.__registration_number


def AboutCar(i):
    print('Brand: ' + AboutCar[i].get_brand())
    print('Model: ' + AboutCar[i].get_model())
    print('Year_of_release: ' + AboutCar[i].get_year_of_release())
    print('Color: ' + AboutCar[i].get__colour())
    print('Price: ' + AboutCar[i].get_price())
    print('----------------')

i=0
Car_list = [Car('opel', 'astra', '2000', 'black', '10000'),
            Car('BMW', 'a-10', '2016', 'white', '20000'),
            Car('opel', 'astra', '2000', 'black', '25000'),
            Car('BMW', 'a-10', '2016', 'white', '15000'),
            Car('opel', 'astra', '2000', 'black', '10000'),
            Car('nissan', 'a-11', '2010', 'green', '20000'),
            Car('opel', 'astra', '2000', 'green', '12000'),
            Car('nissan', 'a-11', '2010', 'blue', '8000'),
            Car('opel', 'astra', '2000', 'green', '10000'),
            Car('BMW', 'sr', '2010', 'blue', '15000'),
            Car('opel', 'astra', '2000', 'blue', '11000')]

Brand = 0
Year = 0

Brande = (input('введите марку \n'))

while i < len(Car_list):
    if Car_list[i].get_brand() == Brande:
        AboutCar(i)
    i+=1
i=0
Year = (input('введите год \n'))
while i < len(Car_list):
    if Car_list[i].get_year_of_release() > Year:
        AboutCar(i)
    i+=1