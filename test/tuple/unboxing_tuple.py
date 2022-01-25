 # Упаковка кортежа
is_tuple = ('a',)
is_tuple_too = 'b',
not_a_tuple = 'c'
print("is_tuple",is_tuple,type(is_tuple),"is_tuple_too",is_tuple_too,
      "not_a_tuple",not_a_tuple,type(is_tuple_too),type(not_a_tuple),sep="\n")
# распаковка кортежа
notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
do, re, mi, fa, sol, la, si = notes
print(mi)
#При необходимости  получить лишь какие-то отдельные значения, то в качестве
# "ненужных" переменных позволено использовать символ нижнего подчеркивания
# "_"
night_sky = 'Moon', 'Stars'
moon, _ = night_sky
print(moon)
