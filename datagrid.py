from sort import radix_sort
from selection import searchBinaryTree
from data_storage import HashTable
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


    def read_csv(self, file, sep=',', enconding='utf-8'):
        """
        Read a csv file and return a HashTable
        """
        self.df = HashTable(100)
        
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

        return self.df


    def show(self, start=0, end=100):
        """
        Show the first end-start non-empty rows of the table
        """
        while start < end:
            event = self.df.table[start]
        
            if event is None:
                end += 1 # to avoid showing empty lines
                pass
            else:
                id = event.id
                owner_id = event.owner_id
                creation_date = event.creation_date
                count = event.count
                name = event.name
                content = event.content
                print(f'{id} | {owner_id} | {creation_date} | {count} | {name} | {content}')
            
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

        # Check if the id already exists
        if self.df.table[int(event.id)] is None:
            self.df.insert(int(event.id), event)
            print("Row inserted successfully")
        else:
            warnings.warn(f"ID {int(event.id)} already exists, row not inserted")


    def delete_row(self, column, value):
        for event in self.df.table:
            if event is not None:
                if column == "id" and int(event.id) == value:
                    self.df.table[int(event.id)] = None
                    print(f"Row with {column}: {event.id} deleted")
                
                elif column == "owner_id" and event.owner_id == value:
                    self.df.table[int(event.id)] = None
                    print(f"Row with {column}: {event.owner_id} deleted")
                
                elif column == "creation_date" and event.creation_date == value:
                    self.df.table[int(event.id)] = None
                    print(f"Row with {column}: {event.creation_date} deleted")
                
                elif column == "count" and event.count == value:
                    self.df.table[int(event.id)] = None
                    print(f"Row with {column}: {event.count} deleted")
                
                elif column == "name" and event.name == value:
                    self.df.table[int(event.id)] = None
                    print(f"Row with {column}: {event.name} deleted")
                
                elif column == "content" and event.content == value:
                    self.df.table[int(event.id)] = None
                    print(f"Row with {column}: {event.content} deleted")
        

    def search(self, column, value):
        pass


    def sort(self, column, direction='asc'):
        #Transforming string into ASCII
        decode_list = []
        if column=='owner_id':
            return radix_sort(self.owner_id)


    def select_count(self, i,j):
        pass
