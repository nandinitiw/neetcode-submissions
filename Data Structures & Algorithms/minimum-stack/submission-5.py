class MinStack:
    #push onto the end of hashmap
    #have some type of hashmap with the first value being the minimum
    #in ascending order
    #question is - what data structure to just store and sort the values
    #just need to store the minimum and next minimum?

    #maybe create a stack to store the potential minimum values and 
    #if pop returns the top of the minimum stakc we pop it from there too?

    def __init__(self):
        self.data = []
        self.values = []

    def push(self, val: int) -> None:
        self.data.append(val)

        if(len(self.data) == 1):
            self.values.append(val)
        elif val <= self.values[-1]:
            self.values.append(val)
        

    def pop(self) -> None:
        ret_val = self.data[-1]
        del self.data[-1]

        if(ret_val == self.values[-1]):
            del self.values[-1]
        return ret_val
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        if len(self.values)==0:
            return None
        return self.values[len(self.values)-1]
        

        
