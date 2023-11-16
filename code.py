def common_prefix(strings):#creating a function for common prefix
    if not strings:
        return ""

    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix#returing to the prefix

def main():#creating a main function
    n = int(input("Enter the number of strings: "))
    strings = [] #creating a set list to store the data given by the user
    for i in range(n):
        string = input(f"Enter string {i + 1}: ")
        strings.append(string)

    result = common_prefix(strings)
    if result:
        print(f"Longest common prefix is: {result}")
    else:
        print("There is no common prefix.")

if __name__ == "__main__":
    main()
