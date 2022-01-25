# создание именнованного кортежа методом make()
from collections import namedtuple

lst = ['Physics', 'Chemistry', 'Math', 'English']
Marks = namedtuple('Marks', lst)
marks = Marks._make([55, 78, 98, 90])
print(marks)