from numpy import dot
from numpy.linalg import norm


def sozluk_hesaplama(veriler):
    genres = ["Unknown", "Action", "Adventure", "Animation", "Children's","Comedy",
    "Crime", "Documentary", "Drama","Fantasy", "Film-Noir", "Horror", 
    "Musical", "Mystery","Romance", "Sci-Fi", "Thriller", "War", "Western"]
    buyuk_sozluk={}
    dosya=open(veriler,"r")
    for veri in dosya:
        deger=veri.split("|")
        film_adlari=deger[1]
        buyuk_sozluk[film_adlari]={}
        for sayi in range(5,24):
            if deger[sayi]=="1" or deger[sayi]=="1/n":
                buyuk_sozluk[film_adlari][genres[sayi-5]]=1
    return buyuk_sozluk
            



def sim_jaccard(prefs, person1, person2):
    person1Kume=set()
    person2Kume=set()

    for kume1 in prefs[person1]:
        person1Kume.add(kume1)
        
    for kume2 in prefs[person2]:
        person2Kume.add(kume2)

    birlesim=len(person1Kume.union(person2Kume))
    kesisim= len(person1Kume.intersection(person2Kume))
    
    if birlesim == 0 or kesisim == 0:
        return 0
    
    return kesisim/birlesim



def topMatches(prefs, person, n=5, similarity=sim_jaccard):
    liste = []
    for other in prefs:
        if other != person:
            tu = (similarity(prefs, person, other), other)
            liste.append(tu)
    liste.sort(reverse=True)
    print(liste[:n])


def sim_cosine(prefs, person1, person2):

    person1_criticscores = []
    person2_criticscores = []

    for item in prefs[person1]:
        if item in prefs[person2]:
            person1_criticscores.append(prefs[person1][item])
            person2_criticscores.append(prefs[person2][item])

    if len(person1_criticscores) == 0:
        return 0
    
    cosine = dot(person1_criticscores, person2_criticscores) / \
        (norm(person1_criticscores) * norm(person2_criticscores))

 
    return cosine

def getRecommendations(prefs, person, similarity=sim_cosine):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)
    
        if sim <= 0: continue
        for item in prefs[other]:
            
            if item not in prefs[person] or prefs[person][item] == 0:
                
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                simSums.setdefault(item, 0)
                simSums[item] += sim

    rankings = [(total / simSums[item], item) 
                for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

