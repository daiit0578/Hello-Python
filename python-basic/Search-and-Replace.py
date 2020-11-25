import re

phone = '095-567-789'

num = re.sub('5','2',phone)
print(num)