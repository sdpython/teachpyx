import numpy as np
import pandas


data = [[8, 7], [18, 18], [6, 8]]
df = pandas.DataFrame(data, columns=["schtroumph"] * 2)
df["index"] = ["schtroumph"] * 3
df.set_index("index")
print(df)
print(df.to_latex(index=True))
