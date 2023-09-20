from datagrid import Event
import time

def calculateTime(startTime):
    total = time.time()-startTime
    print(f'The total time of this operation was: {total}')

def shouldReadCSVwithSuccess(file):
    startTime = time.time()
    df = Event()
    df.read_csv(file)
    calculateTime(startTime)

