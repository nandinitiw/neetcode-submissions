class MinStack:
    #push onto the end of hashmap

    def __init__(self):
        self.data = {}
        self.length = 0
        

    def push(self, val: int) -> None:
        self.length += 1
        self.data[self.length-1] = val
        

    def pop(self) -> None:
        ret_val = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return ret_val
        

    def top(self) -> int:
        return self.data[self.length-1]
        

    def getMin(self) -> int:
        return min(self.data.values())

        
