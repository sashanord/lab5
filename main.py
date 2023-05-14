class StackIsEmptyError(Exception):
    def __init__(self):
        super(StackIsEmptyError, self).__init__("Стек пуст!")


class Stack:
    def __init__(self) -> None:
        self.adaptee = list()

    def push(self, o):
        self.adaptee.append(o)

    def pop(self):
        if len(self.adaptee) == 0:
            raise StackIsEmptyError()
        ans = self.adaptee[-1]
        self.adaptee = self.adaptee[:-1]
        return ans

    def __str__(self):
        return self.adaptee.__str__()




my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
my_stack.pop()
my_stack.pop()
print(my_stack)
my_stack.pop()
my_stack.pop()
