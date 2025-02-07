from datetime import date
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum = ",num1 + num2)
print("Difference = ",num1-num2)
print("Product = ",num1*num2)
print("Quotient = ",num1/num2)


birthYear = int(input("Enter your birth year: "))
print("Your age is :",date.today().year - birthYear)

sentence = input("Enter any sentence :")
print("Your sentence in Uppercase : ",sentence.upper())
print("Your sentence in Lowercase : ",sentence.lower())

input1 = input("Enter any input1 :")
input2 = input("Enter any input2 :")

print("Concatenated input1 and input2 : ",input1 + " " + input2);