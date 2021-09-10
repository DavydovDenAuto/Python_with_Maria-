print("Hello Python world!")
message = "Hello Python world!"
print(message)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[0].title())
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
print("--------------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(3, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
print("------------------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(0)
print(popped_motorcycle)
print(motorcycles)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
print(type(dimensions))
# dict
alien_0 = {'color': 'green', 'points': 5}
for key in alien_0:
    print(key)
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
print("--------------------------------------------------")
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key in user_0:
    print(key)
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print(favorite_languages.items())
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():
    print(name.title())
for language in favorite_languages.values():
    print(language.title())
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
print(aliens)
for alien in aliens:
    print(alien)
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']

    }
print(pizza)
print(f"You ordered a {pizza['crust']}-crust pizza ")
print(pizza['toppings'])
for topping in pizza['toppings']:
    print("\t" + topping)
users = {
    'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton'
        },
    'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
        }
    }
for username, user_info in users.items():
    print(f"\n Username: {username}")