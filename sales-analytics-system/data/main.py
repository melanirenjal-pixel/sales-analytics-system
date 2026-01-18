print("Sales Analytics System started")

file_path = "data/sales_data.txt"

with open(file_path, "r") as file:
    content = file.read()

print("Sales data loaded successfully")
print(content)

    
