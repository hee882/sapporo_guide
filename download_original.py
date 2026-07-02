import urllib.request

urls = {
    "farm_tomita.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Farm_Tomita_Irodori_Field.jpg",
    "blue_pond.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Blue_pond_Biei_Hokkaido_Japan02bs.jpg",
    "otaru.jpg": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Otaru_Canal_in_Summer.jpg",
    "jigokudani.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/26/Noboribetsu_Jigokudani_04.jpg",
    "susukino.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/82/Nikka_Susukino_Sapporo01s.jpg"
}

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
]
urllib.request.install_opener(opener)

for name, url in urls.items():
    try:
        urllib.request.urlretrieve(url, "images/" + name)
        print("Downloaded " + name)
    except Exception as e:
        print("Failed to download " + name + ": " + str(e))
