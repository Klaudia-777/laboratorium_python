import numpy as np
import threading
import operator
from functools import reduce
import datetime

initial_table = [12, 13, 67, 45, 23, 98, 38, 62, 18, 35, 21, 64, 52, 38, 76, 93, 39, 47, 81, 52, 57, 63]
bins = [0, 50, 60, 70, 80, 90, 100]
final_table = []

threads = []
histogram_threads = []
histogram_one_thread = []


def enlarge_no_records(final, init):
    for i in range(20):
        final.append(init)
    final = reduce(lambda x, y: x + y, final)


def one_thread(bins):
    a = np.array(final_table)
    histo, bin = np.histogram(a, bins)
    print(histo)
    print(bins)


def thread(bins):
    a = np.array(final_table)
    hist, bin = np.histogram(a, bins)
    histogram_threads.append(hist.tolist())


# dzielimy listę do wyrysowania histogramu
# na 3 części i obliczamy w osobnych wątkach:

def start_threads():
    for index in range(3):
        x = threading.Thread(target=thread, args=(bins[index * 2:index * 2 + 3],))
        threads.append(x)
        x.start()


enlarge_no_records(final_table, initial_table)

# obliczanie w pojedynczym wątku
one_thread_start_time = datetime.datetime.now()
one_thread(bins)
#one_thread_stop_time = datetime.datetime.now()
#one_thread_diff = one_thread_stop_time - one_thread_start_time

#print(one_thread_diff)
print("\n\n")

# sposób z podzialem na wątki
threads_start_time = datetime.datetime.now()
start_threads()
#threads_stop_time = datetime.datetime.now()
#threads_diff = threads_stop_time - threads_start_time

histogram_threads = reduce(lambda x, y: x + y, histogram_threads)
print(histogram_threads)
print(bins)
#print(threads_diff)