vehicles = {
    101: {
        "brand": "Toyota",
        "model": "Innova",
        "vehicle_type": "SUV",
        "fuel_type": "Diesel",
        "rent_per_day": 3500,
        "total_bookings": 25,
        "available": True,
        "maintenance_cost": 12000,
        "year": 2023,
        "rating": 4.7
    },
    102: {
        "brand": "Hyundai",
        "model": "Creta",
        "vehicle_type": "SUV",
        "fuel_type": "Petrol",
        "rent_per_day": 2500,
        "total_bookings": 32,
        "available": True,
        "maintenance_cost": 8000,
        "year": 2022,
        "rating": 4.5
    },
    103: {
        "brand": "Maruti",
        "model": "Swift",
        "vehicle_type": "Hatchback",
        "fuel_type": "Petrol",
        "rent_per_day": 1500,
        "total_bookings": 40,
        "available": False,
        "maintenance_cost": 5000,
        "year": 2021,
        "rating": 4.2
    },
    104: {
        "brand": "Honda",
        "model": "City",
        "vehicle_type": "Sedan",
        "fuel_type": "Petrol",
        "rent_per_day": 2200,
        "total_bookings": 28,
        "available": True,
        "maintenance_cost": 7000,
        "year": 2023,
        "rating": 4.6
    },
    105: {
        "brand": "Tata",
        "model": "Nexon",
        "vehicle_type": "SUV",
        "fuel_type": "Electric",
        "rent_per_day": 2800,
        "total_bookings": 35,
        "available": True,
        "maintenance_cost": 4000,
        "year": 2024,
        "rating": 4.8
    },
    106: {
        "brand": "Mahindra",
        "model": "Thar",
        "vehicle_type": "SUV",
        "fuel_type": "Diesel",
        "rent_per_day": 4000,
        "total_bookings": 20,
        "available": False,
        "maintenance_cost": 15000,
        "year": 2022,
        "rating": 4.9
    },
    107: {
        "brand": "Maruti",
        "model": "Baleno",
        "vehicle_type": "Hatchback",
        "fuel_type": "Petrol",
        "rent_per_day": 1700,
        "total_bookings": 38,
        "available": True,
        "maintenance_cost": 4500,
        "year": 2023,
        "rating": 4.3
    },
    108: {
        "brand": "Hyundai",
        "model": "Verna",
        "vehicle_type": "Sedan",
        "fuel_type": "Petrol",
        "rent_per_day": 2300,
        "total_bookings": 22,
        "available": True,
        "maintenance_cost": 6500,
        "year": 2021,
        "rating": 4.4
    },
    109: {
        "brand": "Kia",
        "model": "Seltos",
        "vehicle_type": "SUV",
        "fuel_type": "Diesel",
        "rent_per_day": 3000,
        "total_bookings": 30,
        "available": False,
        "maintenance_cost": 9000,
        "year": 2024,
        "rating": 4.6
    },
    110: {
        "brand": "Tata",
        "model": "Tiago",
        "vehicle_type": "Hatchback",
        "fuel_type": "Electric",
        "rent_per_day": 1800,
        "total_bookings": 26,
        "available": True,
        "maintenance_cost": 3000,
        "year": 2024,
        "rating": 4.1
    }
}

print(vehicles)

# WAP to display count of all vehicles and with their ID ,model and brand
count = 0
for k,v in vehicles.items():
    count += 1    
    print(k,v["brand"],v['model'])
print("Total count of all vehicles:",count)

# WAP to print ID from USER if ID present print all details and if not present print other message
vid = int(input("Enter a ID:"))

if vid in vehicles.keys():
    details = vehicles[vid]
    print(details)
else:
    print("ID not present")
    
# Display all vehicle that are availble on rent . prinr their brand,model and daily rental price
for k in vehicles.values():
    if k["available"] == True:
        print(f" Brand_name : {k["brand"]} , model_name: {k["model"]} , price : {k["rent_per_day"]}")

# find most expensive and cheapets vehiclea based on thei daily rental price . Display their brand , model , and rental prize
min_price = float('inf')
max_price = float('-inf')

for key, details in vehicles.items():
    price = details["rent_per_day"]

    if price > max_price:
        max_price = price

    if price < min_price:
        min_price = price

print("Maximum rental price:", max_price)
print("Minimum rental price:", min_price)

#  Q5. Average Rental Price --> Calculate and display the average daily rental price of all vehicles in the dataset.
total_price = 0
count = 0

for val in vehicles.values():
    total_price += val["rent_per_day"] 
    count += 1

avg_price = total_price / count
print("Total average price :",avg_price)

# Q6. Vehicle Filtering
# Display all vehicles that meet both conditions:
# • Their rating is greater than 4.5.
# • Their daily rental price is greater than ₹2,000.

for val in vehicles.values():
    if val["rating"] > 4.5 and val["rent_per_day"] > 2000:
        print("Model :",val["model"],"Brand : ",val["brand"],"rating :",val["rating"],"rent : " ,val["rent_per_day"])

# Q7. Fuel Type Analysis
# Count how many vehicles use each fuel type, such as Petrol, Diesel, and Electric. Store the results in a
# new dictionary.
freq = {}
count_petrol = 0
count_disel = 0
count_ele = 0

for val in vehicles.values():
    if val["fuel_type"] == "Petrol":
        count_petrol += 1
    elif val["fuel_type"] == "Diesel":
        count_disel += 1
    else:
        count_ele += 1
freq["Petrol"] = count_petrol
freq["Diesel"] = count_disel
freq["Electric"] = count_ele

print("Frequency of all fuel type : ",freq)

# Q8. Booking Revenue Calculation
# Calculate the estimated revenue generated by each vehicle using the following formula:
# Estimated Revenue = Rent Per Day × Total Bookings
# Display the brand, model, and estimated revenue for each vehicle. Assume every booking represents one rental day.
for val in vehicles.values():
    estimated_revenue = val["rent_per_day"] * val["total_bookings"]
    print("The estimated Revenue of model",val["brand"],"-->",val["model"],":", estimated_revenue)


# Q9. Top 3 Vehicles
# Find the top three vehicles with the highest customer ratings. Display their brand, model, and rating in descending order.
top_3 = sorted(
    vehicles.values(),
    key=lambda val: val["rating"],
    reverse=True
)
for val in top_3[:3]:
    print("Brand:", val["brand"])
    print("Model:", val["model"])
    print("Rating:", val["rating"])
    print()

# Q10. Vehicle Rental Summary Report
# Generate a summary report containing the following information:
# • Total number of vehicles.
count = 0
for val in vehicles.values():
    count += 1
print(count)

# • Number of available and unavailable vehicles.
total_av = 0
total_unav = 0

for val in vehicles.values():
    if val["available"]:
        total_av += 1
    else:
        total_unav += 1
print("Total available vehicles:",total_av)
print("Total unavailable vehicles:",total_unav)

# • Total number of bookings.
total = 0
for val in vehicles.values():
    total += val["total_bookings"]
print("Total no.of booking is :",total)

# • Average daily rental price.
total_price = 0
count = 0
for val in vehicles.values():
    total_price += val["rent_per_day"]
    count += 1

avg_price = total_price / count
print("Average daily rental price:", avg_price)

# • Total maintenance cost.
total = 0
for val in vehicles.values():
    total += val["maintenance_cost"]
print("Total maintance cost is :",total)

# • Highest-rated vehicle.
highest = max(vehicles.values(), key=lambda val: val["rating"])
print("Brand:", highest["brand"])
print("Model:", highest["model"])
print("Rating:", highest["rating"])
