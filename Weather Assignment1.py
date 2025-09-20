from datetime import date
import math

class WeatherRecord:
    def __init__(self, d, c, t):
        self.date = d
        self.city = c
        self.temp = t

# Dense 2D Array Storage
class DenseStorage:
    def __init__(self, base, end, c):
        self.baseYear = base
        self.cities = c
        self.cityIndex = {city.lower(): i for i, city in enumerate(c)}
        self.data = [[math.nan for _ in range(len(c))] for _ in range(end - base + 1)]

    def insert(self, r):
        self.data[r.date.year - self.baseYear][self.cityIndex[r.city.lower()]] = r.temp

    def delete(self, city, d):
        self.data[d.year - self.baseYear][self.cityIndex[city.lower()]] = math.nan

    def retrieve(self, city, year):
        r = year - self.baseYear
        c = self.cityIndex.get(city.lower(), -1)
        if c == -1 or r < 0 or r >= len(self.data):
            return "City/Year not valid."
        v = self.data[r][c]
        return f"No record found for {city} in {year}" if math.isnan(v) else f"{city} {year} -> {v}°C"

# Sparse Storage
class SparseStorage:
    def __init__(self):
        self.map = {}

    def key(self, d, c):
        return f"{d.year}-{c.lower()}"

    def insert(self, r):
        self.map[self.key(r.date, r.city)] = r.temp

    def delete(self, c, d):
        self.map.pop(self.key(d, c), None)

    def retrieve(self, c, y):
        v = self.map.get(f"{y}-{c.lower()}")
        return f"No record found for {c} in {y}" if v is None else f"{c} {y} -> {v}°C"

# ===== Main Interactive Program =====
if __name__ == "__main__":
    cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru"]
    dense = DenseStorage(2021, 2025, cities)
    sparse = SparseStorage()

    # Preloaded sample data
    dense.insert(WeatherRecord(date(2021, 1, 10), "Delhi", 15.2))
    dense.insert(WeatherRecord(date(2022, 5, 20), "Mumbai", 30.5))
    dense.insert(WeatherRecord(date(2023, 7, 12), "Chennai", 34.8))
    dense.insert(WeatherRecord(date(2024, 8, 5), "Kolkata", 32.1))
    dense.insert(WeatherRecord(date(2025, 3, 5), "Bengaluru", 20.3))

    sparse.insert(WeatherRecord(date(2021, 1, 10), "Delhi", 15.2))
    sparse.insert(WeatherRecord(date(2023, 7, 12), "Chennai", 34.8))
    sparse.insert(WeatherRecord(date(2025, 3, 5), "Bengaluru", 20.3))

    print("=== Weather Data System ===")
    print("Available cities:", cities)

    while True:
        choice = int(input("\nChoose option: 1=Retrieve  2=Insert  3=Delete  4=Exit : "))

        if choice == 4:
            break

        if choice == 1:  # Retrieve
            city = input("Enter city: ")
            year = int(input("Enter year (2021-2025): "))
            print("[Dense]", dense.retrieve(city, year))
            print("[Sparse]", sparse.retrieve(city, year))

        elif choice == 2:  # Insert
            city = input("Enter city: ")
            year = int(input("Enter year (2021-2025): "))
            temp = float(input("Enter temperature: "))
            d = date(year, 1, 1)
            r = WeatherRecord(d, city, temp)
            dense.insert(r)
            sparse.insert(r)
            print(f"Inserted {city} {year} -> {temp}°C")

        elif choice == 3:  # Delete
            city = input("Enter city: ")
            year = int(input("Enter year (2021-2025): "))
            d = date(year, 1, 1)
            dense.delete(city, d)
            sparse.delete(city, d)
            print(f"Deleted record for {city} {year}")

        else:
            print("Invalid choice!")

    # Complexity summary at exit
    print("\n=== Complexity Analysis ===")
    print("Insert/Delete/Retrieve: O(1)")
    print("Traversal: O(R*C)")
    print("Dense Space: O(R*C)")
    print("Sparse Space: O(K)")
    print("=== Program End ===")
