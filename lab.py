from faker import Faker
from faker.providers import DynamicProvider
import random
import time
import matplotlib.pyplot as plt


def insertion_sort(array):
    start_time = time.time()
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        j = i
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp
    end_time = time.time()
    total_time = end_time - start_time
    return total_time

def bubble(a):
    start_time = time.time()
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    end_time = time.time()
    total_time = end_time - start_time
    return total_time


def shake_sort(sequence):
    start_time = time.time()
    left = 0
    right = len(sequence) - 1
    control = right
    while left < right:
        for i in range(left, right):
            if sequence[i] > sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                control = i
        right = control
        for i in range(right, left, -1):
            if sequence[i] < sequence[i - 1]:
                sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]
                control = i
        left = control
    end_time = time.time()
    total_time = end_time - start_time
    return total_time

class IT:

    def __init__(self, name, price, prepayment):
        self.name = name
        self.price = price
        self.prepayment = prepayment

    def __le__(self, other):
        if self.price < other.price:
            return True
        elif self.price == other.price:
            if self.prepayment < other.prepayment:
                return True
            elif self.prepayment == other.prepayment:
                if self.name <= other.name:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        if self.price > other.price:
            return True
        elif self.price == other.price:
            if self.prepayment > other.prepayment:
                return True
            elif self.prepayment == other.prepayment:
                if self.name >= other.name:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.price < other.price:
            return True
        elif self.price == other.price:
            if self.prepayment < other.prepayment:
                return True
            else:
                if self.name >= other.name:
                    return False
                else:
                    return True
        else:
            return False

    def __gt__(self, other):
        if self.price > other.price:
            return True
        elif self.price == other.price:
            if self.prepayment > other.prepayment:
                return True
            else:
                if self.name <= other.name:
                    return False
                else:
                    return True
        else:
            return False

    def Print(self):
        print(self.name, self.price, self.prepayment)


IT_provider = DynamicProvider(
    provider_name="services",
    elements=["install", "delete", "download", "repair", "fix", "buy", "help"]
)

fake = Faker()
fake.add_provider(IT_provider)
fake.services()
with open('test.txt', 'w') as file:
    for i in range(1000):
        file.write(f"{fake.services()} {random.randrange(1000, 5000)} {random.randrange(100, 500)}\n")

objects_list = []
time_bubble=[]
time_insert=[]
time_shaker=[]


for i in range(100, 1100, 100):

    with open('test.txt', 'r') as file:
        lines = file.readlines()[i-100:i]

    for line in lines:
        data = line.split()
        name = data[0]
        price = int(data[1])
        prepayment = int(data[2])
        obj = IT(name, price, prepayment)
        objects_list.append(obj)

    print(len(objects_list))
    print(bubble(objects_list), shake_sort(objects_list), insertion_sort(objects_list))
    time_bubble.append(bubble(objects_list))
    time_shaker.append(shake_sort(objects_list))
    time_insert.append(insertion_sort(objects_list))

plt.xlabel("Кол-во элементов массива")
plt.ylabel("Время сортировки")
plt.plot([i for i in range(100, 1100, 100)], time_bubble, label='Пузырьком')
plt.plot([i for i in range(100, 1100, 100)], time_insert, label='Вставками')
plt.plot([i for i in range(100, 1100, 100)], time_shaker, color='c', label='Шейкер')
plt.legend()
plt.show()
