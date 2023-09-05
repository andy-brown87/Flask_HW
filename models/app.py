from models.order import Order

order1 = Order("Harry", "11th July", 10)
# creates a new order object

print(f"{order1.input_customer_name} made an order on {order1.input_order_date} with a quantity of {order1.input_quantity})