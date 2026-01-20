from utils.file_handler import read_sales_data
from utils.data_processor import process_sales_data


def main():
    print("Sales Analytics System started")

    file_path = "data/sales_data.txt"

    # Step 1: Read raw sales data
    raw_lines = read_sales_data(file_path)
    print("Total records read:", len(raw_lines))

    # Step 2: Process sales data
    sales = process_sales_data(raw_lines)
    print("Total valid sales records:", len(sales))

    # Step 3: Show first 5 processed records
    print("\nSample processed records:")
    for record in sales[:5]:
        print(record)


if __name__ == "__main__":
    main()





    
