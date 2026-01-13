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
#heyy
#neww
#vot tak