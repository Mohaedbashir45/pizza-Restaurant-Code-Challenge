import os
from app import app, db, Restaurant, Pizza, RestaurantPizza

# Create the database file if it doesn't exist
if not os.path.exists('pizza.db'):
    with app.app_context():
        db.create_all()

# Now you can work with the models
def add_test_data():
    with app.app_context():
        # Add test data
        cheese_pizza = Pizza(name='Cheese', ingredients='Cheese')
        pepperoni_pizza = Pizza(name='Pepperoni', ingredients='Pepperoni')
        db.session.add_all([cheese_pizza, pepperoni_pizza])
        db.session.commit()

        dominion_pizza = Restaurant(name='Dominion Pizza', address='Test Address')
        pizza_hut = Restaurant(name='Pizza Hut', address='Test Address')
        db.session.add_all([dominion_pizza, pizza_hut])
        db.session.commit()

        dominion_pizza_cheese = RestaurantPizza(price=5, restaurant_id=dominion_pizza.id, pizza_id=cheese_pizza.id)
        dominion_pizza_pepperoni = RestaurantPizza(price=6, restaurant_id=dominion_pizza.id, pizza_id=pepperoni_pizza.id)
        pizza_hut_cheese = RestaurantPizza(price=7, restaurant_id=pizza_hut.id, pizza_id=cheese_pizza.id)
        pizza_hut_pepperoni = RestaurantPizza(price=8, restaurant_id=pizza_hut.id, pizza_id=pepperoni_pizza.id)
        db.session.add_all([dominion_pizza_cheese, dominion_pizza_pepperoni, pizza_hut_cheese, pizza_hut_pepperoni])
        db.session.commit()

if __name__ == '__main__':
    add_test_data