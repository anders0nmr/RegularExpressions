#Regular expressions are great ways to recognize patterns quickly
#to use regex must import re first
import re

message = 'Call me 415-555-1011 tomorrow or at 415-555-9999'

#create phoneNumber regex
#syntax below says we're looking for 3 digits a dash 3 more digits a dash and 4 digits
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumRegex.search(message)
#Will print first occurence of string that matches the pattern
print(matchObject.group())

#findall will find every occurence of pattern
findAll = phoneNumRegex.findall(message)
#print out list of all numbers that match what we're looking for
print(findAll)

#Regular expressions are a mini-language for specifying text patterns