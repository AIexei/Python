from modules.unique_items import *

items = UniqueItems()

getattr(items, "add")([1, 4])
items.list()
getattr(items, "remove")([1])
items.list()