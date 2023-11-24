
def get_price_of_cake_with_discount(cake_type):
    """
    This function calculates the price of a cake with a discount.
    
    Parameters:
    cake_type (str): The type of cake.
    
    Returns:
    float: The price of the cake with the discount applied.
    """
    # Set the base price of the cake
    price = 10

    # Define the discounts for each cake type
    discount = {
        "chocolate": 10, # 10% discount
        "zanahoria": 20, # 20% discount
        "bayas": 0       # No discount
    }

    # Calculate the current discount as a fraction
    current_discount = discount[cake_type] / 100

    # Calculate the price of the cake with the discount applied
    price_with_discount = price - price * current_discount

    return price_with_discount # Return the price of the cake with the discount applied

# Test the function with different cake types
cake_type = "chocolate"
print("El pastel de chocolate cuesta", get_price_of_cake_with_discount("chocolate"))

cake_type = "zanahoria"
print("El pastel de zanahoria cuesta", get_price_of_cake_with_discount("zanahoria"))

cake_type = "bayas"
print("El pastel de bayas cuesta", get_price_of_cake_with_discount("bayas"))
#
#This code defines a function called `get_price_of_cake_with_discount` that takes a `cake_type` parameter