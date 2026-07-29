#no =[1,2,3,4,5]
#square = [x*x for x in no]
#print(square)


# even = [x for x in range(1,20) if x%2==0 ]
# print(even)

# odd = [x for x in range(1,20) if x%2!=0 ]
# print(odd)

# cube= [x**3 for x in range(1,11)]
# print(cube)

# print(len(cube))

# name=["sachin","dhoni","kohli","rohit"]
# print([len(x) for x in name])



# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(f"{a//b} {a/b}")


if __name__ == '__main__':
    n = int(input())
    
    # range(1, n + 1) generates numbers 1 to n
    # '*' unpacks them as individual items
    # 'sep=", "' connects them with commas
    print(*range( 1,n + 1))
