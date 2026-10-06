#list comprehension
#Every list comprehension can be re-written as a for-loop.  But every for-loop cannot be re-written in list comprehension.
'''a=["python","Java","dsa"]'''
#["PYTHON","JAVA","DSA"]
#print(a.upper()) not possible because in list we don't have upper() method
'''for i in a:
    print(i.upper(),end=" ")'''#output: PYTHON JAVA DSA but want ["PYTHON", "JAVA", "DSA"]
'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#list comprehension syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

'''b=["apple","mango"]
c=[i.capitalize() for i in b]
print(c)'''

'''a=[1,2,3,5,6,8,12,13]
#[1,4,9,25,36,64,144,169]
b=[i*i for i in a]
print(b)'''

'''b=[i for i in range(21)]
print(b)'''

'''b=[i for i in range(16) if(i%2==0)]
print(b)'''

'''b=[i*i for i in range(31) if(i%2==0)]
print(b)'''

'''a=["grapes","berry","mango","kiwi","dragon","apple"]
b=[i for i in a if "a" in i]
print(b)'''

'''a=["grapes","berry","mango","kiwi","dragon","apple"]
b=[i for i in a if "a" not in i]
print(b)'''

#no-elif usage in list-comprehension
#if-else usage in list-comprehension
'''a=[i*i if(i%2==0)else i*5 for i in range(21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''





