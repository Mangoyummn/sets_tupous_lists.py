#collection=single "variable" used to store multiple values 
# List = [] ordered and changeable. Duplicates Ok 
#Set= {}unordered and imutable , but add/remove OK . No du-plicates 
#Tuple=() ordered amd unchangeble . Duplicates OK. Faster 

# Fruit= [ " apples", "oranges" ,"bannana","coconut"]
# print (dir (fruits))

# print(help(fruits))
# print (len (fruits))
# print (fruits[0] )
# print ("pineapple" in fruits)

# for x in fruits :
# print (x)

# fruits[1]="pineapple"
#print (fruits [0])
#for fruits.append ("pineapple")
#for fuits.remove ("apple")
#for fruit .insert (0,"pineapple")
#fruits.reverse()
# #fruits.clear ()
# print(fruits)
# # for fruits in fruits;

# cars=["bmw","masserati"," Audi", "mercedes","ferrari"]
# print ( f" these are list of {cars}")
# print (f"the first car is {cars[0']}")
                                
# #changing the value of the list 
# cars[0]="toyota"
# print ( f"the first car is {cars[0]}")

# print (f "the last car is {cars [-1] }")
# cars [-1] = "lamborginah"
# print(f"the first car is {cars[-1]}")

# #adding a new value to the list 
# cars.append ("bugatti")
# print(cars)
# cars.remove ("maseratti")
# print(cars)

# #looping through the list 
# #otherwise called litering through the list 
# for car in cars :
# #print (len(car))
# #print(car)
# #cars=input ("add a new car please :")
# #cars.append (carRequest)
# print(len (cars))
# cars(cars.uppercase())
# print(cars)

# #challenge 
# #create a list of friends

# make sure the initial list is none 
# friends =[]
# #add a new friend to the list , add at least 5 friends 
# #remove a friend 
# #insert a friend at a specefic index mabye 2
# #print the list of friends 
# #loop through the list and print the friends name 
# #see if the particular friend is in the list (boolean value)
# #if the lists greater then 10 break the loop 
# friends = ["natalie","Lucy","lily","natalia" ,"erik"]
# print(friends)
# friends.remove ("natalie")
# friends.apprend ("areil",[3])
# print (friends)

# if "Lucy" in friends :
#     print ("Lucy is in list")

# for friends in friends :
#  print(friends)
#  print(len(friends))>10:
#  break
# print(friends)







# sets = {}
# fruits={"apples","oranges","bananna","coconut"}
# # print (dir(fruits))
# # # print(help(fruits))
# # # print(len(fruits))
# # print("pineapple" in fruits)
# # print(fruits[0]clear) 
# # fruits.add ( "strawberry", "blueberry ")
# print(fruits)

# fruits.remove ("apple") # removes value from list 
# fruits.pop()         # removes randoom value 
# fruits.add ("pineaple") # adds a value 
# fruits.clear()   # gets rid of  it all 



# #Tupous
# fruits=("apples","oranges","bananna","coconut")
# # print (dir(fruits))
# # # print(help(fruits))
# # # print(len(fruits))
# # print (fruits.index ("apples")) 
# print (fruits.count.("coconut"))

# #print(fruits)
# for fruits in fruits:
#     print(fruits)



#dictionaries
# dictionary= a collection of {key :value } pairs 
#            ordered and changeable. no duplicates 
capitals={"USA":"Washington DC", 
          "India":"Delhi" ,
          "China":"Beijing",
          "Russia":"Moscow"}
# print(dir(capitals))
# # print(help(capitals))
# # print(capitals.get("USA"))
# if capitals.get ("China"):
#     print ("That capital exist")
# else:
#     ("That capital doesn't exist")

# capitals.update({"Germany":"Berlin", "Mexico":"mexico city"})

# capitals.update({"USA":"Detriot"})
#  capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# print(capitals)

# keys+capitals.key()
# for key in capital.keys:()
# print(key)

value=capitals.values()
for value in capitals.values():
 print(value)

 items=capitals.items()
 for key, value in capitals.items():
print(f"{key}:{value}")
