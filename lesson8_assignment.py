num_list = []
num = 0
while(num != -999):
    num = int(input("Please enter a number (-999 to quit): "))
    if(num != -999):
        num_list.append(num)
    else:
        break
print("Using the numbers:")
sum = 0
for count in range(len(num_list)):
    print(num_list[count])
    sum = sum + num_list[count]

average = sum / len(num_list)
print("The average is:", average)
