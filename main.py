# Here I will go through the course from Udemy. I will use this template here to practice.
# I will also use complete an assignment from Udemy on here.
#Below is a string as it as commas
print("hello world")
#Below is a form of an integer
print(5 + 5)
# Here we are going to look at ways to use the methods we have just learned.
#print is method we can input whatever into it and it will be printed.
print("hello world")
# In order to convert an integer into a string we too do the following below.
x = 5
print(" I am " + str(x))
# Doind this will enable to value x to be icluded in the method we are trying to use without an error.
# if we want to convert the string into an interger we use the same Process.
x = "5"
print(10 + int(x))
# we are going to look at the format method.
age = 5
print("I am " + str(age) + " years old")
# Now the above method is rather long to type out so therefore to make things easier to type out we are going to use the format method. as shown below.
print(" I am {} years old".format(age))
print(" I am {} years old and {} months".format(age, 4))
# format method helps add values to string without all the code.
name = "rolf"
user_name_phrase = print( "hello my name is {}".format(name))

#next example:
item_name = "chair"
item_price = 16
item_details = print("Item name: {}, price: {}".format(item_name,item_price))

# Last example: 
friend_name = "anna"
friend_age = 30
multi_format_phrase = print("Hey {}, are you {age} years old".format(friend_name,age = friend_age))

# we are going to look at input method. 
#input("Enter your age: ")
#user_age = input("Enter your age: ")
#print (int(user_age)* 365 * 24 * 60 * 60)
#seconds =int(user_age)* 365 * 24 * 60 * 60
#print ("You have lived for {} seconds".format(seconds))
#so in the above method we asked the user for there age to determine how long they lived in seconds. We did this by first creating a variable for age and then we created a variable for seconds which included the age variable.

# we are not going to complete the code so the user is simply able to enter the information without adding code. 
# weare going to use def which is going to def the method. 
def age_in_seconds(): 
  user_age = input("Enter your age: ")
  age_seconds = int(user_age)* 365 * 24 * 60 * 60
  print("You have lived for {} seconds".format(age_seconds))
age_in_seconds()

# we are not going to look at the if, elif statements. 
price = 100 
if price <100:
  print ("buy the chair")
else:
  print ("dont buy the chair")
# the if statement helps determin whether the chair user should buy or not, helps filter the options. 

if price <100:
  print ("buy the chair")
elif price == 100:
  print ("you can buy the chair....")
else: 
  print ("dont buy the chair")

# now the elif is just to give another option, == (equal too) and if the amount is not equal too (==) then the else statement will exacute. 
