def add_bill(bill):
    with open('bills.txt', 'a') as file:
        file.write(f"{bill}\n")

def show_total_bills():
    total = 0
    with open('bills.txt', 'r') as file:
        for line in file:
            total += float(line.strip())
    print(f"Общий баланс: {total}")

while True:
    action = input("Введите 'добавить' для добавления счета или 'показать' для текущего баланса (введите 'выход' для завершения): ")
    if action == 'выход':
        break
    elif action == 'добавить':
        bill = input("Введите сумму счета: ")
        add_bill(bill)
    elif action == 'показать':
        show_total_bills()