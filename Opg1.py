
templist = ['p', 'r', 'o', 'b', 'e']
# list with mixed data types
templist2 = [1, "Hello", 3.4]
# nested list
templist3 = ["mouse", [8, 4, 6], ['a']]
print("----------List------------")

print(templist[0])
print(templist[1:3])
print(templist3[1][2])
templist[0] = "a"
print(templist)
templist[1:4] = ["b","c","d"]
print(templist)
templist.remove("b")
print(templist)
print(templist.pop(1))
print(templist)
#list comp
listcomp = [3 ** x for x in range(10)]
print(listcomp)

drinks = ["cola","faxe","beer","water"]
for drinks in ["faxe", "beer"]:
        print("jeg kunne godt en ", drinks)
print("-----------Tuples-----------")

#Tuples

extuple = ()

extuple = "lets go", 6, 5.3
gg = (1,2,3)
ff = (4,5,6)
print(extuple)
a, b, c = extuple
print(a)
print(b)
print(c)
print(extuple * 3)
print(gg + ff)
dd = gg + ff
print(dd)
print("-----------Set-----------")

# set
myset = {2,3,1}
myset2 = {5,6,4}
tempset = set()
print(type(tempset))
print(myset)
tempmyset = {2,3,1,4,6}
tempset.discard(8)
#tempmyset.remove(8)
a = {2,3,1,4,5}
b = {5,6,4,7,8}
#union
print(a|b)
print(a.union(b))
#intersection
print(a&b)
print(a.intersection(b))
#diff
print(a-b)
print(b.difference(a))
#symdif
print(a^b)
print(a.symmetric_difference(b))
#Set comp
setcomp = {s*2 for s in range(10)}
print(setcomp)
# Dictionary
print("-----------Dictionary-----------")

exdict = {1:"kage",2:"cola","pause": "pølse"}
print(exdict['pause'])
exdict['nummer'] = 44224422
print(exdict)
print(exdict.popitem())
print(exdict)
# Dictionary Comprehension
dictcom = {x: x*x for x in range(10)}

print(dictcom)
