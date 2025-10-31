ages=[18,21,45,35,50,65,75,80] #list()
#finding minimum age
min_age=ages[0]
for i in range(1,len(ages)):
    if ages[i]<min_age:
        min_age=ages[i]
#finding average age
sum_of_ages=sum(ages)
average=sum_of_ages/len(ages)
print(ages)
print(min_age)
print(average)
salaries=[]
salaries.append(33000)
salaries.append(70000)
salaries.append(100000)
salaries.append(150000)
salaries.append(200000)
salaries.append(250000)
print(salaries)
#to remove last salary
salaries.pop()
print(salaries)
#t remove salary based on index
salaries.pop(0)
del salaries[1]
salaries.remove(150000)
print(salaries)
#searching value
search=70000
I=0
search_index=-1

for k in salaries:
    if k==search:
        search_index=I
        break
    I+=1
print(search_index)
