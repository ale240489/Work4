  

#Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
# степени k.
#Пример:
#если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int(input('Введите максимальную степень многочлена: '))

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
data = open('equation.txt', 'w')  
data.writelines(equationFinish)  
data.close


