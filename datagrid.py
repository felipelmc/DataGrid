from sort import radix_sort, heapsort, mergesort, quicksort, custom_key
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
        pass
      
    def _invert_order(self, arr):
        return arr[::-1]

    def _preProcessingCreationDate(self, arr):
        final = []
        for element in arr:
            element = element.replace("/", "")
            element = element.replace(":", "")
            element = element.replace(" ", "")
            final.append(element)
        return final
    
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

    def _postProcessingCreationDate(arr):
        final = []
        for e in arr:
            final_str = e[0:3]+"/"+e[4:5]+"/"+e[6:7]+" "+e[8:9]+":"+e[10:11]+":"+e[12:13]
        final.append(final_str)
        return final

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
        arr = self._extractArray(self.df, column)

        if column=='owner_id':
            self.owner_id = radix_sort(self.owner_id)
            if direction=='desc':
                self.owner_id = self._invert_order(self.owner_id)
            return self
        
        if column=='creation_date':
            self.creation_date = self._preProcessingCreatedDate(self.creation_date)
            self.creation_date = radix_sort(self.creation_date)
            if direction=='desc':
                self.creation_date = self._invert_order(self.creation_date)
            self.creation_date = self._postProcressingCreatedDate(self.creation_date)
            return self
        
        if column == 'id' or column == 'count':
            arr = heapsort(arr)
            if direction=='desc':
                arr = self._invert_order(arr)

        if column == 'name':
            #suspeito que seja counting sort devido ao tamanho maximo
            if direction=='desc':
                pass
            return self
            
        if column=='content':
            if direction=='desc':
                pass
        
        # creates the ordered array variable
        self.orderedArr = arr

    def select_count(self, i, j):
        pass
