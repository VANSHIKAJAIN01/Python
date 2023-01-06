people=[
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Cho","house":"Ravenclaw"},
    {"name":"Draco","house":"Slytherin"},
]

#def f(person):
 #   return person["name"]
#in lambda person is input and person[name] is an outut
people.sort(key=lambda person: person["name"])

print(people)