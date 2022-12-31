dictt={'apple':2,'sbeery':9,'banana':7,'capple':5}
sortedbykey={k:v for k,v in sorted(dictt.items())}
sortedbyval={k:v for k,v in sorted(dictt.items(),key=lambda x :x[1])}
print(sortedbykey)
print(sortedbyval)
print("="*50)

#handling missing key
country={'USA':7,'India':9,'uk':4}
print(country.get('India','notfound'))
print(country.get('japan','notfound'))
print("="*50)

#sum of all items in dict
def returnsum(dict):
    sum=0
    for i in dict:h
        sum=sum+dict[i]
    return sum
dict={'a':100,'b':200,'c':400}
print("sum:",returnsum(dict))
#secondway
def returnsum(dict):
    return sum(dict.values())
dict={'a':100,'b':76,'c':48}
print("sum:",returnsum(dict))
print("="*50)

#merge  dictionaries
d1={'a':10,'b':20,'c':30}
d2={'d':40,'e':50}
d3={'f':60,'g':70}
merged={**d1,**d2,**d3}
print(merged)
print("="*50)

#del an element in dict
d1={"usa":20,"london":56,"india":89,"japan":30}
del d1["london"]
print("updated dictionary:",d1)



































































































































































































































































