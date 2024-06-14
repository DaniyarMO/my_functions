def check_input(prompt, expected):
    user_input = input(prompt)
    while user_input != expected:
        print("Не верно")
        user_input = input(prompt)
    return user_input

def main():
    year = check_input('Введите год рождения А.С.Пушкина:', '1799')
    day = check_input('В какой день июня родился Пушкин?', '6')
    print('Верно')

if __name__ == "__main__":
    main()
