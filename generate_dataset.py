import random

"""
Pembuatan dataset sesuai dengan kriteria variasi yang diminta.
Dataset akan berada pada range 1 sampai 100000.
Step akan disesuaikan dengan ukuran dataset agar distribusinya uniform.
"""
def generate_dataset(length, status):
    step = int(100000/length)
    if status == "sorted":
        dataset =  list(range(1, 100000, step))
    elif status == "random":
        dataset = random.sample(range(1, 100000, step), length)
    elif status == "reversed":
        dataset = list(range(100000, 0, -(step)))
    save_dataset(f"dataset/{status}_{length}.txt", dataset)
    return dataset

def save_dataset(filename, dataset):
    with open(filename, "w") as f:
        for data in dataset:
            f.write(str(data) + "\n")
            
dataset_sizes = [200, 2000, 20000]
dataset_status = ["sorted", "random", "reversed"]

# main program yang akan memanggil setiap fungsi
for size in dataset_sizes:
    for status in dataset_status:
        dataset = generate_dataset(size, status)  