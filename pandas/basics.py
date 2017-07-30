import pandas as pd

web_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [12, 23, 22, 41, 11, 55],
    'Bounce_Rate': [55, 45, 65, 60, 70, 66]
}

df = pd.DataFrame(web_stats)
print(df)
