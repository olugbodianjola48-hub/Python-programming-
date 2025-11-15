import pandas as pd

#for series

score = [50,60,90,55]
s = pd.Series(score, index=["Maths", "Eng", "Phy", "chm"])
print(s)

#for data frame:
data = {
       "Name": ["Tinubu", "Obi", "Atiku"],
       "Age" : [40, 60, 34],
       "score": [300, 430,900]
}
df = pd.DataFrame(data)
print(df)
print(df["Name"][0])