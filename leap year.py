start = int(input('what year do you want to start with ? '))
num_years = int(input('how many years do you want to check ? '))
end_year = int(start + num_years)   #added the 2 values to get the range


for year in range(start,end_year+1):
    if year % 4 == 0 and year % 100 !=0 or year %400 == 0:
        print(year, " is a leap year")
        

    else:
        print(year, " is not a leap year ")


    
    
