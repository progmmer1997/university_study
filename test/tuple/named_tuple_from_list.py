from collections import namedtuple

lst = ['Physics', 'Chemistry', 'Math', 'English']
Marks = namedtuple('Marks', lst)
marks = Marks(90, 85, 95, 100)
print(marks)