import pandas as pd


###############################################
# Reading data
###############################################

# Fact Tables
economy = pd.read_csv("FHCode\Programming\Pandas\data\data1.csv")
health = pd.read_csv("FHCode\Programming\Pandas\data\data2.csv")
wdi_1999 = pd.read_csv("FHCode\Programming\Pandas\data\data3.csv")

# Dimension Table
countries = pd.read_csv("FHCode\Programming\Pandas\data\data4.csv")


###############################################
# A. Merging data
###############################################

df = pd.merge(left=economy,
              right=health,
              on=["iso3", "date"],
              how="inner")


# It is important to check whether the shape of the final data set is as expected!
print("Health: ", health.shape)
print("Economy: ", economy.shape)
print("Merged: ", df.shape)



# Using an outer join with indicator=True, we can check our merge operation
df = pd.merge(left=economy,
              right=health,
              on=["iso3", "date"],
              how="outer",
              indicator=True)
df.sort_values(["iso3", "date"], inplace=True)

df.value_counts("_merge")
print("Merged: ", df.shape)
df[df._merge == 'right_only']

# Let's take our large facts table as given (left table) and merge corresponding metadata on countries (right table) if available --> Left join

df = pd.merge(left=df,
              right=countries,
              left_on="iso3",
              right_on="id",
              how="left",
              indicator="country_merge")
print(df.shape)

df.country_merge.value_counts()


#################
# Concat
#################
# Finally, we want to add the World Development Indicators from 1999
# This is different from before: we do not need to merge on key columns

# Concat appends a DataFrame below another by default (axis=0)
# while merging on the column names

print(df.shape)
print(wdi_1999.shape)
df = pd.concat([df, wdi_1999], axis=0)
df.sort_values(["iso3", "date"], inplace=True, ignore_index=True)
print("Final DataFrame: ", df.shape)
