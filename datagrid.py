from sort import radix_sort, radix_sort_strings, mergesort
from selection import searchBinaryTree
from hashtable import HashTable
import csv
import warnings

class Event:
    def __init__(self):
        self.id = None
        self.owner_id = None
        self.creation_date = None
        self.count = None
        self.name = None
        self.content = None

class DataGrid:
    def __init__(self):
        self.df = None
      
    def _invert_order(self, arr):
        return arr[::-1]
    
    def _extractArray(self, df, column):
        arr = []
        for bucket in df.table:
            if bucket is not None:
                for event in bucket:
                    if column == "id":
                        arr.append((event, event.id))
                    elif column == "owner_id":
                        arr.append((event, event.owner_id))
                    elif column == "creation_date":
                        arr.append((event, event.creation_date))
                    elif column == "count":
                        arr.append((event, event.count))
                    elif column == "name":
                        arr.append((event, event.name))
                    elif column == "content":
                        arr.append((event, event.content))
        return arr

    def read_csv(self, file, sep=',', enconding='utf-8'):
        """
        Read a csv file and return a HashTable
        """
        self.df = HashTable(20)
        
        with open(file) as csv_file:
            # read csv file
            csv_reader = csv.reader(csv_file, delimiter=sep)
            
            # iterate over each row and insert into HashTable
            for row in csv_reader:
                event = Event()
                event.id = int(row[0])
                event.owner_id = str(row[1])
                event.creation_date = str(row[2])
                event.count = int(row[3])
                event.name = str(row[4])
                event.content = str(row[5])
                self.df.insert(event.id, event)
            
            print("File read successfully")

    def show(self, start=0, end=100):
        """
        Show the table has not been sorted yet, it will show the entries between start and end by
        iterating over the buckets of the HashTable. 
        If the table has been sorted, it will show the entries between stat and end of the ordered array.
        """
        try:
            # tries to take the last ordered array
            arr = self.orderedArr
        except:
            # if it doesn't exist, just iterates over the table
            arr = self._extractArray(self.df, "id")

        while start < end:
            self.search("id", arr[start][0].id)
            start += 1
        
    def insert_row(self, row):
        """
        Receives a dictionary and inserts it into the table
        """
        event = Event()
        event.id = int(row["id"])
        event.owner_id = str(row["owner_id"])
        event.creation_date = str(row["creation_date"])
        event.count = int(row["count"])
        event.name = str(row["name"])
        event.content = str(row["content"])
        self.df.insert(event.id, event)

    def delete_row(self, column, value):
        """
        Receives the column and the value to be deleted & deletes
        """
        self.df.delete(column, value)
        
    def search(self, column, value):
        """
        Receives the column and the value to be searched & returns 
        every entry accordingly
        """
        self.df.search(column, value)

    def sort(self, column, direction='asc'):
        """
        Sorts the table by the column specified
        """
        arr = self._extractArray(self.df, column) #O(n)

        if column=='owner_id':
            arr = radix_sort_strings(arr)
        
        if column=='creation_date':
            arr = radix_sort_strings(arr)
                
        if column == 'name':
            self.name = radix_sort_strings(self.name, 20)
        
        if column == 'id':
            self.id = mergesort(self.id)

        if column =='count':
            self.count = mergesort(self.count) 

        if column=='content':
            self.content = mergesort(self.content)

        if direction=='desc':
            arr = self._invert_order(arr)

        self.orderedArr = arr

    def select_count(self, i, j):
        arr = self._extractArray(self.df, 'count') 
        # maybe here it should be quicksort so that I use quickselect to find the i and j
        #SELECT i IN O(n)
        #SELECT j IN O(n)
        #PERCORRE A HASHTABLE (i < count < j) #O(n)