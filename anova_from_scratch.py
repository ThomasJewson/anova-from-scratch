# %% Step 1:

import pandas as pd

# From remote rather than local for gist
DATA_LOC = r"https://raw.githubusercontent.com/ThomasJewson/anova-from-scratch/main/marij1_indiv.csv"
df = pd.read_csv(DATA_LOC)

df.head(5)
# %%
grand_mean = df["party"].mean()
df["squared_error"] = (df["party"] - grand_mean) ** 2
sst = df["squared_error"].sum()

# %%
usage_groups = df.groupby("marijUse")
grouped_means = usage_groups["party"].mean()


def get_variance_within(useage_group: pd.Series):
    return (useage_group - grouped_means[useage_group.name]) ** 2


df["variance_within"] = usage_groups["party"].apply(get_variance_within)
ssw = df["variance_within"].sum()
# %%
