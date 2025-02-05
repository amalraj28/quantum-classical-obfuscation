from queue import LifoQueue


class Stack:
    def __init__(self, n: int = 0):
        self.st = LifoQueue(maxsize=n)

    def push(self, item):
        self.st.put_nowait(item)

    def pop(self):
        self.st.get_nowait()

    def top(self):
        item = self.st.get_nowait()
        self.push(item)
        return item

    def size(self):
        return self.st.qsize()

    def empty(self):
        return self.st.empty()
