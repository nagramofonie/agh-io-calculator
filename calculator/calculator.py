import math

'''class Calculator:
   def __init__(self, op1: float, op2: float):
       self.op1 = op1
       self.op2 = op2

   def sum(self):
       return self.op1 + self.op2

   def substract(self):
       return self.op1 - self.op2

   def multiply(self):
       return self.op1 * self.op2

   def devide(self):
       if self.op2 == 0:
           return 0

       return self.op1 / self.op2'''

class Calculator:
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self):
        return self.__op1 + self.__op2

    def substract(self):
        return self.__op1 - self.__op2

    def multiply(self):
        return self.__op1 * self.__op2

    def devide(self):
        if self.__op2 == 0:
            return "Error: Zero division"

        return self.__op1 / self.__op2



# W pythonie nie ma zmiennych prywatnych. Jest tylko konwencja. Do oznaczenia "prywatnych" zmiennych dodajemy prefix '_'
# przed nazwą zmiennej, np. _op1
# Podwójne podkreślenie '__' chroni przed przypadkowym nadpisaniem w klasach dziedziczących
