# %% Step 1: 

import pandas as pd

# From remote rather than local for gist
DATA_LOC = r"https://raw.githubusercontent.com/ThomasJewson/anova-from-scratch/main/marij1_indiv.csv"
df = pd.read_csv(DATA_LOC)

df.head(5)
# %%
