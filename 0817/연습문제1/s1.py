class my_stack(object):
    
    def __init__(self, size):
        self.q_size = size
        self.appended = [0] * size
        self.idx = -1

    def push(self, x):
        if self.size == len(self.appended):
            return ('stackoverflow')
        else :
            self.idx += 1
            self.appended[self.idx] = x
    
    def pop(self):
        if self.appended:
            self.idx -= 1
            return self.appended[self.idx + 1]
        else:
            return -1

    def peek(self):
        if self.appended:
            return self.appended[-1]
        else:
            return (-1)

    def is_empty(self):

        return self.idx == 0

    def is_full(self):
        return self.idx == self.q_size

    def size(self):

        return self.idx

        

test = my_stack(3)

test.push(10)
test.push(5)
test.push(1)

print(test.pop())
print(test.pop())
print(test.pop())