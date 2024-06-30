import threading
import time
import mmap
import os
from queue import Queue

# Knuth-Morris-Pratt (KMP) qidiruv algoritmi
def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)

    # Prefiks funksiyasini yarating
    lps = [0] * m
    j = 0  # Pattern uchun indeks

    # Prefiks funksiyasini hisoblang
    compute_lps_array(pattern, m, lps)

    i = 0  # Text uchun indeks
    indices = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def search_worker(filename, pattern, start, end, result_queue):
    with open(filename, 'r') as f:
        f.seek(start)
        text = f.read(end - start)
        indices = kmp_search(pattern, text)
        # Qidiruv natijalariga global ofset qo'shing
        adjusted_indices = [index + start for index in indices]
        result_queue.put(adjusted_indices)

def main(filename, pattern, num_threads):
    start_time = time.time()

    file_size = os.path.getsize(filename)
    chunk_size = file_size // num_threads

    threads = []
    result_queue = Queue()

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else file_size
        thread = threading.Thread(target=search_worker, args=(filename, pattern, start, end, result_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_indices = []
    while not result_queue.empty():
        all_indices.extend(result_queue.get())

    end_time = time.time()
    print(f"Found at positions: {all_indices}")
    print(f"Total time: {end_time - start_time} seconds")

if __name__ == "__main__":
    filename = "large_text_file.txt"  # Katta hajmdagi matn fayl nomi
    pattern = "search_string"  # Qidirilayotgan string
    num_threads = 4  # Mavzular soni

    main(filename, pattern, num_threads)
