from create_two_attribute import Person

#create an object named "person" whose name is "Ali", age is "25"




def namee(name, age):
    person = Person(name,age)
    return person.name, person.age

p1 = namee("Anvar",25)

p2 = namee("Shavkat",35)

print(p1)
print(p2)