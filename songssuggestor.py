mood_songs = {
    "Happy" : [" For a reason " , "  Tere liye " ,  "Doron Doorn"],
    "Gym" : ["Sheesha" , "2 Gaz Ka Ghoo" , "Putt Jat da"],
    "Romantic" : ["Maula mere maula" , "Naam Tera "] ,
    "Sad" : ["Unforgettable", "Kina Cheer " ]
    
}

mood = str(input("Enter your mood = "))
if mood in mood_songs :
    print("Recommended songs are = ")
    for song in mood_songs[mood] :
        print("=" , song )
    
else: print("Not a valid input ")