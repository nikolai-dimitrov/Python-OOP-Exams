class ASD:
    def __init__(self,name):
        self.name = name
        self.__money = 0
asd = ASD("Test")
print(asd.name)
print(asd._ASD__money)