import re
#by using parenthesis we can create multiple groups within a single regular expression
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My number is 415-555-4242')
#the below line of code will print just the first 3 digits - what was included in group 1 when
#we created the phoneNumRegEx
print(matchObject.group(1))
print(len(matchObject.group(2)))

#you can use the pipe object to match one of several patterns

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

