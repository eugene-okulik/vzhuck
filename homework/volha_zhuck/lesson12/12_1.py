class Flower():
    name = ''
    color = ''
    price = 0
    lenght = 0
    time_of_living = 0
    freshness = True

    def __init__(self, name, color, price, lenght, time_of_living, freshness=True) -> None:
        self.name = name
        self.color = color
        self.price = price
        self.lenght = lenght
        self.time_of_living = time_of_living
        self.freshness = freshness
        pass

    def printFlower(self):
        if self.freshness:
            print(f"Name: {self.name}, Color: {self.color}, Price: {self.price}, Length: {self.lenght}, Freshness: Yes")
        else:
            print(f"Name: {self.name}, Color: {self.color}, Price: {self.price}, Length: {self.lenght}, Freshness: No")


class Rose(Flower):

    def __init__(self, color, price, lenght, time_of_living, freshness=True) -> None:
        super().__init__('Rose', color, price, lenght, time_of_living, freshness)


class Sunflower(Flower):

    def __init__(self, color, price, lenght, time_of_living, freshness=True) -> None:
        super().__init__('Sunflower', color, price, lenght, time_of_living, freshness)
   

class Tulip(Flower):

    def __init__(self, color, price, lenght, time_of_living, freshness=True) -> None:
        super().__init__('Tulip', color, price, lenght, time_of_living, freshness)


class Lily(Flower):

    def __init__(self, color, price, lenght, time_of_living, freshness=True) -> None:
        super().__init__('Lily', color, price, lenght, time_of_living, freshness)


class Bouquet:

    def __init__(self):
        self.flowers = []

    def addFlower(self, flower):
        self.flowers.append(flower)
        return self

    def printBouquet(self):
        for flower in self.flowers:
            flower.printFlower()
    
    def avgLifetime(self):
        if len(self.flowers) == 0:
            return 0
        sum = 0
        for flower in self.flowers:
            sum += flower.time_of_living
        avg = sum / len(self.flowers)
        return int(avg)
    
    def priceBouquet(self):
        price = 0
        for flower in self.flowers:
            price += flower.price
        return price
    
    def searchFlowers(self, color):
        for flower in self.flowers:
            if color == flower.color:
                yield flower

    def sortFlowers(self, key):
        if key == "freshness":
            self.flowers.sort(reverse=True, key=lambda f: f.freshness)
        elif key == "color":
            self.flowers.sort(key=lambda f: f.color)
        elif key == "length":
            self.flowers.sort(key=lambda f: f.lenght)
        elif key == "price":
            self.flowers.sort(key=lambda f: f.price)


rose1 = Rose('Yellow', 80, 35, 10, False)
rose2 = Rose('Red', 40, 30, 5, True)
lily1 = Lily('Red', 33, 45, 7, True)
lily2 = Lily('White', 33, 45, 7, True)
tulip1 = Tulip('Purple', 20, 10, 3, True)
sunflower1 = Sunflower('Yellow', 100, 23, 9, False)
#  make bouquet
b1 = Bouquet() \
    .addFlower(rose1) \
    .addFlower(rose2) \
    .addFlower(lily1) \
    .addFlower(tulip1) \
    .addFlower(sunflower1) \
    .addFlower(lily2)
#  average time of living
b1.printBouquet()
print(b1.avgLifetime())
#  price for bouquet
b1.priceBouquet()
print(b1.priceBouquet())
#  seach by color
print('Search by color')
color = 'Red'
found = b1.searchFlowers(color)
for fl in found:
    fl.printFlower()
#  sort flowers by price
b1.sortFlowers(key='price')
print("Bouquet sorted by price: ")
b1.printBouquet()
