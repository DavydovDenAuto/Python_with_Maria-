def greet_user():
    print("Hello!")


greet_user()
print("New code")


def greet_user(username):
    print(f"Hello, {username.title()}!")


greet_user('jessi')
print("New code")


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')
print("New code")


def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')
print("New code")


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.upper()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("New code: ")


def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
print("New code: ")


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
middle_name = ''
print(bool(middle_name))
middle_name = 'lee'
print(bool(middle_name))
print("New code: ")


def build_person(first_name, last_name):
    first_name = 'John'
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
#получаем словарь на 3 стороны
def get_triangle_sides(a,b,c):
    triangle_sides = {'a':a,'b':b, "c":c}
    return triangle_sides
tr = get_triangle_sides(2,3,5)
print(*tr.values())
print(tr.get('a'))
print(tr.keys())
print(tr.items())

print('New code: ')


def build_person(first_name, last_name, age=27):
    age = 1
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age + 11
    return person


musician = build_person('jimi', 'hendrix', age=None)
print(musician)
age = None
print(bool(age))
age = 27
print(bool(age))
print("New code: ")


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
print("New code: ")


def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


def say_hello(*names):
    for i in names:
        msg = f'Hello, {i.title()}!'
        print(msg)
say_hello('Den', 'Mama')

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print("New code: ")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
print("New code: ")


def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print("New copde: ")


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
