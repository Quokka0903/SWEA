class my_queue:

    def __init__ (self, leng):
        self.maxlen = leng
        self.front = 0
        self.rear = 0
        self.idx = 0
        self.q = [None] * self.maxlen

    def is_full(self):
        if self.idx == self.maxlen:
            return True
        else:
            return False

    def is_empty(self):
        if self.idx == 0:
            return True
        else:
            return False

    def enque(self, x):
        if self.is_full():
            return -1
        else:
            self.q[self.rear] = x
            self.idx += 1
            self.rear += 1
            if self.rear == self.maxlen:
                self.rear = 0
        
    def deque(self):
        if self.is_empty():
            return -1
        else:
            res = self.q[self.front]
            self.q[self.front] = None
            self.idx -= 1
            self.front += 1
            if self.front == self.maxlen:
                self.front = 0
            return res

    def peek(self):
        if self.is_empty:
            return -1
        else:
            return self.q[self.front]


# 임의로 길이 5칸의 큐 설정
test_q = my_queue(5)

test_q.enque(1)
test_q.enque(2)
test_q.enque(3)

print(test_q.deque())
print(test_q.deque())
print(test_q.deque())