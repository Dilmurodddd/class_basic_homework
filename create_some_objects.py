from create_one_attribute import Person

#create an object named "p1" whose name is "Anvar"
#create an object named "p2" whose name is "Shavkat"

def namee(a):
    person = Person(a)
    return person.name

p1 = namee("Anvar")

p2 = namee("Shavkat")

print(p1)
print(p2)