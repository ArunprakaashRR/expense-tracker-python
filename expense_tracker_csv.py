import csv
expenses=[]
while True:

   name=input("enter expense name:")
   amount=float(input("enter amount:"))
   expenses.append((name, amount))
   choice=input("add more?(Y/N):")
   if choice =='n':
       break 
total=0
print("\nExpenses:")
for item in expenses:
   print(item[0],"-",item[1])
   total += item[1]
print("Total spent:",total)

