import xml.etree.ElementTree as Element_Tree

# Load and parse the XML file
tree = Element_Tree.parse("movie.xml")
root = tree.getroot()

# Listing all child tags of the movie element
print("\nListing all child tags of the <movie> element:\n")

for movie in root.iter("movie"):
    print(f"Movie Title: {movie.get('title')}")
    for child in movie:
        print(f" - {child.tag}")

# Printing out movie descriptions using itertext()
print("\nPrinting all movie descriptions:\n")

for movie in root.iter("movie"):
    description = movie.find("description")
    if description is not None:
        print(f"{movie.get('title')}: {''.join(description.itertext()).strip()}")

# Counting favorite and non-favorite movies
favorite_count = 0
non_favorite_count = 0

for movie in root.iter("movie"):
    favorite_status = movie.get("favorite", "False").lower()
    if favorite_status == "true":
        favorite_count += 1
    else:
        non_favorite_count += 1

print("\nMovie Favorites Count:")
print(f" - Favorite Movies: {favorite_count}")
print(f" - Non-Favorite Movies: {non_favorite_count}")
