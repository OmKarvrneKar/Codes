# This file demonstrates regular expressions in Python
import re


string=input("Enter a string: ")
val=input("Enter a value to search: ")
result=re.search(val,string) 
result1=re.match(val,string)
result2=re.findall(val,string)


if result1 and result:
    print("Match found")
else:   
    print("Match not found")


text="the like ,12121pyhton programing"
result4= re.sub("pyhton","java",text)
print(result4)

result5=re.split("[:,]",text) # this will split the text into a list of substrings using either a colon or a comma as the delimiter.
print(result5)
result6=re.findall(r'\d+',text) #this will find all the digits in the text and return them as a list of strings.
print(result6)

data="contact: abc123@gmail.com"
email =re.findall(r'\S+@+\S+',data)  # \S+
print(email) # this will find the email address in the data string and return it as a list of strings.

Mobile="82174100475"
if re.fullmatch(r'\d{10}', Mobile) :
    print("valid no")
else: 
    print("not valid")

text= "python java c11"
worlds=re.findall(r'\w',text)
print(worlds)
#==========================