import csv
def main():
  product_number = 0
  name = 1
  request_quantity = 1
  request_key = 0
  price = 2
  products = read_products("products.csv", product_number)
  print("Products")
  print(products)
  with open("request.csv", "rt") as csv_file:
    reader = csv.reader(csv_file)
    
    next(reader)
    for row in reader:
      product_name = products[request_key]
      name = product_name[0]
      quantity = request_quantity
      product_price = product_name[1]
  print(f"{name}, {quantity}, {product_price}")    
       
def read_products(filename, product):
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
    
       reader = csv.reader(csv_file)
       
       next(reader)
       
       for row in reader:
         
         key = row[product]
         
         dictionary[key] = row
    return dictionary

if __name__ == "__main__":
  main()
  