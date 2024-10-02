print("введите два числа для их сравнения")
num1=input("Первое число:")
num2=input("Второе число:")
num = num1 if num1<num2 else num2 
if num1==num2 :
    print("Числа равны")
else:
    print("Наименьшее число:", num)
    
