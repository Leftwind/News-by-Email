#We don't need graphical user interface. Only Command User Interface. 
import requests

api_key='6df06dce864941e58549c6f084c62336'
api_url='https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6df06dce864941e58549c6f084c62336'


#Nake request
request = requests.get(api_url)
#Get dictionary
content = request.json()
#Acces the article titles and description
for articles in content["articles"]:
    print(articles["title"])
    print(articles["description"])