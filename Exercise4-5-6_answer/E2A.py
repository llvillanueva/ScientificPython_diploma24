import time
import recaman as rec

start_time = time.time()
rec.recaman(1000)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time without using SET: {elapsed_time} seconds")

start_time = time.time()

rec.recaman2(1000)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time using SET: {elapsed_time} seconds")