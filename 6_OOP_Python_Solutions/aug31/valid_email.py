import re
print("Enter a email address")
y = input()
m = re.match(r'[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}', y)
if m:
    print("Valid")
else:
    print("Invalid")
