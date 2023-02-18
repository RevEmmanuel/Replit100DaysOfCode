import csv, os


with open("100MostStreamedSongs.csv", encoding='utf-8') as file:
  reader = csv.DictReader(file)

  for row in reader:
    os.chdir("C:/Users/user/Documents/Replit 100 Days Of Code/Python/Day56Creations")
    dir = os.listdir()
    artist = row["Artist(s)"].title()
    print(artist)
    if artist not in dir:
      os.mkdir(artist)
    song = row["Song"]
    print(row["Song"])
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()
