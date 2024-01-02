import time

def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:
        hours, reminder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(reminder, 60)

        timer = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        print(timer, end="\r")

        time.sleep(1)

        total_seconds -= 1

    print("Время вышло!")

def get_minutes():
    while True:
        try:
            minutes = int(input("Введите количество минут для таймера: "))
            if minutes < 0:
                raise ValueError("Время не может быть отрицательным. ")
            return minutes
        except ValueError as e:
            print(fr"Ошибка: {e}. Попробуйте ещё раз.")

minutes = get_minutes()

countdown(0, minutes, 0) 

        
