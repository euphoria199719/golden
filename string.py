txt="there is NO Planet B"
capitalize=txt.capitalize()
print(capitalize)
casefold=txt.casefold()
print(casefold)
center=txt.center(7)
print(center)
count=txt.count("e")
print(count)
encode=txt.encode()
print(encode)
endswith=txt.endswith("")
print(endswith)
txt1="H\te\tl\tl\to"
expandtab=txt1.expandtabs(4)
expandtab2=txt1.expandtabs()
print(expandtab)
print(expandtab2)
txt2="Hello Army,Welcome to Magic Shop"
find=txt2.find("Army")
print(find)
age=27
txt3="My name is V, I am {}"
print(txt3.format(age))
quantity=2
itemno=50
cost=700
myorder="I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,cost))
myorder="I want {2} pieces of item {0} for {1} dollars"
print(myorder.format(quantity,itemno,cost))
index=txt2.index("Magic")
print(index)
txt4="Bangtan7"
isalnum=txt4.isalnum()
print(isalnum)
isalnum=txt3.isalnum()
print(isalnum)
txt5="BIGHIT"
isalpha=txt5.isalpha()
print(isalpha)
isdecimal=txt4.isdecimal()
print(isdecimal)
txt6="7"
isdecimal=txt6.isdecimal()
print(isdecimal)
isdigit=txt6.isdigit()
print(isdigit)
isidentifier=txt4.isidentifier()
print(isidentifier)
isidentifier=txt.isidentifier()
print(isidentifier)
islower=txt2.islower()
print(islower)
isnumeric=txt.isnumeric()
print(isnumeric)
isprintable=txt.isprintable()
print(isprintable)
txt7=" "
isspace=txt7.isspace()
print(isspace)
istitle=txt.istitle()
print(istitle)
isupper=txt5.isupper()
print(isupper)
mytuple=("v","min","kook")
join="#".join(mytuple)
print(join)
ljust=txt4.ljust(20,"5")
print(ljust)
lower=txt5.lower()
print(lower)
lstrip=txt5.lstrip()
print("Hybe labels is previous known as ",lstrip," since 2013")
txt8="hello,Bam"
mytable=str.maketrans("B","J")
print(txt8.translate(mytable))
partition=txt2.partition("welcome")
print(partition)
replace=txt2.replace("Fans","army")
print(replace)
upper=txt2.upper()
print(upper)
swapcase=txt2.swapcase()
print(swapcase)
strip=txt2.strip()
print(strip)

