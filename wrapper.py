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
    gradecount = len(grades)
    for grade in grades:
        try:
            sumofgrades += float(grade['grade'])
        except:
            print("No Grade")
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

# Todo Bagrut Grades
# Todo Timetable
# Todo Messages
# ect'