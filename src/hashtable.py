from utils import is_prior_to, is_posterior_to, is_substring

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
            elif self.table[hashed_id].id == id:
                # update the event
                self.table[hashed_id] = event
                break
            # If the node is not None and it is not deleted, keep going
            else:
                hashed_id = (hashed_id + 1) % self.capacity
                count += 1

    def search(self, column, value):
        """
        Search for a value in column "id" of the table
        """
        if column == "id":
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
                return None
            # otherwise, print the node
            else:
                return event

        else:
            objects = []
            n_found = 0
            for event in self.table:
                if event is not None and event.deleted is False:
                    n = len(value)  
                    if (column == "owner_id" and event.owner_id == value 
                        or (column == "creation_date" and is_posterior_to(event.creation_date, value[0]) and is_prior_to(event.creation_date, value[1]))
                        or (column == "count" and event.count >= value[0] and event.count <= value[1])
                        or (column == "name" and is_substring(event.name, value, n))
                        or (column == "content" and is_substring(event.content, value, n))):
                        objects.append(event)
                        n_found += 1
            
            if n_found == 0:
                return None
            else:
                return objects

    def delete(self, column, value):
        """
        Deletes a row according to the value at the given column
        """
        if column == "id":
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
                return
            # if the node was deleted
            elif event.deleted is True and changed_flag is True:
                return
        
        else:
            for event in self.table:
                if event is not None and event.deleted is False:  
                    n = len(value)  
                    if (column == "owner_id" and event.owner_id == value 
                        or (column == "creation_date" and is_posterior_to(event.creation_date, value[0]) and is_prior_to(event.creation_date, value[1]))
                        or (column == "count" and event.count >= value[0] and event.count <= value[1])
                        or (column == "name" and is_substring(event.name, value, n))
                        or (column == "content" and is_substring(event.content, value, n))):
                        # delete the event
                        event.deleted = True
                        # decrease the size
                        self.size -= 1