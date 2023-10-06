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

        # Iterate through the existing table and add the items to the new table
        for bucket in self.table:
            if bucket is not None:
                for event in bucket:
                    hashed_id = self._hash(event.id)
                    new_table[hashed_id] = [event]

        self.capacity = new_capacity  # Update the capacity
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
        bucket = self.table[hashed_id] # Get the bucket list at the hashed_id

        if bucket is None:
            self.table[hashed_id] = [event]
            self.size += 1
            return
        else:
            for item in bucket:
                if item.id == id:
                    # update the item
                    item.owner_id = event.owner_id
                    item.creation_date = event.creation_date
                    item.count = event.count
                    item.name = event.name
                    item.content = event.content
                    warnings.warn("Item updated")
                    return
            bucket.append(event)
            self.size += 1
            return

    def search(self, column, value):
        """
        Search for a value in a given column of the table
        """
        for bucket in self.table:
            if bucket is not None:
                for event in bucket:
                    if column == "id" and int(event.id) == value:
                        print(f'{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}')
                    elif column == "owner_id" and event.owner_id == value:
                        print(f'{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}')
                    elif column == "creation_date" and event.creation_date == value:
                        print(f'{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}')
                    elif column == "count" and event.count == value:
                        print(f'{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}')
                    elif column == "name" and event.name == value:
                        print(f'{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}')
                    elif column == "content" and event.content == value:
                        print(f'{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}')

    def delete(self, column, value):
        """
        Deletes a row according to the value at the given column
        """
        for bucket in self.table:
            if bucket is not None:
                for event in bucket:
                    if column == "id" and int(event.id) == value:
                        bucket.remove(event)
                        print(f"Row with {column}: {event.id} deleted")
                    elif column == "owner_id" and event.owner_id == value:
                        bucket.remove(event)
                        print(f"Row with {column}: {event.owner_id} deleted")
                    elif column == "creation_date" and event.creation_date == value:
                        bucket.remove(event)
                        print(f"Row with {column}: {event.creation_date} deleted")
                    elif column == "count" and event.count == value:
                        bucket.remove(event)
                        print(f"Row with {column}: {event.count} deleted")
                    elif column == "name" and event.name == value:
                        bucket.remove(event)
                        print(f"Row with {column}: {event.name} deleted")
                    elif column == "content" and event.content == value:
                        bucket.remove(event)
                        print(f"Row with {column}: {event.content} deleted")