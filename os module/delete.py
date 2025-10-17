import os
import shutil

for i in range(0, 100):
    # os.rename(f"data/Day{i}", f"data/Tutorial{i}")
     shutil.rmtree(f"data/Tutorial {i}")