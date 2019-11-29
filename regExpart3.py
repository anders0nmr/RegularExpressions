import re
# question mark says match 0 or 1 times
batRegEx = re.compile(r'Bat(wo)?man')
mo = batRegEx.search('The adventures of Batman')
print(mo.group())
mo = batRegEx.search('The adventures of Matt')
mo == None
print(mo)