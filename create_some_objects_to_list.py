from create_one_attribute import Person

#Create an object named "p1" whose name is "Anvar"
#Create an object named "p2" whose name is "Shavkat"
#Create an object named "p3" whose name is "Jasur"

#Add these objects to the "persons" named list

def namee(a):
    persons = Person(a)
    return persons.name

p1 = namee(["Ali","Shavkat","Jasur"])

print(p1)