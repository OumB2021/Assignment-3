class Product:

  #constructor
  def __init__(self, name, price, stock):
    if (stock < 0 ):
      raise ValueError("insufficient stock")
    else:
      self.name = name
      self.price = price
      self.stock = stock

  def get_info(self):
    return "%s - price: $%.0f - stock: %s" % (self.name, self.price, self.stock)

  def sell (self, quantity):
    if (self.stock < 0 ):
      raise ValueError("insufficient stock")
    elif (quantity > self.stock):
      raise ValueError("insufficient quantity")
    else:
      self.stock -= quantity
      return quantity*self.price

class Electronics(Product):

  def __init__ (self, name, price, stock, warranty):
    if (warranty < 0):
      raise ValueError("Warranty cannot be negative")
    else:
      super().__init__(name, price, stock)
      self.warranty = warranty
  
  def get_info(self):
    return "%s - Price: $%.0f - Stock: %s - Warranty: %s months" % (self.name, self.price, self.stock, self.warranty)

class Clothing(Product):

  def __init__ (self, name, price, stock, size):
    if (size.upper() not in ["XS", "S", "M", "L", "XXL"]):
      raise ValueError("Size is not correct")
    else:
      super().__init__(name, price, stock)
      self.size = size

  def get_info(self):
    return "%s - Price: $%.0f - Stock: %s - size: %s" % (self.name, self.price, self.stock, self.size)

class Store:

  def __init__(self):
    self.inventory = []

  def add_product(self, product):
    self.inventory.append(product)

  def sell_product(self, product_name, quantity):

    for item in self.inventory:
      if (product_name.title() == item.name.title()):
        return item.sell(quantity)

    raise ValueError("item was not found in the store")

  def get_inventory(self):

    inventory_str = ["Store Inventory:"]
    for item in self.inventory:
      inventory_str.append(item.get_info())
    
    return "\n".join(inventory_str)


def main():
  # Test Case 1: Create instances of Electronics and Clothing classes
  phone = Electronics("Phone", 700, 10, 24)
  shirt = Clothing("Shirt", 30, 25, "L")

  # Test Case 2: Test get_info method for Electronics and Clothing classes
  assert phone.get_info() == "Phone - Price: $700 - Stock: 10 - Warranty: 24 months"
  assert shirt.get_info() == "Shirt - Price: $30 - Stock: 25 - size: L"

  # Test Case 3: Test sell method for Product class
  assert phone.sell(2) == 1400
  assert shirt.sell(5) == 150
  assert phone.stock == 8
  assert shirt.stock == 20

  # Test Case 4: Test Store class add_product, sell_product, and get_inventory methods
  my_store = Store()
  my_store.add_product(phone)
  my_store.add_product(shirt)

  
  assert my_store.sell_product("Phone", 3) == 2100
  assert my_store.sell_product("Shirt", 10) == 300
  
  assert phone.stock == 5
  assert shirt.stock == 10

  inventory_str = "Store Inventory:\nPhone - Price: $700 - Stock: 5 - Warranty: 24 months\nShirt - Price: $30 - Stock: 10 - size: L"
  assert my_store.get_inventory() == inventory_str

  print("All sample test cases passed!")

main()
