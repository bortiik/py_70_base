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



