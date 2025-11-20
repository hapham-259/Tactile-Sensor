import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


data_dir = "venv/lib/python3.12/site-packages/data/ur_tactip/surface_9d/data"
csv_path = os.path.join(data_dir, "targets.csv")
df = pd.read_csv(csv_path)


plt.figure(figsize=(6, 4))
plt.scatter(df["pose_z"],df["Fz"], s=5)
plt.xlabel("pose_z (contact depth)")
plt.ylabel("Fz (normal force)")
plt.title("Contact Depth vs Normal Force")
plt.grid(True)
plt.tight_layout()
plt.show()
