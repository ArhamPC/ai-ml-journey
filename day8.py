import numpy as np
import pandas as pd

data = {
    "Name" : ["Aqib", "Pupi", "Moma", "Gidi", "Sany"],
    "score" : [90, 70, 92, 87, 55],
    "Age"   : [20, 22, 19, 21, 23]
}


set = pd.DataFrame(data)

print("=== Student Table ===")
print(set)


scores = np.array(data["score"])
print("Max Score --> " ,  np.max(scores))
print("Averae Score --> " , np.mean(scores))
print("Lowest Score -->", np.min(scores))
print("Total Score  -->", np.sum(scores))


print("With Max Score : " , set.loc[ set["score"].idxmax() , "Name"])
print("With Max Score : " , set.loc[ set["score"].idxmin() , "Name"])