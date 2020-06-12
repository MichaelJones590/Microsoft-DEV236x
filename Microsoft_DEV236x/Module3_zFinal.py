#3.6 Module 3 Required Coding Activity
# Cheese Order
max_order_amount = float(100.00)
min_order_amount = float(0.25)
price = float(7.99)
order_amount = input('Enter cheese order weight (numeric value):')
order_amount_float = float(order_amount)
if order_amount_float > max_order_amount:
    print(order_amount, 'is more than currently available stock')
elif order_amount_float < min_order_amount:
    print(order_amount, 'is below minimum order amount')
else:
    order_cost = order_amount_float * price
    print(str(order_amount_float), 'costs', ('$' + str(order_cost)))