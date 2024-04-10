
# Pizza Restaurants API

This Flask API allows you to manage pizza restaurants and their pizzas. It provides endpoints for retrieving restaurants, deleting restaurants, retrieving pizzas, and creating new RestaurantPizzas.

## Getting Started

Follow these instructions to set up and run the server locally.

### Prerequisites

-   Python 3
-   Flask
-   SQLite or any other relational database management system (RDBMS)

### Installation

1.  Clone the repository.
2.  Navigate to the project directory.
3.  Install dependencies.
4.  Set up the database.

### Running the Server

Start the Flask server.

## Endpoints

### GET /restaurants

Retrieves all restaurants.

### GET /restaurants/:id

Retrieves a specific restaurant by ID.

### DELETE /restaurants/:id

Deletes a restaurant by ID.

### GET /pizzas

Retrieves all pizzas.

### POST /restaurant_pizzas

Creates a new RestaurantPizza associated with an existing Pizza and Restaurant.

## Conclusion

This API provides endpoints to manage pizza restaurants and pizzas. For more details on usage and implementation, please refer to the documentation above. If you encounter any issues or have questions, feel free to reach out. Happy coding!
