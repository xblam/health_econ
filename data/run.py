import pandas as pd
import numpy as np

# ================================================================
# 1. Load data
# ================================================================
df = pd.read_csv("health_econ_raw/health_econ_raw.csv")

print("Raw shape:", df.shape)
df.head()

print(list(df.columns))
