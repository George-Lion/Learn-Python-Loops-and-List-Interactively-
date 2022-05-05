people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_List = []
    for value in people:
        if value == person_name:
            value.remove(person_name)
            print(value)
       

print(deletePerson("daniella"))
""" print(deletePerson("juan"))
print(deletePerson("emilio"))  """