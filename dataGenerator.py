import random
import string

def generate_data(n_rows):
    with open(f'data/fake_data{n_rows}.csv', 'w') as f:
    # id column
        for i in range(n_rows):
            id = i
            
            owner_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
            
            year = random.randint(2000, 2020)
            
            month = str(random.randint(1, 12))
            if len(month) == 1:
                month = '0' + month
            
            day = str(random.randint(1, 31))
            if len(day) == 1:
                day = '0' + day
            
            hour = str(random.randint(0, 23))
            if len(hour) == 1:
                hour = '0' + hour
            
            minute = str(random.randint(0, 59))
            if len(minute) == 1:
                minute = '0' + minute
            
            second = str(random.randint(0, 59))
            if len(second) == 1:
                second = '0' + second
            
            creation_date = str(year) + '/' + month + '/' + str(day) + ' ' + str(hour) + ':' + str(minute) + ':' + str(second)

            count = random.randint(0, 100)

            name = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(0, 19)))

            description = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(0, 400)))

            # insert the data into a csv file
            f.write(str(id) + ',' + str(owner_id) + ',' + str(creation_date) + ',' + str(count) + ',' + str(name) + ',' + str(description) + '\n')

def shuffle_data(file):
    with open(f'data/{file}', 'r') as f:
        lines = f.readlines()
        random.shuffle(lines)
        with open(f'data/{file}', 'w') as f:
            f.writelines(lines)

n = [10, 100, 1000, 10000, 100000, 300000, 500000]

for i in n:
    generate_data(i)
    shuffle_data(f'fake_data{i}.csv')