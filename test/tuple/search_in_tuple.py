input_box = ('firstbox', (15, 150))
# помним про индексацию, ведущую своё начало с 0
print(input_box[1][1])
# Если элемент кортежа есть вложенный кортеж, то применяются
# дополнительные квадратные скобки (в зависимости от уровня
# вложенности).
# Например, чтобы обратиться ко второму элементу второго
# элемента, следует поступить так:
input_box = ('firstbox', (15, 150))
# помним про индексацию, ведущую своё начало с 0
print(input_box[1][1])
#  поиск элемента в кортеже
song = ('Roses', 'are', 'Red')
print('Red' in song)
print('Violet' in song)

