
class Mem_list(list):

    def map(self,fn):
        return Mem_list(map(fn,self))
    
    def reduce(self,fn):
        y=self[0]
        for i in range(1,len(self)):
            y=fn(y,self[i])
        return y

class Mem_table():
    def __init__(self):
        self.mem_table=dict()
