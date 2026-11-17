anime_type = ["RomCom", "Horror", "Isekai", "Adventure", "Sci-Fi"]
anime_title = []

while True:
    ans = input("Do you watch Anime? (Yes/No): ")

    if ans == "Yes":
        print("What type of Anime do you watch? Select from the list below:)")
        for x in anime_type:
            print(x)

        a_type = input("Type of Anime genre: ")

        title = input("What is the title of the Anime?: ")
        anime_title.append(title)
        continue
    
    else:
        print("Thank you")
        break