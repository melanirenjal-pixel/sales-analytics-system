from utils.file_handler import read_sales_data
from utils.data_processor import parse_sales_data, total_sales

def main():
    print("Day 2 started")

    file_path = "data/sales_data.txt"

    raw_lines = read_sales_data(file_path)
    records = parse_sales_data(raw_lines)

    print("Total records:", len(records))
    print("Total sales amount:", total_sales(records))

if __name__ == "__main__":
    main()


    
