def convert_currency(amount, rate):
    """Конветрирует сумму по заданному курсу"""
    return amount * rate

def main():
    rub_to_kzt_rate = 5.0
    cny_to_kzt_rate = 64.40
    usd_to_kzt_rate = 459.62


    
    print("Выберите валюту для конвертации в теньгушки: ")
    print("1: Рубль (RUB)")
    print("2: Пиндодошки (CNY)")
    print("3: Баксики (USD)")
    choice = input("Введите (1-3): ")

    if choice == '1':
        amount_in_rub = float(input("Введите сумму в Рубликах: "))
        amount_in_kzt = convert_currency(amount_in_rub, rub_to_kzt_rate)
        print(f"{amount_in_rub} RUB равно {amount_in_kzt:.2f} KZT")
    elif choice == '2':
        amount_in_cny = float(input("Введите сумму в Пиндодошках: "))
        amount_in_kzt = convert_currency(amount_in_cny, cny_to_kzt_rate)
        print(f"{amount_in_cny} CNY равно {amount_in_kzt:.2f} KZT")
    elif choice == '3':
        amount_in_usd = float(input("Введите сумму в Баксиках: "))
        amount_in_kzt = convert_currency(amount_in_usd, usd_to_kzt_rate)
        print(f"{amount_in_usd} USD равно {amount_in_kzt:.2f} KZT")
    else:
        print("Неверный выбор")

    
if __name__ == "__main__":
    main()

