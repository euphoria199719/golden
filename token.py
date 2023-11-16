x=input("Enter a string:")#take input from user
a=x.split(" ")#splitting string into a list
for i in range(len(a)):#allows to access or iterate across the list using its index
    k=a[i]#reversing each word
    k=k[::-1]
    a[i]=k
a[0]=a[0].capitalize()#formatting the first word using index
b=" ".join(a)#creating a new string by concatination
print(b)#print the final output string