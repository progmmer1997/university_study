from  collections import namedtuple

dct = {'Physics': 0, 'Chemistry': 0, 'Math': 0, 'English': 0}
Marks = namedtuple('Marks', dct)
marks = Marks(90, 85, 95, 100)
print(marks)