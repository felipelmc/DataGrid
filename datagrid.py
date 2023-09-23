from sort import radix_sort
from selection import searchBinaryTree

class Event:
    def __init__(self):
        self.id = None
        self.owner_id = None
        self.creation_date = None
        self.count = None
        self.name = None
        self.content = None

    def read_csv(self, file, sep=',', enconding='utf-8'):
        pass

    def show(self, start=0, end=100):
        pass

    def insert_row(self, row):
        pass

    def delete_row(self, column, value):
        pass

    def search(self, column, value):
        pass

    def sort(self, column, direction='asc'):
        #Transforming string into ASCII
        decode_list = []
        if column=='owner_id':
            return radix_sort(self.owner_id)

    def select_count(self, i,j):
        pass
