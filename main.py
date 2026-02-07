#task 1
tup_1 = (1, 2, 3)
print(max(tup_1) - min(tup_1))

#task 2

tup_2 = (5,2,-2,7,-8,-9,1, 0)
neww = [1 for i in range(len(tup_2) - 1) #0n
        if tup_2[i] < 0 and tup_2[i + 1] > 0 #O1
        or tup_2[i] >= 0 and tup_2[i + 1] < 0] #O1
print(sum(neww)) #O1

#task_3

tup_2 = (5, 2, -2, 7, 8, -9, 1, 4, 1024, 9, 5, 17)
primary = []
for dig in tup_2:
    if dig <= 0:
        continue
    count = 0
    for i in range(1, int(dig ** 0.5) + 1):
        if dig % i == 0:
            count += 1
        if count == 2:
            break
    else:
        primary.append(dig)
print(primary)

#task 4

tup_2 = (5, 2, 2, 10, 9, 5, 17, 1, -5, -7, -15)
count = 0
final = []
for i in range(len(tup_2) - 1):
    if tup_2[i] < tup_2[i + 1]:
        maxx = tup_2[i - count: i+2]
        count += 1
        if len(maxx) > len(final):
            final = maxx
    else:
        count = 0
tup_2 = tup_2[::-1]
for i in range(len(tup_2) - 1):
    if tup_2[i] < tup_2[i + 1]:
        maxx = tup_2[i - count: i + 2]
        count += 1
        if len(maxx) > len(final):
            final = maxx
    else:
        count = 0
print(final)

#task 5

tup_2 = (5, 2, 2, 10, 9, 5, 17, 1, -5, -7, -15, 5)
for i in range(len(tup_2)):
    if tup_2[i] in tup_2[:i]:
        print(tup_2[i], end = ' ')

#task 6

list_2 = [8,1,2,4,9,5,7,6]
list_1 = [4,1,6,9, 11, -6]
flag = False
minn = max(list_1) + 1
for num in list_1:
    if num not in list_2 and num < minn:
        minn = num
        flag = True

if flag:
    print(minn)
else:
    print('таких чисел нет')

#task 7

lisst = [1, 34, 89, 902, 3]
new_list = [[i, int(str(i)[::-1])] for i in lisst if i % 2 == 0]
for i in new_list:
    print(*i, end = ' ')


#task 8

listt = [8,1,2,4,9,5,7,6,8, 4, 4]
stroka = [str(i) for i in listt]
stroka = ''.join(stroka)
listt = list(set(listt))
for i in range(len(listt)):
    print(listt[i], stroka.count(str(listt[i])))

#task 9

lis = [9, 90, -6, 0, 9, -6, -20, 8, 0]
polog = []
otr = []
nol = []
for i in lis:
    if i > 0:
        polog.append(i)
    elif i < 0:
        otr.append(i)
    else:
        nol.append(i)
neww = polog + otr + nol
print(*neww)

#task 10

listt = [9, 90, -6, 0, 9, -6, -20, 8, 0, 4]
neww = []
for i in range(len(listt)):
    q = 1
    if listt[i] not in listt[:i] and listt[i] not in listt[i + 1:]:
        q = 2
    for _ in range(q):
        neww.append(listt[i])
print(*neww)

#task 11

school = {
    '9a': 15,
    '9b': 17,
    '9v': 22,
    '10a': 21,
    '10b': 18,
    '10v': 15,
    '11a': 20,
    '11b': 19,
    '11v': 18
}

school['9v'] = 20        # обновляем количество учеников в 9v
school['9d'] = 15        # добавляем новый класс 9d
del school['9v']         # удаляем класс 9v

pup = 0
for val in school:
    pup += school[val]

print(pup)               # выводим общее количество учеников (через цикл)
print(sum(school.values()))  # выводим то же самое через встроенную функцию

#task 12

sett = set([i for i in range(1, int(input('загадайте максимальное число')) + 1)])
n = int(input('Август загадывает число'))
while len(sett) != 1:
    bea = set(int(i) for i in input('Беатрис вводит числа через пробел').split())
    if n in bea:
        sett &= bea
        print(*sett, '- возможные числа')
    else:
        sett -= bea
        print(*sett, '- возможные числа')
else:
    print(f'вы угадали, число загаданное Августом {n}')


#task 13

sleng = {}
text = [i.split(':') for i in input().lower().split('.')[:-1]]
for txt in text:
    sleng[txt[0].strip()] = txt[1]
n = int(input('введите количество слов'))
for i in range(n):
    word = input('введите слово').lower().strip()
    if word in sleng.keys():
        print(sleng[word])
    else:
        print('не найдено')

#less 8


try:
    x = (1, 2, 5, 7)
    x = x / 2
except Exception as e:
    print(e)

#task 2

try:
    x = [1, 2, 5, 7]
    x[5] = 6
except IndexError:
    pass

a, b, c = map(int, input('введите a b c через пробел').split())
try:
    if a = 0 or b == 0 or c == 0:
        raise ArithmeticError("одна из сторон равна 0")
    else:
        p = (a + b + c) / 2
        s = (p(p-a)(p-b)(p-c))**0.5
        print(s)
except ArithmeticError as e:
    print(e)
except Exception:
    pass

#task 5

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
try:
    try_key = input("введите ключ удаляемого элемента")
    if try_key not in dictionary:
        raise KeyError('данного ключа нет в хеш таблице') #используем raise тк в условии написано бросить исключение
    else:
        print(dictionary[try_key])
except KeyError as e:
    print(e)
except Exception:
    pass

#task 4

listik = [1, 3, 6, 7, 9, 0]
index_try = int(input())
try:
    if len(listik) - 1 < index_try:
        raise TypeError('index out of range')
    else:
        del listik[index_try]
except TypeError as e:
    print(e)
except Exception:
    pass

#task 6
summ_list = input().split()
summ = 0
for num in summ_list:
    try:
        summ += int(num)
    except Exception:
        pass
print(summ)

#task 7

dictik = {}
try:
    stroka = input().split()
    ''.join(stroka)
    for sumb in stroka:
        try:
            int(sumb)
        except ValueError:
            if sumb in dictik.keys():
                dictik[sumb] += 1
            else:
                dictik[sumb] = 1
except ValueError:
    print(TypeError)
finally:
    print(dictik)

#lesson 9 task 1

def minimal_num(a,b):
    return min(a,b)

q, w , c, d = [1,2,3,4]

print(minimal_num((minimal_num(q,w)), minimal_num(c,d)))

#task 2

def ideal_num(num):
    finall = sum([i for i in range(1, int(num / 2) + 1) if num % i == 0])
    if finall == num:
        print('YES')
    else:
        print('NO')

ideal_num(int(input()))

#task 3


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(fib(int(input())))

#task 4

def closest_mode(num):
    if num % 5 ==0:
        return num
    else:
        return num + (5 - num % 5)

print(closest_mode(5))

#task 5

def check_variable():
    variable = input()
    while variable != 'поработали, и хватит':
        flag = True
        if not variable[0].isalpha():
            flag = False
        for i in variable:
            if not (i.isalpha() or i.isdigit() or i == '_'):
                flag = False
        if flag:
            print('можно использовать')
        else:
            print('нельзя использовать')
        print('для завершения работы наберите "поработали, и хватит"')
        flag = True
        variable = input()

check_variable()

#task 6
def generator():
    return [i for i in range(10, 100) if i % 2 == 1]

print(generator())

#task 7

lisst = [i for i in range(100, 1000) if i % 3 == 0 and i % 5 == 0]
print(lisst)

#task 8
listik = [1, 1, 5, 6, 8, 8, 8, 9, 9, 11, 87, 87]
def diferet_el(listik):
    count = sum([1 for i in range(len(listik)-1) if listik[i] != listik[i+1]])
    return count
print(diferet_el(listik))

#task 9

listt = list(map(int, input().split()))
if len(listt) == 1:
    print(listt)
else:
    listt = [listt[-1]] + listt + [listt[0]]
    new_lisst = [listt[i - 1] + listt[i+1] for i in range(1, len(listt)-1)]
    print(new_lisst)

#task 10

listt = ['aa', 'b', 'fgc', 'd', 'ehg', 'rtyui', 'd']
listt.sort(key=len, reverse=True)
print(listt)

#task 11

listt = ['aa', 'b', 'fgc', 'd', 'ehg', 'rtyui', 'd', 'a']
listt.sort(key=lambda x: x.count('a'))
print(listt)

#lesson 9

def log_result(fun):
    def wrapper(num):
        result = fun(num)
        print(result)
        return result
    return wrapper


def square(number: int) -> int:
    return number ** 2

square = log_result(square)
square(10)

#task 2

def repeat(fun):
    def wrapper(num, x):
        for i in range(num):
            x = fun(x)
        print(x)
        return x
    return wrapper
def square(number: int) -> int:
    return number ** 2

square = repeat(square)

square(10, 10)

#task 3

def arithmetic(a, b):
    return a / b

def error_catch(fun):
    def wrapper(num_1: int, num_2: int):
        try:
            result = fun(num_1, num_2)
            return result
        except Exception as e:
            print(f'случилась ошибка - {e}')
    return wrapper

arithmetic = error_catch(arithmetic)
print(arithmetic(1, 0))

#task 4

listik = ['ghjgkl', 'kgi', 'f', 'girfbwcdf', 'gfki']
new_listik = [len(i) for i in listik]
print(new_listik)

#task 5

listik = ['apple', 'Banana', 'cherry', 'DATE']
new_listik = [i for i in listik if i.islower()]
print(new_listik)

#task 6

listik = [
    ('Алиса', 23),
    ('Максим', 37),
    ('София', 15),
    ('Артём', 29),
    ('Ева', 31),
    ('Михаил', 18),
    ('Анна', 40),
    ('Даниил', 12),
    ('Мария', 25),
    ('Иван', 34),
]

new_listik = [i for i in listik if i[1] > 18]
print(new_listik)


#task 7

from functools import reduce
listik = [[1,2], [3,4], [5,6]]
new = reduce(lambda x, y: x + y, listik)
print(new)

#task 8

listik = ['mouse', 'dog', 'cat', 'car', 'snake', 'cow']
dictik = {}
dictik = {i[0]: [i] for i in listik}
new_dictik = {dictik[i[0]].append(i) for i in listik if i not in dictik[i[0]]}
print(dictik)

#task 9

inventory = [
    ("яблоки", 85.00, 50),
    ("бананы", 120.50, 30),
    ("молоко", 75.90, 25),
    ("хлеб", 45.00, 40),
    ("яйца", 140.00, 20),
    ("сыр", 320.00, 15),
    ("вода", 30.00, 100),
    ("кофе", 550.00, 8),
    ("печенье", 95.50, 35),
    ("рис", 180.00, 12)
]

sum_list = [['цена на ' + i[0], i[1] * i[2]] for i in inventory]
print(sum_list)


#task classes
#task 1

class SomeOperations():
    def __init__(self, a: int, b: int) -> None:
        self._a = a
        self._b = b
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    def some_summ(self):
        return self._a + self._b

    def maximum(self):
        return max(self._a, self._b)

operatonship = SomeOperations(5, 7)
operatonship.a = 8
print(operatonship.some_summ())

#task 2

class Counter:
    def __init__(self, count = 0):
        self.count = count

    @property
    def coount(self):
        return self.count

    def add(self):
        self.count += 1

    def subtract(self):
        self.count -= 1

new_counter = Counter(10)
new_counter.add()
print(new_counter.count)


#task_3

class Shop:
    def __init__(self, **kwargs):
        self.products_dict = kwargs

    def info(self):
        print(self.products_dict)

    def add_product(self, **product):
        self.products_dict.update(product)

    def products_dict_coast(self, keyy):
        print(f'цена на {keyy} составляет {self.products_dict[keyy]}')

    def delete_product(self, keyy):
        del self.products_dict[keyy]

product_shop = Shop(**{'banana':3.5, 'apple':2, 'milk':3})
product_shop.add_product(**{'bananna':4})
product_shop.info()


#task 4


class MoneyBox:
    def __init__(self, capacity):
        self.__capacity = capacity
        self._coin_count = 0

    @property
    def coin_count(self):
        return self._coin_count

    @coin_count.setter
    def coin_count(self):
        print("you can't")

    @coin_count.deleter
    def coin_count(self):
        print(f'u broke money box and take {self._coin_count} rubles')

    def add_coin(self):
        if self._coin_count < __capacity:
            self._coin_count += 1

    def empty_space(self):
        print(f'u can add {self._coin_count} coins')

pig_money_box = MoneyBox(5)
pig_money_box.add_coin()
pig_money_box.empty_space()



