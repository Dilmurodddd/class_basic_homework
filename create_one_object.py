from create_one_attribute import Person

def namee(a):
    person = Person(a)
    return person.name

ali = namee("Ali")
print(ali)
#create an object named "person" whose name is "Ali"