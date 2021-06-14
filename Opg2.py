class person:
    def __init__(self, name, lastname):
        self.name = name
        self.__lastname = lastname

    def hvem(self):
        print("navn: ", self.name)
        print("Efternavn: ", self.__lastname)

    def getlastname(self):
        print(self.__lastname)

    def setlastname(self, lastname):
        self.__lastname = lastname


bs = person("jens", "lange")
print(bs._person__lastname)
bs.getlastname()
print(bs.name)

bs.setlastname("jensen")
bs.name = "karsten"
bs.hvem()
print("---------Car without prop-------------")


class Car2:

    def __init__(self, mph, countrycode):
        self.mph = mph
        self.countrycode = countrycode


bmw1 = Car2(199, "DK")
bmw1.mph = 333
print(bmw1.mph)
bmw1.mph = 10
print(bmw1.mph)
print(bmw1)

print("----------Car with prop------------")


class Car:

    def __init__(self, mph, ckode):
        self.mph = mph
        self.ckode = ckode

    @property
    def mph(self):
        return self.__mph

    @property
    def ckode(self):
        return self.__ckode

    @mph.setter
    def mph(self, mph):
        if mph < 200:
            self.__mph = mph
        else :
            print("Way to fast!")

    @mph.getter
    def mph(self):
        return self.__mph

    @ckode.setter
    def ckode(self, ckode):
        if len(ckode) < 3:
            self.__ckode = ckode
        else :
            print("Error Wrong countrycode")

    @ckode.getter
    def ckode(self):
        return self.__ckode

    def __str__(self):
        return "This car's speed is: " + str(self.mph) + "Mph and Its countrycode is: " + str(self.ckode)


bmw2 = Car(199, "DK")
bmw2.ckode = "DDDD"
bmw2.mph = 5555
print(bmw2.mph)
print(bmw2)

