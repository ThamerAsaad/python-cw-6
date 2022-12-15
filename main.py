
# write your code here
person = {
        'name': "thamer",
        'age': 18,
        'hobbies': ["drawing", "Gaming", "walking"]
}

print(person['name'])
print(person['age'])

person['age'] = 19
person['country'] = "Saudi Arabia"


print(person)
print(len(person))

person['hobbies'].append("tennis")

def check_hobbies(person):
    if len(person['hobbies']) > 3:
        print("WOW YOU ARE AMAZING!")

check_hobbies(person)    