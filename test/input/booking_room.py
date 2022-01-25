def get_room_number():
    while True:
        try:
            num = int(input("Введите номер комнаты: "))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
room_number = get_room_number()
print(f"Комната {room_number} успешно забронирована!")
