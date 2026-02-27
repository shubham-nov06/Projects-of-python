# This Python code snippet creates a dictionary called `mood_songs` where each key represents a mood
# (e.g., "Happy", "Gym", "Romantic", "Sad") and the corresponding value is a list of songs associated
# with that mood.
mood_songs = {
    "Happy": [" For a reason ", "  Tere liye ", "Doron Doorn"],
    "Gym": ["Sheesha", "2 Gaz Ka Ghoo", "Putt Jat da"],
    "Romantic": ["Maula mere maula", "Naam Tera "],
    "Sad": ["Unforgettable", "Kina Cheer "],
}

mood = str(input("Enter your mood = "))
if mood in mood_songs:
    print("Recommended songs are = ")
    songs = mood_songs[mood]

    for i in range(len(songs)):
        print(f"{i+1}.{songs[i]}")

else:
    print("Not a valid input ")
