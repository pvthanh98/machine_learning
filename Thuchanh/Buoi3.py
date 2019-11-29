import pandas as pd
import numpy as np

data = pd.read_csv("playtennis.csv")
#yes 
dt0 = data.outlook[data.play=="yes"]
P1_1 = dt0.value_counts()
P1_1 = P1_1 / dt0.count()

dt0 = data.outlook[data.play=="no"]
print("-=====")
print(dt0)
P1_2 = dt0.value_counts()
P1_2 = P1_2 / dt0.count()

#temperture

dt0 = data.temp[data.play=="yes"]
P2_1 = dt0.value_counts()
P2_1 = P2_1 / dt0.count()

dt0 = data.temp[data.play=="no"]
P2_2 = dt0.value_counts()
P2_2 = P2_2 / dt0.count()

#humidity
dt0 = data.humidity[data.play=="yes"]
P3_1 = dt0.value_counts()
P3_1 = P3_1 / dt0.count()

dt0 = data.humidity[data.play=="no"]
P3_2 = dt0.value_counts()
P3_2 = P3_2 / dt0.count()

#windy
dt0 = data.windy[data.play=="yes"]
P4_1 = dt0.value_counts()
P4_1 = P4_1 / dt0.count()

dt0 = data.windy[data.play=="no"]
P4_2 = dt0.value_counts()
P4_2 = P4_2 / dt0.count()
2
play = data.play.value_counts() / data.play.count()
#du doan rainy cool high false

P_yes = P1_1.rainy * P2_1.cool * P3_1.high *P4_1[0] * play[0]
P_no = P1_2.rainy * P2_2.cool * P3_2.high *P4_2[0]*play[1]

P_y = P_yes / (P_no +P_yes)
P_n = P_no / (P_no +P_yes)

print("rate of yes: ",P_y)
print("rate of no: ",P_n)