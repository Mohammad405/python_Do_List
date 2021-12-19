import copy

class DoList:
    def __init__(self) -> None:
        self.lst = []
        self.index = -1
    def add(self,item):
        self.lst.append(item)

    def findItem(self,item):
        try:
            return self.lst.index(item) 
        except:
             print(f'{item} not found') 
        
    def delete(self,item):
        idx = self.findItem(item)
        del self.lst[idx]

    def clearAll(self):
        self.lst.clear()

    def length(self):
        return len(self.lst)

    def copy(self):
        return copy.copy(self)
    
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.lst):
            self.index = -1
            raise StopIteration
        else:
            return self.lst[self.index]
   
    def printList(self):
        for idx, item in enumerate(self.lst,1):
            print(f'{idx}- {item}')




