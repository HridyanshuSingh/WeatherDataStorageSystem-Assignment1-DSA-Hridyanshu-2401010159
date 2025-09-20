Assignment 1 DSA

# 🌦 Weather Data Management System (Python)

This project implements a simple **Weather Data Storage and Retrieval System** using two storage approaches:
- **Dense 2D Array Storage**
- **Sparse Storage (Dictionary/HashMap)**

It allows users to insert, delete, and retrieve weather records interactively, while comparing performance trade-offs of both storage techniques.

---

## 📌 Features
- **WeatherRecord ADT** to represent `(date, city, temperature)`.
- **DenseStorage**:
  - Uses a 2D list (Year × City).
  - Stores temperature values indexed by year & city.
- **SparseStorage**:
  - Uses a dictionary (hash map).
  - Stores only existing `(year, city)` records.
- **Interactive Menu**:
  - Retrieve temperature for a given city & year.
  - Insert a new record.
  - Delete an existing record.
  - Exit the system.
- **Complexity Analysis** displayed at the end.
