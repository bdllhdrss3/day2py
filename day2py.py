from collections import Counter 
string = input("enter any word or phrase : ") #for entering in the word
vowels = "aeiouAEIOU"
#now craeting a variable and list of those vowels from the list

str = [ letter for letter in vowels if letter in string]
str2 = ''.join(str)

#now creating that loop and variables which will store number of duplicates in the strings

dup = Counter(string)
dup2 = [value for value in dup.values() if value > 1 ]
dup3=len(dup2)


#now we create the final print function to print out the vowels in the string and the number of the duplicates in a tuple
print((str2,dup3))
