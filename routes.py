from app import app, db, Restaurant, Pizza, RestaurantPizza
from flask import jsonify

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in restaurant.pizzas]
    } for restaurant in restaurants])

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients,
        'restaurants': [{'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address} for restaurant in pizza.restaurants]
    } for pizza in pizzas])
