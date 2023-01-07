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
usage_groups = df.groupby("marijUse", group_keys=False)
grouped_means = usage_groups["party"].mean()


def get_variance_within(useage_group: pd.Series):
    return (useage_group - grouped_means[useage_group.name]) ** 2


df["variance_within"] = usage_groups["party"].apply(get_variance_within)
ssw = df["variance_within"].sum()
# %%
df["variance_between"] = (
    (usage_groups["party"].mean() - grand_mean) ** 2
) * usage_groups["party"].count()

ssb = df["variance_between"].sum()

ssb = sst - ssw
# %%
num_groups = df["marijUse"].nunique()
num_observations = len(df)

deg_of_freedom_within = num_observations - num_groups
deg_of_freedom_between_groups = num_groups - 1

f_statistic = (ssb / deg_of_freedom_between_groups) / (ssw / deg_of_freedom_within)
f_statistic
