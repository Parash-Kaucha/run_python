str1 = "hello emma, emma is out of the way. emma is waiting for you."
count = 0

if "emma" in str1:
    count = count + 1

print(count)
# print(str1.index("emma"))
print(str1.split().index("emma"))