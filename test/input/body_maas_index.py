print("Это калькулятор индекса массы тела")
weight=float(input("Введите вас вес(кг):"))
height=float(input("Введите ваш рост(м):"))
body_mass_index=round(weight/height**2,1)
if body_mass_index<=16.0:
    print("Индекс массы тела равен:",body_mass_index,"\n",
          "Ваш индекс массы тела соответствует Выраженному дефециту массы тела.\n Обратитесь к врачу")
elif  body_mass_index>=16 and body_mass_index<=18.5:
    print("Индекс массы тела равен",body_mass_index,"\n",
          "Ваш индекс массы тела соответствует дефециту массы тела.","Обратитесь к врачу")
elif body_mass_index>=18.5 and body_mass_index<=25.0:
    print("Индекс массы тела равен:",body_mass_index,"\n",
          "Ваш индекс массы тела соответствует норме.\n Так держать!!!")
elif body_mass_index>=5 and body_mass_index<=30:
    print("Индекс массы тела :",body_mass_index,"\n",
          "Ваш индекс массы тела соответствует избыточному весу.\n Попробуйте изменить жизнь")
elif body_mass_index>=0 and body_mass_index <=35:
    print("Индекс массы тела равен",body_mass_index,"\n",
          "Ваш индекс массы тела соответствует ожирению I степени.\n Обратитесь к врачу")
elif body_mass_index>=35 and body_mass_index<=40:
    print("Индекс массы тела равен:",body_mass_index,"\n",
          "Ваш индекс массы тела соответствует ожирению II степени.\n Обратитесь к врачу")
elif body_mass_index>=40:
    print("Индекс массы тела:",body_mass_index,"\n",
          "Ваш индекс массы тела соответствует ожирению III степени.\n Обратитесь к врачу")
