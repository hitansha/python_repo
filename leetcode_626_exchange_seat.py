'''
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?

 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
'''

#python 

student=[[1,'a'],[2,'b'],[3,'c'],[4,'d'],[5,'e']]

print("old order :",student)
total=len(student)
f=False
if total%2!=0:
    total-=1
    f=True
#print(total)
for i in range(0,total,2):
    b1,b2=student[i],student[i+1]
    b1[1],b2[1]=b2[1],b1[1]
#print(f)
if f:
   # print("yes")
    pass
    
print("new order : ",student)