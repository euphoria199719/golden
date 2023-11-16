nums=[]#creating a list to store the elements
print("Enter 10 nos(in ascending order):")#take input from user
for i in range(10):#range returns a sequence of values and prints the element in a new line
    nums.insert(i,int(input()))#to insert an element into list
print("Enter a number to search:")
search=int(input())#using search an element
first=0
last=9
middle=(first+last)/2
middle=int(middle)
while first<=last:#checking the value of the element for meeting the conditions
    if nums[middle]<search:
        first=middle+1# indexing starts with 0
    elif nums[middle]==search:
            print("The number found at position:")#printing the result
            print(middle+1)
            break#if the above conditions pass stop the loop
    else:
        last=middle-1
    middle=(first+last)/2
    middle=int(middle)
if first>last:#if the above conditions fail execute this statement
        print("The number is  not found in list")