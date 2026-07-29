# s = "program"

# print("pro" in s)  # True, because "pro" is a substring of "program"
# print("gram" in s)  # True, because "gram" is a substring of    

# print(s[:-1])
# m= input("Enter a string: ")

# if m == m[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# s= input("Enter a string: ")
# print(s.replace(" ", "_"))  # Replaces all spaces in the string with underscores
# the above code checks if the input string is a palindrome and replaces spaces with underscores in the string.

# m= input("Enter a string: ")
# print(m.lower())s
# print(m.isalpha())

# u =0
# l =0
# for i in m:
#     if i.isupper():
#         u +=1
#     elif i.islower():
#         l +=1
# print(f"Number of uppercase letters: {u}")
# print(f"Number of lowercase letters: {l}")
# the above code counts the number of uppercase and lowercase letters in the input string.

# for i in m:
#     if i.isalpha():
#         l +=1
#     elif i.isdigit():
#         u +=1
# print(f"Number of letters: {l}")
# print(f"Number of digits: {u}")
# the above code counts the number of letters and digits in the input string.

# result=" "
# for  i in m:
#     if i not in result:
#         result += i
# print(result)
# THe above code removes duplicate characters from the input string and prints the result.

# s=input("Enter a string: ")
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break/
#the above code finds and prints the first non-repeating character in the input string.

# m=input("Enter a string: ")

# maxx = m[0]
# for i in m:
#     if m.count(i) > s.count(maxx):
#         maxx=i
# print(maxx)
# the above code finds the first non-repeating character and the most frequently occurring character in the input string.

# s1=input("Enter first string: ").lower().replace(" ", "")
# s2=input("Enter second string: ").lower().replace(" ", "")

# if sorted(s1) == sorted(s2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")  
#the above code checks if two input strings are anagrams of each other by comparing their sorted character lists after converting them to lowercase and removing spaces.

# sen= input("Enter a sentence: ")
# print(len(sen.split()))

# world=sen.split()
# longest=" "

# for i in world:
#     if len(i) > len(longest):
#         longest=i
# print(longest)

# password = input("Enter a password: ")
# if (len(password) >= 8 and 
#         any(char.isupper() for char in password) and
#         any(char.islower() for char in password) and
#         any(char.isdigit() for char in password)):
#         print("Password is stronger.")
# else:
#     print("Password is weak.")

# s= input("Enter a string: ").replace("  ", " ")
# print(s[::-1])  # This line prints the reverse of the input string.

n= "🐍"

for i in range(100):
    print(n)