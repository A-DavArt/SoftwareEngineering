import random
def roll():
    die_value = random.randint(1, 6)
    print(f"Выпало: {die_value}")
    if die_value >= 5:
        print("Вы победили!")
    elif die_value >= 3:
        roll()
    else:
        print("Вы проиграли!")
if __name__ == "__main__":
    roll()
