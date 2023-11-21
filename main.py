#We don't need graphical user interface. Only Command User Interface. 
import requests
from send_email import send_email

api_key='6df06dce864941e58549c6f084c62336'
api_url='https://newsapi.org/v2/everything?domains=wsj.com&apiKey=6df06dce864941e58549c6f084c62336'


#Make request
request = requests.get(api_url)
#Get dictionary
content = request.json()

#Acces the article titles and description
body = ''
for articles in content["articles"][:20]:
    if articles["title"] is not None:
        #Create articles to send message:
        #We need the titles and the descriptioons to contain the data.   
        body = "Subjetc: Today's news" + '\n' + body + articles["title"] + '\n' + articles["description"] + '\n' + articles["url"] + 2*'\n'
    
body = body.encode('utf-8')
#Out of the loop cause 1 email not a lot. 
send_email(message = body)