#Implement an stack using list

class Stack:
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]
    def peak(self):
        if not is_empty(self):
            return self.item[-1]

    def get_stack(self):
        return self.items

if __name__=='__main__':

    s = Stack()
    s.push(5)
    s.push(4)
    s.push(6)
    s.push(3)
    s.push(7)

    print s.get_stack()

    s.pop()
    print s.get_stack()
