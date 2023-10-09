import sys
sys.path.append('../src')

from datagrid import DataGrid
import time

import sys
sys.path.append('../')

n = [10, 100, 1000, 10000, 100000, 300000, 500000]

# além de calcular o tempo de execução para tamanhos de entrada diferentes,
# também calcula a média de tempo de execução para cada tamanho de entrada

with open(f'../results/testSelectCount.csv', 'w') as f:
    f.write('method,n,mean_time\n')

    for i in n:
        datagrid = DataGrid()

        datagrid.read_csv(f'../data/fake_data{i}.csv')

        times = []
        for method in ['quickselect', 'heapsort']:
            for j in range(10):
                start_time = time.time()
                datagrid.select_count(0, 10, how=method)
                end_time = time.time()
                times.append(end_time - start_time)

            mean_time = sum(times) / len(times)

            print(f"Mean time to select count of {i} rows: {mean_time}")
            f.write(f'{i},{mean_time}\n')