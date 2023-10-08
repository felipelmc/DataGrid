import warnings

class HashTable:
    def __init__(self, capacity, load_factor=0.75):
        self.load_factor = load_factor
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0  # Initialize the size to 0

    def _hash(self, key):
        """
        Hash the key and return the hashed value
        """
        return key % self.capacity
    
    def _resize(self):
        """
        Function to resize the table when the load factor is reached
        """
        # Create a new table with 3 times the capacity
        new_capacity = self.capacity * 3

        # Populate the new table with new_capacity None values
        new_table = [None] * new_capacity

        self.capacity = new_capacity  # Update the capacity

        # Iterate through the existing table and add the items to the new table
        for item in self.table:
            if item is not None:
                # Hash the key
                hashed_key = self._hash(item.id)
                count = 0

                while count < self.capacity:
                    # If the node is None, insert the event
                    if new_table[hashed_key] is None:
                        new_table[hashed_key] = item
                        break
                    # If the node is not None and it is deleted, insert the event
                    elif new_table[hashed_key].deleted is True:
                        new_table[hashed_key] = item
                        break
                    # If the node is not None and it is not deleted, keep going
                    else:
                        hashed_key = (hashed_key + 1) % self.capacity
                        count += 1

        self.table = new_table # Update the table

    def _check_resize(self):
        """
        Checks if the table needs to be resized
        """
        # Check the alpha of the table
        alpha = self.size / self.capacity

        # Resize if the alpha is greater than or equal to the load factor
        if alpha >= self.load_factor:
            self._resize()
    
    def insert(self, id, event):
        """
        Insert a new event into the table
        """
        self._check_resize()  # Check if the table needs to be resized
        hashed_id = self._hash(id) # Hash the id
        count = 0

        while count < self.capacity:
            # If the node is None, insert the event
            if self.table[hashed_id] is None:
                self.table[hashed_id] = event
                self.size += 1
                break
            # If the node is not None and it is deleted, insert the event
            elif self.table[hashed_id].deleted is True:
                self.table[hashed_id] = event
                self.size += 1
                break
            # If the node is not None and it is not deleted, keep going
            else:
                hashed_id = (hashed_id + 1) % self.capacity
                count += 1

    def search(self, value):
        """
        Search for a value in column "id" of the table
        """
        h = self._hash(value)
        event = None
        count = 0

        while count < self.capacity:
            event = self.table[h]
            # there never was a node with that id
            if event is None:
                break
            # there is a node with that id and it is not deleted
            if event.id == value and event.deleted is False:
                break
            h = (h + 1) % self.capacity
            count += 1
        
        # if the node is None or deleted, it means that the node was not found
        if event is None or event.deleted is True:
            print(f"Row with id = {value} not found")
        # otherwise, print the node
        else:
            print(f"{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}")

    def delete(self, value):
        """
        Deletes a row according to the value at the given column
        """
        hashed_id = self._hash(value)
        event = None
        count = 0
        changed_flag = False

        while count < self.capacity:
            event = self.table[hashed_id]
            # there never was a node with that id
            if event is None:
                break
            # there is a node with that id and it is not deleted
            if event.id == value and event.deleted is False:
                # delete the node
                event.deleted = True
                # set the flag to True
                changed_flag = True
                # decrease the size
                self.size -= 1
                break
            # otherwise, keep searching
            hashed_id = (hashed_id + 1) % self.capacity
            count += 1
        
        # if the node is None, it means that the node was not found
        if event is None or changed_flag is False:
            print(f"Row with id = {value} not found")
        # if the node was deleted
        elif event.deleted is True and changed_flag is True:
            print(f"Row with id = {value} deleted")
        