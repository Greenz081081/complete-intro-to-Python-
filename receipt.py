import csv
from datetime import datetime

# Get the current date and time from your computer's operating system
current_date_and_time = datetime.now(tz = None)

def main():
    # Include a try block
    try:
        print()

        # Print the store name at the top of the receipt.
        print("Inkom Emporium")

        sales_tax_rate = 0.06
    
    
        
        # Calls the read_products function and stores the 
        # products dictionary in a variable named products.
        products = read_products("products.csv")
    
        print()
        print("Requested Items")
        print()
     

        filename = "request.csv"
        # Opens the request.csv file for reading.
        with open(filename, "rt") as request_file:

        

            reader = csv.reader(request_file)

            next(reader)
       
            subtotal = 0
            # Contains a loop that reads and processes each row from the request.csv file.
            for items in reader:
                request_key = items[0]
                request_quantity = int(items[1]) 
          
            
                if request_key in products:
                    value = products[request_key]
                    name = value[0]
                    price = value[1]
                    quantity = request_quantity

                    # sum the numbers of ordered items
                    length = len(name)

                
           
                # Print the list of ordered items.
                print(f"{name}: {quantity} @ {price}")

                # sum the subtotal due
                subtotal  = subtotal + (quantity * price)

                # Compute the sales tax amount. Use 6% as the sales tax rate.
                sales_tax = subtotal * sales_tax_rate

                # Compute the total amount due.
                total = subtotal + sales_tax
    
            
            print()
            # print the number of ordered items.
            print(f"Number of items: {length}")

            # print the subtotal due.
            print(f"Subtotal: {subtotal:.2f}")

            # print the sales tax amount
            print(f"Sales Tax: {sales_tax:.2f}")

            # print the total amount due.
            print(f"Total: {total:.2f}")

            print()

            # Print a thank you message.
            print("Thank you for shopping at the Inkom Emporium.")

            # print the current date and time.
            print(f"{current_date_and_time:%a %b %w %X %Y}")

            filename = "receipt.txt"
            # Opens a text file named receipt.txt for appending
        with open (filename, "at") as receipt_file:

            # Appends to the end of the receipt.txt file one line of text that contains the
            # following five (5) values:
            # number of ordered items
            # the subtotal of the ordered items
            # sales tax amount
            # the total amount due
            # the current date

            print(f"Length: {length}, Subtotal: {subtotal:.2f}, Sales Tax: {sales_tax:.2f},"
            f" Total: {total:.2f}, Date: {current_date_and_time:%a %b %w %X %Y}", file=receipt_file)


    # except block to handle FileNotFoundError
    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                " because it doesn't exist.")

    # except block to handle PermissionError
    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                " because you don't have permission.")

    # except block to handle KeyError
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)


def read_products(filename):
    
    products_dict = {}

    filename = "products.csv"
    # open the products.csv file for reading
    with open(filename, "rt") as products_file:

    # use a csv.reader to read each row and populate a dictionary
    # named products with the contents of the products.csv file.
        reader = csv.reader(products_file)

        next(reader)

        for row in reader:
            product_key = row[0]
            product_name = row[1]
            product_price = float(row[2])

            products_dict[product_key] = [product_name, product_price]

    return products_dict

if __name__ == "__main__":
    main()



