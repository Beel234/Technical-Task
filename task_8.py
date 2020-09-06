number = input("Enter number") #User enters number
numbers = [str(i) for i in range(int(number)+1)]
count = 0
number_with_3 =[]
for i in numbers:
  if len(i) ==1:
    if i[0] == '3':
      count = count+1
      number_with_3.append(i)
  if len(i) == 2:
    if i[0] == '3':
      count = count+1
      number_with_3.append(i)
    if i[1] == '3':
      count = count+1
      number_with_3.append(i)
  if len(i) == 3:
    if i[0] == '3':
      count = count+1
      number_with_3.append(i)
    if i[1] == '3':
      count = count+1
      number_with_3.append(i)
    if i[2] == '3':
      count = count+1
      number_with_3.append(i)
threes = {'count':count,'numbers':set(number_with_3)}
print(threes)