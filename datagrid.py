class Event:
    def __init__(self):
        self.id = None
        self.owner_id = None
        self.creation_date = None
        self.count = None
        self.name = None
        self.content = None

    def read_csv(file, sep=',', enconding='utf-8'):
        pass

    def show(start=0, end=100):
        pass

    def insert_row(row):
        pass

    def delete_row(column, value):
        pass

    def search(column, value):
        pass

    def sort(column, direction='asc'):
        pass

    def select_count(i,j):
        pass
