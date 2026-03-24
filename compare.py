import json

with open("mileage.json") as f:
    cars = json.load(f)

best = max(cars, key=lambda x: int(x["mileage"].split()[0]))

print("Best Mileage Car:")
print(best["car"], "-", best["mileage"])
