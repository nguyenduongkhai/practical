
numbers=[3,1,4,1,5,9,2]

numbers[0]=10                #a
numbers[len(numbers)-1]=1    #b
print(numbers)


another_numbers=numbers[2:len(numbers)-1] #c
print(another_numbers)

check_nine=9 in numbers    #d
print(check_nine)