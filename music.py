import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
data = pd.read_csv("data_fin.csv")
vec = TfidfVectorizer()
vector = vec.fit_transform(data.genre)
index = pd.Series(data = data.index, index=data.music)
def recommender(music,n=10):
    loc = index[music] 
    dis = linear_kernel(vector[loc],vector)
    val = pd.DataFrame(dis)
    val = val.transpose()
    val.columns = ["music"]
    val = val.sort_values(by = "music", ascending=False)
    name = []
    gen = []
    rate = []
    pop = []
    for i in range(0,n):
        name.append(data.music[val.index[i]])
        gen.append(data.genre[val.index[i]])
        rate.append(data.rating[val.index[i]])
        pop.append(data.Popularity[val.index[i]])
    return name , gen , rate , pop

def checker(name):
    if name in index:
        return "1"
    
def lister():
    return data.music, data.genre, data.rating, data.Popularity