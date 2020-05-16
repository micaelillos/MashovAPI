import json
import requests
import inital
import shutil

# gets average of grades
def getGradesAvg():
    url = inital.BASEURL + "grades"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'))
    grades = json.loads(response.text)
    sumofgrades = 0
    for grade in grades:
        sumofgrades += float(grade['grade'])
    avg = sumofgrades / float(len(grades))
    return avg

#gets user picture
def getPicture():
    url = inital.OtherBase + "picture"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'),  stream=True)
    response.raw.decode_content = True
    with open('user.jpeg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)



##Todo Bagrut Grades
##Todo Timetable
##Todo Messages
## ect'