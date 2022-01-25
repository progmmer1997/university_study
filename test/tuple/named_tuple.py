# для начала импортируем сам модуль
from collections import namedtuple
# создание именнованного кортежа
citizen = namedtuple("Citizen", "name age status")
Alex = citizen(name='Alex Mercer', age=27, status='show businessman')
print(Alex.name,Alex.status,sep="\n")

