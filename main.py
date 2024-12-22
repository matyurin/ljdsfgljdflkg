result = []

def divider(a, b):
    if a < b:
        raise ValueError("Значення 'a' менше ніж 'b'")
    if b > 100:
        raise IndexError("Значення 'b' більше ніж 100")
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), value)
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Помилка для пари ({key}, {value}): {e}")

print("Результат:", result)






#try:
  #  num = int(input('Введіть число'))
 #   print(10 \ num)
#except ZeroDivisionError:
#    print('Помилка: неможна ділити на нуль')
#except ValueError:
   # print('Помилка:ви ввели не число !')
  #finally:
  #  print('Дякуємо за користування нашим додатком !')