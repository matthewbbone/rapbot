from bs4 import BeautifulSoup
import requests as req

def generating(artist, title, save):
        artist = artist.lower().replace(" ", "%20")
        title = title.lower().replace(" ", "%20")
        generate_url = 'http://www.azlyrics.com/lyrics/'+artist+'/'+title +'.html'
        print(generate_url)
        processing(generate_url, artist, title, save)
        
def processing(generate_url, artist, title, save):
    response = req.get(generate_url, verify = False)
    read_lyrics = response.content
    soup = BeautifulSoup(read_lyrics, 'lxml')
    lyrics = soup.find_all("div", attrs={"class": None, "id": None})
    lyrics = [x.getText() for x in lyrics]
    printing(artist, title, save, lyrics)
    
def printing(artist, title, save, lyrics):    
    for x in lyrics:
        print(x, end="\n\n")
    if save == True:
        saving(artist, title, lyrics)
    elif save == False:
        pass
            
def saving(artist, title, lyrics):
        f = open(artist + '_' + title + '.txt', 'w')
        f.write("\n".join(lyrics).strip())
        f.close()