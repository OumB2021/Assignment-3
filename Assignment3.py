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
    return "%s - price: $%.2f - stock: %s" % (self.name, self.price, self.stock)

  def sell (self, quantity):
    if (self.stock < 0 ):
      raise ValueError("insufficient stock")
    elif (quantity > self.stock):
      raise ValueError("insufficient quantity")
    else:
      self.stock -= quantity

class Electronics(Product):

  def __init__ (self, name, price, stock, warranty):
    if (warranty < 0):
      raise ValueError("Warranty cannot be negative")
    else:
      super().__init__(name, price, stock)
      self.warranty = warranty
  
  def get_info(self):
    return "%s - Price: $%.2f - Stock: %s - Warranty: %s months" % (self.name, self.price, self.stock, self.warranty)

class Clothing(Product):

  def __init__ (self, name, price, stock, size):
    if (size.upper() not in ["XS", "S", "M", "L", "XXL"]):
      raise ValueError("Size is not correct")
    else:
      super().__init__(name, price, stock)
      self.size = size

  def get_info(self):
    return "%s -, Price: $%.2f - Stock: %s - size: %s" % (self.name, self.price, self.stock, self.size)

class Store:

  def __init__(self):
    self.inventory = []

  def add_product(self, product):
    self.inventory.append(product)

  def sell_product(self, product_name, quantity):

    for item in self.inventory:
      if (product_name.title() == item.__class__.__name__):
        item.sell(quantity)
        return item.price * quantity

    raise ValueError("item was not found in the store")

  # def get_inventory(self):

  #   # for item in inventory:



def main():
  p = Product("p", 1.98, 5)

  e = Electronics("p", 1.23, 4, 4)

  c = Clothing("c", 2.54, 3, "s")

  s = Store()
  s.add_product(c)
  s.add_product(e)
  s.add_product(p)
  a = s.sell_product("product", 2)
  print (a)



main()
