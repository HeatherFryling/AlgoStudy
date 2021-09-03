from collections import deque

class AnimalShelter:

    ANIMALS = ['cat', 'dog']

    def __init__(self):
        self.q = deque()

    # O(1) time | O(1) space
    def enqueue(self, animal):
        if animal[:3] not in self.ANIMALS:
            raise ValueError('Shelter only accepts:', str(self.ANIMALS))
        self.q.append(animal)
    
    # O(1) time | O(1) space
    def dequeue_any(self):
        if len(self.q) == 0:
            raise ValueError('Sorry, the shelter is empty!')
        else:
            return self.q.popleft()

    # O(n) time | O(n) space
    def dequeue_cat(self):
        dog_q = deque()
        if len(self.q) == 0:
            raise ValueError('Sorry, the shelter is empty!')

        curr = self.q.popleft()
        while (curr != None and curr[ : 3] != self.ANIMALS[0]):
            dog_q.append(curr)
            curr = self.q.popleft()
        
        # Put the dogs back in their correct position.
        while (len(dog_q) > 0):
            self.q.appendleft(dog_q.pop())

        return curr

    # O(n) time | O(n) space
    def dequeue_dog(self):
        cat_q = deque()
        if len(self.q) == 0:
            raise ValueError('Sorry, the shelter is empty!')

        curr = self.q.popleft()
        while (curr != None and curr[ : 3] != self.ANIMALS[1]):
            cat_q.append(curr)
            curr = self.q.popleft()
        
        # Put the dogs back in their correct position.
        while (len(cat_q) > 0):
            self.q.appendleft(cat_q.pop())

        return curr

s = AnimalShelter()
animals = ['cat1', 'cat2', 'dog1', 'dog2', 'dog3', 'cat3']
for animal in animals:
    s.enqueue(animal)
print(s.q)
print(s.dequeue_any())
print(s.q)
print(s.dequeue_dog())
print(s.q)
print(s.dequeue_cat())
print(s.q)
print(s.dequeue_cat())
print(s.q)



    