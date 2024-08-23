from tqdm import tqdm
import time

def test():
    with tqdm(total=100) as pbar:
        while True:
            time.sleep(0.1)  # Simulate work being done
            pbar.update(10)

test()