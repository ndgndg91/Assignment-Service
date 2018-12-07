file = open('test.txt', 'r')
string = file.read()
# print(string)
# print(len(string))
t_count = string.count('T')
a_count = string.count('A')
g_count = string.count('G')
c_count = string.count('C')
print('0칸씩 띄웠을 경우 - A의 개수 :', a_count, 'C의 개수 :', c_count, 'G의 개수 :', g_count, 'T의 개수 :', t_count)
a_count = 0
c_count = 0
g_count = 0
t_count = 0
for i in range(0, len(string), 2):
    if string[i] == 'A':
        a_count += 1
    elif string[i] == 'C':
        c_count += 1
    elif string[i] == 'G':
        g_count += 1
    elif string[i] == 'T':
        t_count += 1
print('1칸씩 띄웠을 경우 - A의 개수 :', a_count, 'C의 개수 :', c_count, 'G의 개수 :', g_count, 'T의 개수 :', t_count)
a_count = 0
c_count = 0
g_count = 0
t_count = 0
for i in range(0, len(string), 3):
    if string[i] == 'A':
        a_count += 1
    elif string[i] == 'C':
        c_count += 1
    elif string[i] == 'G':
        g_count += 1
    elif string[i] == 'T':
        t_count += 1
print('2칸씩 띄웠을 경우 - A의 개수 :', a_count, 'C의 개수 :', c_count, 'G의 개수 :', g_count, 'T의 개수 :', t_count)
a_count = 0
c_count = 0
g_count = 0
t_count = 0
for i in range(0, len(string), 4):
    if string[i] == 'A':
        a_count += 1
    elif string[i] == 'C':
        c_count += 1
    elif string[i] == 'G':
        g_count += 1
    elif string[i] == 'T':
        t_count += 1
print('3칸씩 띄웠을 경우 - A의 개수 :', a_count, 'C의 개수 :', c_count, 'G의 개수 :', g_count, 'T의 개수 :', t_count)

file.close()