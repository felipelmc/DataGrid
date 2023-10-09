import sys
sys.path.append('../src')

from datagrid import DataGrid
import time
import random

import sys
sys.path.append('../')

n = [10, 100, 1000, 10000, 100000, 300000, 500000]

# além de calcular o tempo de execução para tamanhos de entrada diferentes,
# também calcula a média de tempo de execução para cada tamanho de entrada

with open(f'../results/testSelectCount.csv', 'w') as f:
    f.write('method,n,mean_time\n')
    
    ######### FAKE DATA 10 #########

    # TESTS FOR MEDIAN OF MEDIANS
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data10.csv')
    times = []
    
    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9))
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'median-of-medians,10,{mean_time}\n')
    print(f"Median of medians with 10 rows: {mean_time}")

    # TESTS FOR QUICKSELECT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data10.csv')
    times = []
    
    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'quickselect,10,{mean_time}\n')
    print(f"Quickselect with 10 rows: {mean_time}")

    # TESTS FOR HEAPSORT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data10.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'heapsort,10,{mean_time}\n')
    print(f"Heapsort with 10 rows: {mean_time}")

    ######### FAKE DATA 100 #########

    # TESTS FOR MEDIAN OF MEDIANS
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data100.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99))
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'median-of-medians,100,{mean_time}\n')
    print(f"Median of medians with 100 rows: {mean_time}")

    # TESTS FOR QUICKSELECT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data100.csv')
    times = []
    
    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'quickselect,100,{mean_time}\n')
    print(f"Quickselect with 100 rows: {mean_time}")

    # TESTS FOR HEAPSORT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data100.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)
    
    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'heapsort,100,{mean_time}\n')
    print(f"Heapsort with 100 rows: {mean_time}")

    ######### FAKE DATA 1000 #########

    # TESTS FOR MEDIAN OF MEDIANS
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data1000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999))
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'median-of-medians,1000,{mean_time}\n')
    print(f"Median of medians with 1000 rows: {mean_time}")

    # TESTS FOR QUICKSELECT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data1000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'quickselect,1000,{mean_time}\n')
    print(f"Quickselect with 1000 rows: {mean_time}")

    # TESTS FOR HEAPSORT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data1000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'heapsort,1000,{mean_time}\n')
    print(f"Heapsort with 1000 rows: {mean_time}")

    ######### FAKE DATA 10000 #########

    # TESTS FOR MEDIAN OF MEDIANS
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data10000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999))
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'median-of-medians,10000,{mean_time}\n')
    print(f"Median of medians with 10000 rows: {mean_time}")

    # TESTS FOR QUICKSELECT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data10000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)
    
    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'quickselect,10000,{mean_time}\n')
    print(f"Quickselect with 10000 rows: {mean_time}")

    # TESTS FOR HEAPSORT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data10000.csv')
    times = []
    
    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 9999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'heapsort,10000,{mean_time}\n')
    print(f"Heapsort with 10000 rows: {mean_time}")

    ######### FAKE DATA 100000 #########

    # TESTS FOR MEDIAN OF MEDIANS
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data100000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999))
    end_time = time.time()
    times.append(end_time - start_time)
    
    mean_time = sum(times) / len(times)
    f.write(f'median-of-medians,100000,{mean_time}\n')
    print(f"Median of medians with 100000 rows: {mean_time}")

    # TESTS FOR QUICKSELECT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data100000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)
    
    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'quickselect,100000,{mean_time}\n')
    print(f"Quickselect with 100000 rows: {mean_time}")

    # TESTS FOR HEAPSORT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data100000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 99999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'heapsort,100000,{mean_time}\n')
    print(f"Heapsort with 100000 rows: {mean_time}")

    ######### FAKE DATA 300000 #########

    # TESTS FOR MEDIAN OF MEDIANS
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data300000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999))
    end_time = time.time()
    times.append(end_time - start_time)
    
    mean_time = sum(times) / len(times)
    f.write(f'median-of-medians,300000,{mean_time}\n')
    print(f"Median of medians with 300000 rows: {mean_time}")

    # TESTS FOR QUICKSELECT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data300000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'quickselect,300000,{mean_time}\n')
    print(f"Quickselect with 300000 rows: {mean_time}")

    # TESTS FOR HEAPSORT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data300000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 299999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'heapsort,300000,{mean_time}\n')
    print(f"Heapsort with 300000 rows: {mean_time}")

    ######### FAKE DATA 500000 #########

    # TESTS FOR MEDIAN OF MEDIANS
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data500000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999))
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999))
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'median-of-medians,500000,{mean_time}\n')
    print(f"Median of medians with 500000 rows: {mean_time}")

    # TESTS FOR QUICKSELECT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data500000.csv')
    times = []

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='quickselect')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'quickselect,500000,{mean_time}\n')
    print(f"Quickselect with 500000 rows: {mean_time}")

    # TESTS FOR HEAPSORT
    datagrid = DataGrid()
    datagrid.read_csv('../data/fake_data500000.csv')

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    start_time = time.time()
    datagrid.select_count(0, random.randint(0, 499999), how='heapsort')
    end_time = time.time()
    times.append(end_time - start_time)

    mean_time = sum(times) / len(times)
    f.write(f'heapsort,500000,{mean_time}\n')
    print(f"Heapsort with 500000 rows: {mean_time}")