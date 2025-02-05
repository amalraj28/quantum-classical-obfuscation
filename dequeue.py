from collections import deque


class Deque:
    def __init__(self, n: int | None = None):
        self.dq = deque(maxlen=n)
    
    def push_back(self, item) -> None:
        self.dq.append(item)
    
    def push_front(self, item) -> None:
        self.dq.appendleft(item)
    
    def pop_back(self) -> None:
        self.dq.pop()
    
    def pop_front(self) -> None:
        self.dq.popleft()
    
    def empty(self) -> bool:
        return len(self.dq) == 0
    
    def size(self) -> int:
        return len(self.dq)

    def clear(self) -> None:
        self.dq.clear()
    
    def front(self):
        return self.dq[0]

    def back(self):
        return self.dq[-1]
    
