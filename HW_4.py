class Car:
    __idName = ''
    __carMark = ''
    __model = ''
    __year = 0
    __color = ''
    __price = 0
    __carNum = ''

    def __init__(self, idName0, carMark0, model0, year0, color0, price0, carNum0):
        self.__idName = idName0
        self.__carMark = carMark0
        self.__model = model0
        self.__year = year0
        self.__color = color0
        self.__price = price0
        self.__carNum = carNum0
        print
        'New object created!'

    def get_idName(self):
        return self.__idName

    def get_carMark(self):
        return self.__carMark

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_carNum(self):
        return self.__carNum

    def carAge(self, curryYears=2021):
        return curryYears - self.get_year()


def carInfoOut(i):
    print(str(CarPark[i].carAge()) + ' years old bus'
    + '\nidName: ' + CarPark[i].get_idName()
    + '\ncarMark: ' + CarPark[i].get_carMark()
    + '\nmodel: ' + CarPark[i].get_model()
    + '\nyear: ' + str(CarPark[i].get_year())
    + '\ncolor: ' + CarPark[i].get_color()
    + '\nprice: ' + str(CarPark[i].get_price())
    + '\ncarNum: ' + CarPark[i].get_carNum())


i = 0
CarPark = [Car('A-1', 'Ford', 'Fokus', 2010, 'black', '10000', '1221 MA-7'),
           Car('A-10', 'Nissan', 'A', 2012, 'green', '20000', '3214 MA-7'),
           Car('A-30', 'Opel', 'TM', 2016, 'black', '15000', '1234 MA-7'),
           Car('A-11', 'Volkswagen', 'Polo', 2019, 'black', '12000', '1200 MA-7'),
           Car('A-50', 'Chevrolet', 'X', 2014, 'black', '14000', '3666 MA-7'),
           Car('A-55', 'Volkswagen', 'Golf', 2013, 'white', '18000$', '1212 MA-7'),
           Car('A-60', 'BMW', 'A', 2017, 'black', '14000', '1234 MA-7'),
           Car('C-1', 'Audi', 'Rul', 2012, 'black', '160000', '1237 MA-7')]

carMark = ''
termNun = 0

carMark = ''
termNun = 0

carMark = (input('Введите марку автомобиля \n'))
while i < len(CarPark):
    if CarPark[i].get_carMark() == carMark:
        carInfoOut(i)
    i += 1

model = input('Введите модель автомобиля \n')
age = int(input('Возраст автомобиля \n'))
i = 0
while i < len(CarPark):
    if (CarPark[i].get_model() == model and CarPark[i].carAge() > age):
        carInfoOut(i)
    i += 1

