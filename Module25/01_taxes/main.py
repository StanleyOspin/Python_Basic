class Property:
    def __init__(self, worth):
        self.set_worth(worth)

    def get_worth(self):
        return self.__worth

    def set_worth(self, worth):
        self.__worth = worth

    def tax_calculation(self):
        self.tax = self.__worth / 1500
        return self.tax


class Appartment(Property):

    def tax_calculation(self):
        self.tax = self.get_worth() / 1000
        return self.tax


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        self.tax = self.get_worth() / 200
        return self.tax


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        self.tax = self.get_worth() / 500
        return self.tax


wallet = int(input('Сколько денег на вашем счете? '))

flat_worth = int(input('Стоимость квартиры: '))
flat = Appartment(worth=flat_worth)
flat_tax = flat.tax_calculation()

car_worth = int(input('Стоимость машины: '))
car = Car(worth=car_worth)
car_tax = car.tax_calculation()

country_house_worth = int(input('Стоимость дачи: '))
country_house = CountryHouse(worth=country_house_worth)
country_house_tax = country_house.tax_calculation()

total_tax = flat_tax + car_tax + country_house_tax

print('\nНалог на квартиру: {} рублей'.format(flat_tax))
print('Транспортный налог: {} рублей'.format(car_tax))
print('Дачный налог: {} рублей'.format(country_house_tax))
print('\nОбщая сумма налога: {} рублей'.format(total_tax))
if wallet >= total_tax:
    print('Жизнь удалась')
else:
    print('Денег не хватает даже на налоги, нужно идти работать!')
