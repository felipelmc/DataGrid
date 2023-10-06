import warnings

class HashTable:
    def __init__(self, capacity, load_factor=0.75):
        self.load_factor = load_factor
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0  # Initialize the size to 0

    def _hash(self, key):
        return key
    
    def _resize(self):
        # Create a new table with 3 times the capacity
        new_capacity = self.capacity * 3

        # Populate the new table with new_capacity None values
        new_table = [None] * new_capacity

        # Iterate through the existing table and add the items to the new table
        for item in self.table:
            if item is not None:
                new_index = self._hash(item.id)
                new_table[new_index] = item

        self.capacity = new_capacity  # Update the capacity
        self.table = new_table # Update the table

    def _check_resize(self):
        # Check the alpha of the table
        alpha = self.size / self.capacity

        # Resize if the alpha is greater than or equal to the load factor
        if alpha >= self.load_factor:
            self._resize()
    
    def insert(self, key, value):
        # Check if the table needs to be resized
        self._check_resize()

        # Get the index of the key
        index = self._hash(key)

        # If the index is empty, insert the value
        if self.table[index] is None:
            self.table[index] = value
            self.size += 1  # Increment the size
        else:
            warnings.warn(f"ID {key} already exists, row not inserted")
