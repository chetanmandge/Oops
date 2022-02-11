''' forword pattern
*
**
***
****
*****'''
for i in range(1, 5):
    for j in range(i,5):
        print(" ", end=' ')
    for k in range( i):
        print("*", end=' ')
    print(" ")

for i in range(5, 0,-1):
    for j in range(i,5):
        print(" ", end=' ')
    for k in range(i):
        print("*", end=' ')
    print(" ")
''' reverse pattern 
*****
****
***
**
*
'''
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end='')
#     print()
# i=0
# while(i<=5):
#     for j in range(1,i+1):
#         print("*",end='')
#     i+=1
#     print()
'''If combine both pattern we get below pattern 
* 
** 
*** 
**** 
*****
****
***
**
*'''