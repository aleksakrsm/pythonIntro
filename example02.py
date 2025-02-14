# count number of apperances of each word in txt
import copy
from collections import defaultdict
import datetime
import re

txt = "hej   OVO ovo Ovo   Ova   ohdhd hakf hakf hakf  ahhd ovo aaa ova  aaa ovo "
mapa = {}
for word in txt.split(" "):
    word = word.strip()

    if word == "":
        continue

    word = word.lower()

    if word in mapa:
        mapa[word] += 1
    else:
        mapa[word] = 1

# sorted_keys_in_list = sorted(mapa.keys(), key=lambda x: mapa.get(x), reverse=True)

sorted_list_of_items = sorted(mapa.items(), key=lambda x: x[1], reverse=True)
sorted_map = dict(sorted_list_of_items)

print(mapa)
print(sorted_map)

a = [print(word) for word in ["kiwi", "jabuka", "banana"]]
print(a)

b = [word + " !" for word in ["kiwi", "jabuka", "banana", "lubenica", "avokado"]]
print(b)

# b.sort()
# print(b)

# b.reverse()
# print(b)

# b.sort(reverse=True)
# print(b)

# pointer
# c=b
# print(c)
# b.append("mandarina")
# print(c)

d = b.copy()
e = list(b)

f = b[:]
print(f)

# join
b_f = b + f
print(b_f)
b_f.extend(f)
print(b_f)

id = "01"
jmbg = "2106999000000"
info = f"Student id is {id}, jmbg is {jmbg}"
print(info)
# help({3,4})

#     TUPLES

tuple = (1, 2, 3)
print(tuple)
# tuple[-1] = 33
print(tuple)
# del tuple

tuple2 = (11, 22, 33)
tuple = tuple + tuple2
print(tuple)

fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)

fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)

# bad python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

tuple1 = (1, 2, 3)
tuple1 = tuple1 * 2
print(tuple1)

#  SETs

myset = {'apple', 'banana', 'cherry'}
myset.add("lemon")
print(myset)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
fruits.remove("banana")
# fruits.remove("banana") -> will throw an error if value doen not exist
fruits.discard("mango")
fruits.discard("mango")
print(fruits)
fruits.clear()
print(fruits)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = set1.union(set2)
set4 = {"a", "b", "c"}

set5 = set1 | set2 | set3 | set4
print(set5)

# DICTIONARIES

x = {'type': 'fruit', 'name': 'banana'}
x['type'] = 'berry'
print(x)
print(x.items())

x.update({'name': 'apple'})
x.update({'color': 'red'})
print(x)

y = x.copy()
print(y)

a = {'name': 'John', 'age': 20}
b = {'name': 'May', 'age': 23}
customers = {'c1': a, 'c2': b}
for x, obj in customers.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])

a = 2
b = 5
print("YES") if a == b else print("NO")

dictionary = dict({"david": 3, "tamara": 1, "aleksa": 7, "marija": 2})
###### for key, value in dictionary.items(): to je iteritems
for key, value in dictionary.items():
    print(key, " ---> ", value)

names = ["Aleksa", "David", "Todor"]
names = ["Aleksa", "David", "Todor", "Tamara"]
color = ["r", "g", "b"]

ziped = zip(names, color)
print(ziped)
print(*ziped)
dict_from_ziped = dict(zip(names, color))
print(dict_from_ziped)

colors = ["red", "green", "blue", "red", "red", "orange", "grey"]
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)

d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)


# If you do not know the number of arguments that will be passed into your function,
# there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("a", "b", "c", "d", "e", "f")


# If you do not know the number of KEYWORD arguments that will be passed into your function,
# there is a prefix you can add in the function definition, which prefix?
def my_function2(**kid):
    print("His first name is " + kid["arg1"])


my_function2(arg1="todor", arg2="viktor")

#     LAMBDAs

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))

string = "Anavolimilovana"
print(string[::-1])

x = datetime.datetime
print(x.now())

x = datetime.datetime.now()
print(x.day)
print(x.month)
print(x.year)
print(x.strftime('%A')) #ovo ? ? ?
print(x.strftime('%M'))
print(x.strftime('%B'))
# print(x.strftime('%N'))

x = datetime.datetime(2024, 8, 20)
print(x.strftime('%d'))

txt = 'The rain in Spain'
x = re.findall('[a-c]', txt)
print(x)

x = re.search('a', txt)
print(x.start())
print(x.start())

txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start())

x = re.search("^The.*Spain$", txt)

print(x)
print(x.start())
if x:
  print("YES! We have a match!")
else:
  print("No match")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

price = 100
txt = f"It is {'perfect' if price == 100 else 'ok'}"
print(txt)

# f = open('demofile.txt', 'w')
# f = open('demofile.txt', 'x')
# x = open('demofile.txt', 'b')