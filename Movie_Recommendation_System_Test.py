from Movie_Recommendation_System import sozluk_hesaplama, sim_jaccard, topMatches, sim_cosine, getRecommendations

def main():
    prefs = sozluk_hesaplama("u.item.txt")
    print(prefs)
    print(sim_jaccard(prefs,"GoldenEye (1995)","Get Shorty (1995)"))
    topMatches(prefs, 'Star Wars (1977)', 5)
    topMatches(prefs, 'Lion King, The (1994)', 5)
    topMatches(prefs, 'Godfather, The (1972)', 5)
    print(getRecommendations(prefs, "GoldenEye (1995)"))
    
main()


    
