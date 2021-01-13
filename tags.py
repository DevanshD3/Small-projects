tags = []
tag = ''
hashtags = []
# type . to stop the loop
while (tag != '.'):
    tag = input()
    tags.append(tag)
tags.remove('.')
print()
print("Use this for your tags")
print(*tags, sep=',')

for tag in tags:
    tag = str(tag).replace(' ', '')
    hashtags.append(tag)

hashtags = ["#" + hasht for hasht in hashtags]

print()
print("Use this as hashtags")
print(*hashtags, sep=' ')
