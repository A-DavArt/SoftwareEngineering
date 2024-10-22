def log_expense(expense):
    with open('expenses.txt', 'a') as file:
        file.write(expense + '\n')

def display_expenses():
    with open('expenses.txt', 'r') as file:
        expenses = file.readlines()
        for expense in expenses:
            print(expense.strip())

while True:
    action = input("Введите 'добавить' для записи расхода или 'просмотреть' для показа расходов (введите 'выход' для завершения): ")
    if action == 'выход':
        break
    elif action == 'добавить':
        expense = input("Введите информацию о расходе: ")
        log_expense(expense)
    elif action == 'просмотреть':
        display_expenses()