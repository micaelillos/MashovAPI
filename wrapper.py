import json
import requests
import inital
import shutil

# list of schools API
school = requests.get("https://web.mashov.info/api/schools")
listOfSchools = json.loads(school.text)

# gets average of grades
def getGradesAvg():
    url = inital.BASEURL + "grades"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'))
    grades = json.loads(response.text)
    sumofgrades = 0
    gradecount = len(grades)
    for grade in grades:
        try:
            sumofgrades += float(grade['grade'])
        except:
            gradecount = gradecount-1
    avg = sumofgrades / gradecount
    return avg


# gets user picture
def getPicture():
    url = inital.OtherBase + "picture"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'), stream=True)
    response.raw.decode_content = True
    with open('user.jpeg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


def get_class_list():
    url = inital.BASEURL + "alfon"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'), stream=True)
    student_list = json.loads(response.text)
    name_list = []
    for student in student_list:
        name_list.append(student['privateName'] + ' ' + student['familyName'])
    print(name_list)
    print(len(name_list))

def getBagrut():
    url = inital.BASEURL + "bagrut/grades"
    response = requests.request("GET", url, data=inital.payload (), headers=inital.getHeader ('GET'))
    bagrutGrades = json.loads(response.text)
    for grade in bagrutGrades:
        try:
            print(f"{grade['name']}->{grade['final']}")
        except:
            continue

def getSchools():
    for school in listOfSchools:
        print(f"{school['name']} -> {school['semel']}")

# Todo Timetable
# Todo Messages
# ect'