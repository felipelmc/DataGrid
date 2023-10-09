import sys
sys.path.append('../src')

from datagrid import DataGrid
import time

n = set([10, 100, 1000, 10000, 30000, 50000, 70000, 100000, 300000, 500000, 20000, 50000, 70000, 200000, 400000])
columns = ['id', 'owner_id', 'creation_date', 'count', 'name', 'content']

ids = [7, 99, 504, 1500, 19001, 200002, 40003]

owner_ids = ["NVNQ1", "OB89S", "64KCM", "Y9FPP", "SQLBM"]

creation_dates = [("2010/01/15 00:00:00", "2010/02/28 23:59:59"), ("2013/05/10 08:30:00", "2013/06/20 17:45:00"), 
                  ("2015/09/01 12:00:00", "2015/10/15 21:30:00"), ("2018/03/20 06:15:00", "2018/04/10 14:45:00"),
                  ("2020/11/05 15:30:00", "2020/12/31 23:59:59")]

counts = [(3, 7), (1, 2), (1, 5), (2, 4), (5, 10)]

names = ["AX", "HX", "PFL", "RKL", "Q"]

contents = ["A", "HX", "PLFRT", "KLTV", "WRT"]

with open(f'../results/testDelete.csv', 'w') as f:
    f.write('column,n,mean_time\n')

    for i in n:
        datagrid = DataGrid()
        datagrid.read_csv(f'../data/fake_data{i}.csv')

        for column in columns:
            if column == 'id':
                times = []
                for id in ids:
                    start_time = time.time()
                    
                    datagrid.delete_row(column, id)
                    
                    end_time = time.time()
                    times.append(end_time - start_time)

                mean_time = sum(times) / len(times)

                print(f"Mean time to delete_row {i} rows by {column}: {mean_time}")
                f.write(f'{column},{i},{mean_time}\n')
            
            elif column == 'owner_id':
                times = []
                for owner_id in owner_ids:
                    start_time = time.time()
                    
                    datagrid.delete_row(column, owner_id)
                    
                    end_time = time.time()
                    times.append(end_time - start_time)

                mean_time = sum(times) / len(times)

                print(f"Mean time to delete_row {i} rows by {column}: {mean_time}")
                f.write(f'{column},{i},{mean_time}\n')
            
            elif column == 'creation_date':
                times = []
                for creation_date in creation_dates:
                    start_time = time.time()
                    
                    datagrid.delete_row(column, creation_date)
                    
                    end_time = time.time()
                    times.append(end_time - start_time)

                mean_time = sum(times) / len(times)

                print(f"Mean time to delete_row {i} rows by {column}: {mean_time}")
                f.write(f'{column},{i},{mean_time}\n')

            elif column == 'count':
                times = []
                for count in counts:
                    start_time = time.time()
                    
                    datagrid.delete_row(column, count)
                    
                    end_time = time.time()
                    times.append(end_time - start_time)

                mean_time = sum(times) / len(times)

                print(f"Mean time to delete_row {i} rows by {column}: {mean_time}")
                f.write(f'{column},{i},{mean_time}\n')

            elif column == 'name':
                times = []
                for name in names:
                    start_time = time.time()
                    
                    datagrid.delete_row(column, name)
                    
                    end_time = time.time()
                    times.append(end_time - start_time)

                mean_time = sum(times) / len(times)

                print(f"Mean time to delete_row {i} rows by {column}: {mean_time}")
                f.write(f'{column},{i},{mean_time}\n')

            elif column == 'content':
                times = []
                for content in contents:
                    start_time = time.time()
                    
                    datagrid.delete_row(column, content)
                    
                    end_time = time.time()
                    times.append(end_time - start_time)

                mean_time = sum(times) / len(times)

                print(f"Mean time to delete_row {i} rows by {column}: {mean_time}")
                f.write(f'{column},{i},{mean_time}\n')

