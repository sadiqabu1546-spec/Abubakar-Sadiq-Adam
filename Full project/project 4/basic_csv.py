DATA_FILE = "products.csv"

def parse_product_data(filename):
    product_list = []
    try:
        with open(filename, 'r') as file_object:
            # Read and discard the header line
            file_object.readline() 
            
            for line in file_object:
                try:
                    # Clean and split the line
                    parts = line.strip().split(',')
                    
                    if len(parts) != 3:
                        print(f"Warning: Skipping malformed line: {line.strip()}")
                        continue
                    
                    product_name = parts[0]
                    price = float(parts[1])
                    quantity = int(parts[2])
                    
                    # Create dictionary and add to list
                    product_dict = {
                        "Product": product_name, 
                        "Price": price, 
                        "Quantity": quantity
                    }
                    product_list.append(product_dict)
                    
                except ValueError:
                    print(f"Warning: Skipping invalid data row: {line.strip()}")
                    
        return product_list
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def main():
    product_data = parse_product_data(DATA_FILE)
    
    if product_data:
        print("\n--- Product Inventory Report ---")
        print(f"{'Product':<12} | {'Price':<10} | {'Quantity':<8} | {'Value':<10}")
        print("-" * 50)
        
        total_inventory_value = 0
        
        for product in product_data:
            item_value = product["Price"] * product["Quantity"]
            total_inventory_value += item_value
            
            print(f"{product['Product']:<12} | ${product['Price']:>9.2f} | {product['Quantity']:^8} | ${item_value:>9.2f}")
            
        print("-" * 50)
        print(f"Total Inventory Value: ${total_inventory_value:.2f}")
    else:
        print("No valid product data found to display.")

if __name__ == "__main__":
    main()
    
