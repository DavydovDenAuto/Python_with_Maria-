def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')  # this line will execute during import because it is not within main block
if __name__ == "__main__": # this line is under main block hence it will only execute when you execute this file not on import
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
проверять, запущен ли скрипт как программа, или импортирован. Это можно сделать с помощью переменной __name__, 
которая определена в любой программе, и равна "__main__", если скрипт запущен в качестве главной программы, 
и имя, если он импортирован. 
"""