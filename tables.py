num = int(input("Enter any number for the multiplication table: "))
print("The multiplication table for " + str(num) + " is ")
for i in range(1,13):
        print(num, 'x' , i, '=' ,num*i)
         
