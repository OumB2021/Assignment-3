class Product:

  #default constructor
  def __init__(self):
    name = ""
    price = 0.0
    stock = 0

  #overloaded constructor
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock

  def get_info(self):
    return "Product's name: %s, price: %f, stock: %s" % (self.name, self.price, self.stock)  