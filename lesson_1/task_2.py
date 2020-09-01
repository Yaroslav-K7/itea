library_countries = {
    "Ukraine": "Kyiv",
    "Russia": "Moscow",
    "Belarus": "Minsk",
    "Franse": "Paris",
    "Italy": "Rome"
}
countries = ["Ukraine", "Russia", "Belarus", "France", "Italy"]

for countr in countries:
    if countr in library_countries:
        print(library_countries[countr])
