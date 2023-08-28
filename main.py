# write your code here
favorite_animals = ["dog" , "cat" , "monkey" , "rabbit"]
print(favorite_animals)
print(favorite_animals[1])

favorite_animals.remove("monkey")

favorite_animals = ["dog" , "cat" , "monkey" , "rabbit"]
for animal in favorite_animals:
    print(f"i love {animal}")
    
numbers = [5,4,3,2,1]    
numbers_sum = 0

for sum in numbers:
    numbers_sum =(sum + numbers_sum)
    
print(numbers_sum)