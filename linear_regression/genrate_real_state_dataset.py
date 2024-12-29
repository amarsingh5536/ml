def generate_price(sqft, bedrooms, bathrooms, offers, brick, neighborhood):
    base_price = 100000
    price = base_price + (sqft * 100) + (bedrooms * 10000) + (bathrooms * 5000) + (offers * 2000)
    
    if brick:
        price += 50000  # Increase pricefor brick houses
    if neighborhood == "South":
        price += 100000  # Increase price for South neighborhood

    # Adding some randomness
    price += random.uniform(-50000, 50000)
    return round(price, 2)

def generate_data():
    data = []
    neighborhoods = [ "East", "West", "South", "North"]
    for i in range(1, 201):
        sqft = random.randint(800, 4000)
        
        if 800 <= sqft <= 1600:
            bedrooms = random.randint(1,3)
            bathrooms = random.randint(1, bedrooms)
        if 1600 <= sqft <= 2500:
            bedrooms = random.randint(2,4)
            bathrooms = random.randint(2, bedrooms)
        if 2600 <= sqft <= 4000:
            bedrooms = random.randint(2,5)
            bathrooms = random.randint(2, 4)
        
        offers = random.randint(0, 5)
        brick = random.choice([0, 1])
        neighborhood = random.choice(neighborhoods)
        
        price = generate_price(sqft, bedrooms, bathrooms, offers, brick, neighborhood)
        
        entry = {
            "property": f"{i}",
            "price": price,
            "sqft": sqft,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "offers": offers,
            "has_brick": brick,
            "neighborhood": neighborhood
        }
        data.append(entry)
    return data

# Generate the data
data = generate_data()

# Specify the CSV file name
csv_file = "real_estate_data.csv"

# Write data to CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["property", "price", "sqft", "bedrooms", "bathrooms", "offers", "has_brick", "neighborhood"])
    writer.writeheader()
    writer.writerows(data)

print(f"Data generated and saved to {csv_file}")