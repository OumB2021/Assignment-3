class Product:

  #constructor
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock

  def get_info(self):
    return "Product's name: %s, price: %.2f, stock: %s" % (self.name, self.price, self.stock)

  def sell (self, quantity):
    if (self.stock < 0 or quantity > self.stock):
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
    return "Product's name: %s, price: %.2f, stock: %s, warranty: %s months" % (self.name, self.price, self.stock, self.warranty)

class Clothing(Product):

  def __init__ (self, name, price, stock, size):
    if (size.upper() not in ["XS", "S", "M", "L", "XXL"]):
      raise ValueError("Size is not correct")
    else:
      super().__init__(name, price, stock)
      self.size = size

  def get_info(self):
    return "Product's name: %s, price: %.2f, stock: %s, size: %s" % (self.name, self.price, self.stock, self.size)

def main():
  p = Product("p", 1.98, 3)
  print(p.get_info())

  e = Electronics("p", 1.23, 4, 4)
  print(e.get_info())

  c = Clothing("c", 2.0, 4, "l")
  print(c.get_info())

main()