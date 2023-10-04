def calculate_pizza_price(size, flavor, peperoni, cheese):
    # Define prices for pizza sizes and flavors
    size_prices = {"small": 15, "medium": 20, "large": 25, "extra large": 30}
    flavor_prices = {"Fajita": 0, "Tikka": 0, "Hot and Spicy": 0, "Kababish Pizza": 0}

    # Calculate the base price based on size and flavor
    base_price = size_prices.get(size.lower(), 0) + flavor_prices.get(flavor, 0)

    # Calculate peperoni and cheese costs
    peperoni_cost = 0
    cheese_cost = 0

    if size.lower() in ["small", "medium"]:
        if peperoni:
            peperoni_cost = 2
        if cheese:
            cheese_cost = 1
    elif size.lower() in ["large", "extra large"]:
        if peperoni:
            peperoni_cost = 4
        if cheese:
            cheese_cost = 2

    # Calculate the total cost
    total_cost = base_price + peperoni_cost + cheese_cost
    return total_cost

def main():
    print("Welcome to the Pizza Order System")

    # Get user input for pizza details
    size = input("Enter pizza size (small, medium, large, extra large): ")
    flavor = input("Enter pizza flavor (Fajita, Tikka, Hot and Spicy, Kababish Pizza): ")
    peperoni = input("Do you want to add peperoni (yes/no)? ").lower() == "yes"
    cheese = input("Do you want to add cheese (yes/no)? ").lower() == "yes"

    # Calculate the total cost
    total_cost = calculate_pizza_price(size, flavor, peperoni, cheese)

    print(f"Your total bill is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
