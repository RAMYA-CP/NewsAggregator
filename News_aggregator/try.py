import requests 
from bs4 import BeautifulSoup
def content():
    urls=requests.get("https://www.bbc.com/news")
    soup=BeautifulSoup(urls.text,'html.parser')
    t=soup.find("div",{'class':'gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international'})
    f=t.select('h3')
    content=[]
    for l in f[2:]:
        content.append(l.text)
    an=t.find_all('a',{'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'})
    links=[]
    for ik in an:
        link=ik.get('href')
        if "https://www.bbc.co.uk" not in link:
            link="https://www.bbc.co.uk"+link
        links.append(link)
    im=t.select('img')
    images=[]
    for i in im[1:]:
        tu=i.get('data-src')
        tu=str(tu)
        tu=tu.replace('{width}','170')
        images.append(tu)
    conima=zip(links,content,images)
    for i,j,k in conima:
        print(i,j,k)
content()