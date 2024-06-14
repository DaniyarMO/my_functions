class PersonalAccount:
    def __init__(self):
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        print("Счет успешно пополнен на", amount, "руб.")

    def purchase(self, amount, item):
        if amount > self.balance:
            print("Недостаточно средств на счете.")
            return
        self.balance -= amount
        self.history.append((item, amount))
        print("Покупка", item, "совершена успешно.")

    def show_history(self):
        print("История покупок:")
        for item, amount in self.history:
            print(item, "-", amount, "руб.")

    def display_menu(self):
        print("\nМеню:")
        print("1. Пополнить счет")
        print("2. Покупка")
        print("3. История покупок")
        print("4. Выход")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                amount = float(input("Введите сумму для пополнения счета: "))
                self.deposit(amount)
            elif choice == "2":
                amount = float(input("Введите сумму покупки: "))
                item = input("Введите название покупки: ")
                self.purchase(amount, item)
            elif choice == "3":
                self.show_history()
            elif choice == "4":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    account = PersonalAccount()
    account.run()
