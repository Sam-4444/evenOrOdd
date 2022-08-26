# get the user input and check if it is valid
try:
        a=input("enter a number : ")
        a=int(a)
except:
        print(a," : is not a digit !")
        exit()

# check it is odd or even
def even_odd():
  global a
  if a%2==0:
        print(a," : is even ")
  else:
        print(a," : is odd ")


even_odd()