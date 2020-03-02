class Queue():
    def __init__(self):
        self.queue = []

    
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)

    def __str__(self):
        out = f''
        for item in self.queue:
            out += f'{item}'
        return out