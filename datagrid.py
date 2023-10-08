from sort import radix_sort, radix_sort_strings, mergesort
from selection import searchBinaryTree
from hashtable import HashTable
import csv

class Event:
    def __init__(self):
        self.id = None
        self.owner_id = None
        self.creation_date = None
        self.count = None
        self.name = None
        self.content = None
        self.deleted = False

class DataGrid:
    def __init__(self):
        self.df = HashTable(10)
      
    def _invert_order(self, arr):
        return arr[::-1]
    
    def _extractArray(self, df, column):
        arr = []
        count = 0
        for event in df.table:
            if event is not None and event.deleted is False:
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
                count += 1
        return arr, count

    def read_csv(self, file, sep=',', enconding='utf-8'):
        """
        Read a csv file and return a HashTable
        """ 
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
        If the table has not been sorted yet, it will show the entries between start and end by
        iterating over the items of the HashTable. 
        If the table has been sorted, it will show the entries between start and end of the ordered array.
        """

        try:
            # tries to take the last ordered array
            arr = self.orderedArr
            if end > self.size_arr:
                end = self.size_arr
        except:
            arr, size_arr = self._extractArray(self.df, 'id')
            if end > size_arr:
                end = size_arr
        
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
        if column == "id":
            self.df.delete(value)
        elif column == "owner_id":
            pass
        elif column == "creation_date":
            pass
        elif column == "count":
            pass
        elif column == "name":
            pass
        elif column == "content":
            pass
        
    def search(self, column, value):
        """
        Receives the column and the value to be searched & returns 
        every entry accordingly
        """
        if column == "id":
            self.df.search(value)
        elif column == "owner_id":
            pass
        elif column == "creation_date":
            pass
        elif column == "count":
            pass
        elif column == "name":
            pass
        elif column == "content":
            pass

    def sort(self, column, direction='asc'):
        """
        Sorts the table by the column specified
        """
        arr, size_arr = self._extractArray(self.df, column)

        if column=='owner_id' or column=='creation_date':
            arr = radix_sort_strings(arr, len(arr[0]))
                
        if column == 'name':
            arr = radix_sort_strings(arr, 20)
        
        if column == 'id' or column == 'count' or column=='content':
            arr = mergesort(arr)

        if direction=='desc':
            arr = self._invert_order(arr)

        self.orderedArr = arr
        self.size_arr = size_arr

    def select_count(self, i, j):
        arr, size_arr = self._extractArray(self.df, 'count')
        arr = heapsort(arr)

        if i > size_arr:
            i = size_arr
        
        if j > size_arr:
            j = size_arr

        while i < j:
            self.search("id", arr[i][0].id)
            i += 1
            
        # maybe here it should be quicksort so that I use quickselect to find the i and j
        #SELECT i IN O(n)
        #SELECT j IN O(n)
        #PERCORRE A HASHTABLE (i < count < j) #O(n)