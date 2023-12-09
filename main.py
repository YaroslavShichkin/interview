class Stack():
    def __init__(self, empty_list):
        self.list = empty_list

    def is_empty(self):
        return len(self.list) != 0

    def push(self, el):
        self.list.append(el)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def check_balance(self, test):
        open_array = ['(', '[', '{']
        check_close_dict = {'(': ')', '[': ']', '{': '}'}
        for bracket in test:
            if self.is_empty():
                if bracket == check_close_dict[self.peek()]:
                    self.pop()
                    continue
            if bracket in open_array:
                self.push(bracket)
                continue
            return 'Несбалансированно'
        if not self.is_empty():
            return 'Сбалансированно'
        return 'Несбалансированно'

first = Stack([])
print(first.check_balance(input()))