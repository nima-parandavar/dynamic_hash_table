class DHashTable(object):
    def __init__(self):
        self.hash_list = [None]
        
    def hash_func(self, item, i=0) -> int:
        index = (item % len(self.hash_list)) + i
        return index

    def insert(self, item: int, data: list):
        i = 0
        while True:
            index = self.hash_func(item, i)
            if self.hash_list[index] == None:
                break
            i -= 1
        
        self.hash_list[index] = [item, data]
        
        if self.is_full():
            self.extend()
            
    def search(self, item):
        i = 0
        count = 0
        while count <= len(self.hash_list):
            
            index = self.hash_func(item, i)
            if self.hash_list[index][0] == item:
                return self.hash_list[index]
            i -+ 1
            count += 1
        return False
    
    def delete(self, item):
        i = 0
        count = 0
        try:
            while count < len(self.hash_list):
                
                index = self.hash_func(item, i)
                if self.hash_list[index][0] == item:
                    self.hash_list[index] = None
                    break
                i -+ 1
                count += 1
        
        except TypeError:
            return False
        if self.is_third_empty():
            self.shrink()
        
    def is_third_empty(self):
        if self.hash_list.count(None) == (len(self.hash_list) // 3):    
            return True
        return False
        
    def is_full(self):
        if self.hash_list.count(None) == 0:
            return True
        return False
    
    def extend(self):
        length = len(self.hash_list)
        items = [i for i in self.hash_list if i != None]
        self.hash_list = [None] * (length * 2)
        
        for item in items:
            self.insert(item=item[0], data = item[1])
        
    def shrink(self):
        length = len(self.hash_list)
        items = [i for i in self.hash_list if i != None]
        self.hash_list = [None] * ((length // 3) + 1)
        
        for item in items:
            self.insert(item = item[0], data= item[1])
        
    def display(self):
        return self.hash_list