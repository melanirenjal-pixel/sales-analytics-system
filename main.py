from utils.data_processor import calculate_total_sales
from utils.file_handler import save_result

print("Sales Analytics System started")

file_path = "data/sales_data.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

print("Sales data loaded successfully")

total_sales = calculate_total_sales(lines)
print("Total Sales Amount:", total_sales)

save_result(total_sales)
print("Result saved to output/result.txt")


    
