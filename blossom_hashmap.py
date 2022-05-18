from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for item in range(self.array_size)]
  
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code  
  
  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for lst in list_at_array:
      if lst[0] == key:
        lst[1] = value
        return
    list_at_array.insert(payload)
      

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]
    for lst in list_at_index:
      if lst[0] == key:
        return lst[0], lst[1]
    return None

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
blossom.assign("Andy","Kim")
print(blossom.retrieve('Andy'))
