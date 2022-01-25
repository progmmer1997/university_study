from collections import namedtuple

tupl = ('Physics', 'Chemistry', 'Math', 'English')
Marks = namedtuple('Marks', tupl)
marks = Marks(90, 85, 95, 100)
print(marks)