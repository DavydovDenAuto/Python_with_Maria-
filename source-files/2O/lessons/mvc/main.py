# https://www.giacomodebidda.com/posts/mvc-pattern-in-python-introduction-and-basicmodel/

import basic_backend
import mvc_exceptions as mvc_exc
import view
import model
import controller

my_items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]

c = controller.Controller(model.ModelBasic(my_items), view.View())
print ("c.show_items()")
c.show_items()
print("c.show_items(bullet_points=True)")
c.show_items(bullet_points=True)
print("c.show_item('chocolate')")
c.show_item('chocolate')
print ("c.show_item('bread')")
c.show_item('bread')
print("c.insert_item('bread', price=1.0, quantity=5)")
c.insert_item('bread', price=1.0, quantity=5)
print("c.insert_item('chocolate', price=2.0, quantity=10)")
c.insert_item('chocolate', price=2.0, quantity=10)
print("c.show_item('chocolate')")
c.show_item('chocolate')
print("c.update_item('milk', price=1.2, quantity=20)")
c.update_item('milk', price=1.2, quantity=20)
print("c.update_item('ice cream', price=3.5, quantity=20)")
c.update_item('ice cream', price=3.5, quantity=20)
print("c.delete_item('fish')")
c.delete_item('fish')
print("c.delete_item('bread')")
c.delete_item('bread')


