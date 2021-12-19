class Item:
    def __init__(self, name, count = 1 ) -> None:

        self.name = name
        self.count = count 

    def setName(self, newName):
        self.name = newName

    def setCount(self, newCount):
        self.count = newCount

    def getName(self):
        return self.name

    def getCount(self):
        return self.count

    def __add__(self, other):
        return self.count + other.count

    def __iadd__(self, other):
        self.count += other.count
        return self

    def __radd__ (self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __lt__(self, other):
        return self.count < other.count

    def __gt__(self, other):
        return self.count > other.count

    def __eq__(self,other):
        return self.name == other.name and self.count == other.count

    def __ne__(self, other):
        return self.name != other.name and self.count != other.count

    def __str__(self) -> str:
         return f'Item is {self.name}, You need {self.count}'







