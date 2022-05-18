class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions = 0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index] 
    
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    #If keys are the same, we are overriding.
    elif current_array_value[0] == key:
      self.array[array_index] = [key,value]
      return
    # Collision!
    number_collisions = 1
    while current_array_value[0] != key:
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array(new_array_index)
      if current_array_value is None or current_array_value[0] == key:
        self.array[array_index] = [key,value]
      number_collisions += 1    
      
    return

    # recursive method
  #def assign(self, key, value, number_collisions = 0):
    array_index = self.compressor(self.hash(key, number_collisions))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    number_collisions += 1
    self.assign(self, key, value, number_collisions)
    return
  
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    # possible_return_value holds different key
    retrieval_collisions = 1 
    while possible_return_value[0] != key:
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]
      if possible_return_value is None:
          return None
      if possible_return_value[0] == key:
          return possible_return_value[1]
      retrieval_collisions += 1
    return


hash_map = HashMap(20)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))


# Some things to consider:

# How would you delete a key-value pair from this hash map?
# Parts of the code are a little repetitive, how would you factor these roles differently?
# What should your hash map do if a key-value is added and the array is full? How does this hash map handle that?





























