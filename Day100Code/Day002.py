# Day002 - 07/09/2026

# Beginner - Understanding Data Types and How to manipulate Strings

# Subscripting and Slicing

# print("Hello"[0]) # H
# print("Hello"[4]) # o
# print("Hello"[0:3]) # Hel
# print("Hello"[1:4]) # ell 

# # String 

# print("233" + "456") # 233456

# # interger

# print(233 + 456) # 689  

# # large number

# print(123_456_789) # 123456789

# # float = Floating point number

# print(3.14159) # 3.14159

# # boolean

# print(True) # True
# print(False) # False

# --------------------------------------------------------------------

# len("12345") # a função len() retorna o tamanho da string, 
# no caso 5 ela não conta o número 12345 e sim a quantidade de caracteres 
# que tem na string, no caso 5.

# len(12345) TypeError: object of type 'int' has no len()

# print(type(12345)) # <class 'int'>
# print(type(3.14159)) # <class 'float'>
# print(type(True)) # <class 'bool'>
# print(type("Hello")) # <class 'str'>
# print(type(len("Hello"))) # <class 'int'>
# print(type(70 + float("100.5"))) # <class 'float'>
# print(type(str(70) + str(100))) # <class 'str'>

# print(int("90") + int("100")) # 190

# Tipo de função de conversão de dados:

# int()
# float()
# str()
# bool()

# --------------------------------------------------------------------

# nome = input("Qual é o seu nome? ")
# tamanho = len(nome)
# print(tamanho)

# print(type(tamanho)) # <class 'int'>
# print("Número de caracteres do seu nome é: " + str(tamanho))

# --------------------------------------------------------------------

# print("My age:" + str(456))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(6 / 3)
# print(6 // 3) # a divisão com duas // a sainda é um número inteiro
# print(2 ** 3)

# ()
# **
# * or /
# + or -

# print(3 * (3 + 3) / 3 - 3)

# --------------------------------------------------------------------

# BMI Calculator
# The body mass index (BMI) is a measure used 
# in medicine to see if someone is underweight or 
# overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

# height = 1.65 
# weight = 84


# Write your code here.
# Calculate the bmi using weight and height.
# bmi = (weight / (height ** 2))

# print(bmi)