from sort import radix_sort, heapsort, mergesort, quicksort
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
      
    def _invert_order(arr):
        n = len(arr)
        return [arr[i] for i in range(n, -1, -1)]

    def _preProcessingCreationDate(arr):
        final = []
        for element in arr:
            element = element.replace("/", "")
            element = element.replace(":", "")
            element = element.replace(" ", "")
            final.append(element)
        return final

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
        Show the first end-start non-empty rows of the table
        """
        while start < end:
            if self.df.table[start] != None:
                events = self.df.table[start]
                for event in events:
                    print(f"{event.id} | {event.owner_id} | {event.creation_date} | {event.count} | {event.name} | {event.content}")
                    start += 1
            else:
                start += 1
                end += 1

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
        
        if column == 'id':
            self.id = heapsort(self.id)
            if column=='desc':
                self.id = self._invert_order(self.id)
            return self

        if column == 'name':
            #suspeito que seja counting sort devido ao tamanho maximo
            if direction=='desc':
                pass
            return self
        
        if column=='count':
            if direction=='desc':
                pass
            
        if column=='content':
            if direction=='desc':
                pass

    def select_count(self, i,j):
        pass
