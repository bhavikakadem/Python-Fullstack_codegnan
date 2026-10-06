#patterns
#right triangle
'''n=int(input())
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()'''

#inverted right triangle
'''n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()'''

#square pattern
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''

#pyramid pattern
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
