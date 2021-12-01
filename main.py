import os



number_a = float(input("Число A - "))
if number_a % 1 == 0:
  number_a = int(number_a)
else:
  number_a = float(number_a)



number_b = float(input("Число B - "))
if number_b % 1 == 0:
  number_b = int(number_b)
else:
  number_b = float(number_b)


class MyMath:

  def __init__(self, number_a, number_b):
    self.number_a = number_a
    self.number_b = number_b
  
    pass

  def addition(self):
    print("Cумма - " ,self.number_a + self.number_b)
  
  def multiplication (self):
    umn = self.number_a * self.number_b
    if umn % 1 == 0:
      umn = int(umn)
    else:
      umn = float(umn)
    print("Умножение - " , umn)

  def division (self):
    if self.number_b == 0:
      print("Делить на 0 нельзя!")
    else:
      umn3 = self.number_a / self.number_b
      if umn3 % 1 == 0:
        umn3 = int(umn3)
      else:
        umn3 = float(umn3)
      print("Деление - " ,umn3)

  def subtraction (self):
    print("Вычитание - " ,self.number_a - self.number_b)
  
  def pow (self):
    print("Возведение в степень - " ,self.number_a ** self.number_b)

  def sqrt_a (self):
    if self.number_a < 0:
      print("Невозможно")
    else:
      umn1 = self.number_a ** (0.5)
      if umn1 % 1 == 0:
        umn1 = int(umn1)
      else:
        umn1 = float(umn1)
      print("Корень из A - " ,umn1)
  
  def sqrt_b (self):
    if self.number_b < 0:
      print("Невозможно")
    else:
      umn2 = self.number_b ** (0.5)
      if umn2 % 1 == 0:
        umn2 = int(umn2)
      else:
        umn2 = float(umn2)
      print("Корень из B - " ,umn2)


chislo = MyMath(number_a ,number_b)


while True:
  print("-" * 22)
  print("Число A:", number_a , "Число B:", number_b)
  print("Команды:")
  print("1 - Cумма")
  print("2 - Умножение")
  print("3 - Деление")
  print("4 - Вычитание")
  print("5 - Возведение в степень")
  print("6 - Корень из A")
  print("7 - Корень из B")
  print("8 - Ввод новых чисел")
  print("9 - Выход")
  print("-" * 22)
  choice = input()
  os.system('clear')
  if choice == "1":
    chislo.addition()
  elif choice == "2":
    chislo.multiplication()
  elif choice == "3":
    chislo.division()
  elif choice == "4":
    chislo.subtraction()
  elif choice == "5":
    chislo.pow()
  elif choice == "6":
    chislo.sqrt_a()
  elif choice == "7":
    chislo.sqrt_b()  
  elif choice == '9':
    print("Пока!")
    break
  elif choice == '8':
    number_a = float(input("Число A - "))
    if number_a % 1 == 0:
      number_a = int(number_a)
    else:
      number_a = float(number_a)
    number_b = float(input("Число B - "))
    if number_b % 1 == 0:
      number_b = int(number_b)
    else:
      number_b = float(number_b)
  else:
    print('Повтори :( ')

  



