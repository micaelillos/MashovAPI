import requests
import config as cfg

#get payload info from config file
def payload():
    return ({"username": cfg.mashov["username"],
             "password": cfg.mashov["password"],
             "semel":cfg.mashov["semel"],
             "year": cfg.mashov["year"]})

# logins and gets token & cookie
login = requests.post('https://web.mashov.info/api/login',json=payload())
token = login.headers.get('x-csrf-token')
cookie = login.headers.get('Set-Cookie')

# returns required header with appropriate method
def getHeader(method, token=token,cookie=cookie):
    return ({
    'method': str(method),
    'x-csrf-token': token,
    'cookie': cookie
    })

#user id
userid = login.text[127:163]
#base url
BASEURL = "https://web.mashov.info/api/students/"+userid+"/"
OtherBase = "https://web.mashov.info/api/user/"+userid+"/"
