operations = ['push 4', 'pop', 'push 3', 'push 5', 'push 2', 'inc 3 1', 'pop', 'push 1', 'inc 2 2', 'push 4', 'pop', 'pop']

def superStack(operations):
    SS = Super_Stack()
    for op in operations:
        if op.find('pop') >= 0:
            SS.super_pop()
        elif op.find('push') >= 0:
            SS.super_push(op.split()[1])
        else:
            SS.super_inc(int(op.split()[1]),int(op.split()[2]))

class Super_Stack:
    def __init__(self):
        self.top = []
        self.count = 0

    def __len__(self):
        return len(self.top)

    def __str__(self):
        return str(self.top[::1])

    def super_pop(self):
        #print("pop")
        self.top.pop(-1)
        self.count -= 1
        if self.count <= 0:
            print("EMPTY")
        else:
            print(self.top[-1])

    def super_push(self,num):
       # print("push",num)
        self.top.append(num)
        self.count += 1
        if self.count <= 0:
            print("EMPTY")
        else:
            print(self.top[-1])

    def super_inc(self,i,v):
       # print("inc", i, v)
        for index in range(i):
            self.top[index] = str(int(self.top[index]) + v)
        if self.count <= 0:
            print("EMPTY")
        else:
            print(self.top[-1])

case_divide(operations)