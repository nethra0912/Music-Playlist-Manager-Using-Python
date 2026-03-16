import random

# recursion function to count songs
def count_songs(playlist, i=0):
    if i == len(playlist):
        return 0
    return 1 + count_songs(playlist, i+1)


# function to add song
def add_song(playlist, ratings):
    song = input("Enter song name: ")
    rating = int(input("Enter rating (1-5): "))
    
    playlist.append(song)
    ratings.append(rating)

    print("Song added to playlist!\n")


# function to view playlist
def view_playlist(playlist, ratings):
    if len(playlist) == 0:
        print("Playlist is empty.\n")
    else:
        print("\nYour Playlist")
        for i in range(len(playlist)):
            print(i+1, "-", playlist[i], "| Rating:", ratings[i])
        print()


# function to remove song
def remove_song(playlist, ratings):
    view_playlist(playlist, ratings)
    
    num = int(input("Enter song number to remove: "))
    
    if num > 0 and num <= len(playlist):
        removed = playlist.pop(num-1)
        ratings.pop(num-1)
        print(removed, "removed from playlist.\n")
    else:
        print("Invalid number.\n")


# function to play random song
def play_random_song(playlist):
    if len(playlist) == 0:
        print("No songs available.\n")
    else:
        song = random.choice(playlist)
        print("Now Playing:", song, "🎵\n")


# function to analyze ratings
def analyze_ratings(ratings):
    if len(ratings) == 0:
        print("No ratings available.\n")
        return

    total = sum(ratings)
    avg = total / len(ratings)

    print("Average Song Rating:", avg)

    if avg >= 4:
        print("Your playlist is amazing!\n")
    elif avg >= 3:
        print("Your playlist is good.\n")
    else:
        print("Try adding better songs.\n")


# music star pattern
def music_pattern():
    print("\nMusic Energy Pattern")
    for i in range(1, 6):
        print("🎵" * i)


# music series
def music_series():
    print("\nTop Playlist Ranking")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")


# main program
def main():

    playlist = []
    ratings = []

    print("Welcome to Music Playlist Manager")

    name = input("Enter your name: ")
    print("Hello", name.upper(), "\n")

    while True:

        print("1. Add Song")
        print("2. View Playlist")
        print("3. Remove Song")
        print("4. Play Random Song")
        print("5. Analyze Ratings")
        print("6. Show Music Pattern")
        print("7. Show Music Series")
        print("8. Count Songs (Recursion)")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_song(playlist, ratings)

        elif choice == "2":
            view_playlist(playlist, ratings)

        elif choice == "3":
            remove_song(playlist, ratings)

        elif choice == "4":
            play_random_song(playlist)

        elif choice == "5":
            analyze_ratings(ratings)

        elif choice == "6":
            music_pattern()

        elif choice == "7":
            music_series()

        elif choice == "8":
            print("Total Songs:", count_songs(playlist), "\n")

        elif choice == "9":
            print("Enjoy your music!")
            break

        else:
            print("Invalid choice.\n")


main()
