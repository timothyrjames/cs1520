# we'll use this separate file so that we don't have to tightly couple our 
# data access code and our application.
class ShoppingListItem(object):
  def __init__(self, id, title='', quantity=0):
    self.title = title
    self.quantity = quantity
    self.id = id

  def to_dict(self):
    return {
      'title': self.title,
      'quantity': self.quantity,
    }