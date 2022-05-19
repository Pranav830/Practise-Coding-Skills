
#Comments are given with hash symbol for a single line comments

"""for multiline comments we can use
 triple quotes
 to understand this"""

"""Print statement by default consists of a newline included in that so every print statement gets printed in the 
new line one after other so if you want to  print it in the same line then we have to give end="" in the end of the 
print statement as shown in the example"""

#So this print statement won't leave a newline after this print so for checking we can add one more print statement under this and both will get printed in the same line
print("Testing print statement newline", end="") #If we specify anything inside end ="123" then 123 will also get printed along with print statement if we give space then it will come inside it
print("Testing print statement new line feature")#So instead of printing these in 2 lines as we have given end = "" we will get both of these printed in the same line

#Escape Sequence is used to print it in new line so whenever a \n is encountered then it will escape it into new line

print("c:\narry") #The output will be arry since \n is considered as escape or new line character
print("c:\nnarry") #To print narry completely we have to give something like this
#\n is used for new line and we have some other escape seq like \t which is used for giving a tab space