# below is a list of my favorite hobbies
print("Some of my favorite hobbies are:")
hobbies = ['reading', 'swimming', 'coding', 'art']
for hobby in hobbies:
    print(hobby.title())
    
# use append to add to list
hobbies.append('board games')
print(hobbies)
for hobby in hobbies:
    print(hobby.title())

# use pop to remove items from list
hobbies = ['reading', 'swimming', 'coding', 'art', 'board games']
popped_hobbies = hobbies.pop()
print("I removed: " + popped_hobbies)
print(hobbies)

# use sort to alphabetize a list:
hobbies = ['reading', 'swimming', 'coding', 'art', 'board games']
hobbies.sort()
print(hobbies)
print("Here is an alphabetized list:")
for hobby in hobbies:
    print(hobby.title())