# Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.

import random
k = int(input('Введите максимальную степень многочлена: '))
#Создание многочленов
def equation(k):
    equation = []
    for i in range(k):
        a = random.randint(0,100)
        b = random.randint(0,100)
        if k != 1 and a==1:
            equation.append(f'x^{k} + ')
            k -= 1
        elif k != 1 and a==0:
            k -= 1    
        elif k != 1:
            equation.append(f'{a}*x^{k} + ')
            k -= 1
        elif k == 1 and a==1:
              equation.append(f'{a} + {b} = 0')  
              k -= 1     
        elif k == 1 and a!= 0:
              equation.append(f'{a}*x + {b} = 0')  
              k -= 1
        elif k == 1 and a==0:
              equation.append(f'{b} = 0')  
              k -= 1                  
    return equation


equationFinish = ','.join(equation(k)).replace(',','')
equationFinish2 = ','.join(equation(k)).replace(',','')
#Создание файлов
data = open('equation.txt', 'w')  
data.writelines(equationFinish)  
data.close
data = open('equation2.txt', 'w')  
data.writelines(equationFinish2)  
data.close 
#Считывание файлов
data = open('equation.txt', 'r')  
for line in data:
    file1 = line 
data.close
data = open('equation2.txt', 'r')  
for line in data:
    file2 = line  
data.close
#Создание строчной записи фалов и их редактирование
file1 = file1.replace(' ','').replace('=0','').split('+')
file2 = file2.replace(' ','').replace('=0','').split('+')

dict_file1 = {}
dict_file2 = {}
finish = {}

index = 0
index2 = 0
#Создание словаря по файлу 1
for i in range(len(file1)-1,-1,-1):
    if i > 1:
        i = int(file1[index].split('^')[1])
        if file1[index].startswith('x'):
            dict_file1[i] = 1
            index+=1
        else:
            dict_file1[i] = file1[index].split('*')[0]
            index+=1

    if i == 1:
        if '^' in file1[index]:
            i = int(file1[index].split('^')[1])
        if 'x' in file1[index]:
            dict_file1[i] = file1[index].split('*')[0]
            index+=1  
    if i == 0:
        dict_file1[i] = file1[index]
        index+=1 

#Создание словаря по файлу 2

for i in range(len(file2)-1,-1,-1):
    if i > 1:
        i = int(file2[index2].split('^')[1])
        if file2[index2].startswith('x'):
            dict_file2[i] = 1
            index2+=1
        else:
            dict_file2[i] = file2[index2].split('*')[0]
            index2+=1

    if i == 1:
        if '^' in file2[index2]:
            i = int(file2[index2].split('^')[1])
        if 'x' in file2[index2]:
            dict_file2[i] = file2[index2].split('*')[0]
            index2+=1  
    if i == 0:
        dict_file2[i] = file2[index2]
        index2+=1



#Создание итогового словаря
if len(dict_file1) >= len(dict_file2):
    for i in range(len(dict_file1)-1, -1, -1):
        key = i
        #print(key)
        for x in dict_file2.keys():
        
            if key in dict_file2.keys():
                if key == x:
                    finish[i] = int(dict_file1.get(i)) + int(dict_file2.get(x))
            else:
                finish[i] = dict_file1.get(i) 
if len(dict_file2) > len(dict_file1):
     for i in range(len(dict_file2)-1, -1, -1):
        key = i
        #print(key)
        for x in dict_file1.keys():
            if key in dict_file1.keys():
                if key == x:
                    finish[i] = int(dict_file2.get(i)) + int(dict_file1.get(x))
            else:
                finish[i] = dict_file2.get(i)
                               
#Создание итогового списка на основе итогового словаря
arrayFinal = []
for a in range(len(finish)-1, -1, -1):
    if a != 1 and a != 0:
        arrayFinal.append(f'{finish.get(a)}x^{a} +')
    elif a == 1:
        arrayFinal.append(f'{finish.get(a)}x +')
    else:
        arrayFinal.append(f'{finish.get(a)} = 0')

equationSuperrrFinish = ','.join(arrayFinal).replace(',','') 
data = open('equationSuperrrrFinish.txt', 'w')  
data.writelines(equationSuperrrFinish)  
data.close       
                        
#print(file1)
#print(file2)        
print(dict_file1)
print(dict_file2)
#print(finish)
print(equationSuperrrFinish) 