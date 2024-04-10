from flask import request
from app import app, db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
    db.session.add_all([pizza1, pizza2])
    db.session.commit()

    restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
    restaurant2 = Restaurant(name='Pizza Hut', address='Westgate')

    db.session.add_all([restaurant1, restaurant2])
    db.session.commit()

    restaurant_pizza1 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza1.id, price=10.99)
    restaurant_pizza2 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza2.id, price=12.99)
    restaurant_pizza3 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza1.id, price=11.99)
    restaurant_pizza4 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza2.id, price=13.99)

    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4])
    db.session.commit()
