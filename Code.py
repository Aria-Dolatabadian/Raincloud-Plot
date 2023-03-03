import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid",font_scale=2)
import ptitprince as pt

df = pd.read_csv ("data.csv", sep= ",")
print(df.head())
print(df.tail())

sns.barplot(x = "group", y = "score", data = df, capsize= .1)
plt.title("Figure 1\n Bar Plot")
plt.show()

# plotting the clouds
f, ax = plt.subplots(figsize=(7, 5))
dy="group"; dx="score"; ort="h"; pal = sns.color_palette(n_colors=1)
ax=pt.half_violinplot( x = dx, y = dy, data = df, palette = pal, bw = .2, cut = 0.,
                      scale = "area", width = .6, inner = None, orient = ort)
plt.title("Figure 2\n Basic Rainclouds")
plt.show()

# adding the rain
f, ax = plt.subplots(figsize=(7, 5))
ax=pt.half_violinplot( x = dx, y = dy, data = df, palette = pal, bw = .2, cut = 0.,
scale = "area", width = .6, inner = None, orient = ort)
ax=sns.stripplot( x = dx, y = dy, data = df, palette = pal, edgecolor = "white",
size = 3, jitter = 0, zorder = 0, orient = ort)
plt.title("Figure 3\n Raincloud Without Jitter")
plt.show()
