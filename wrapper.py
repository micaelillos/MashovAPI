import json
import requests
import inital
import shutil
import matplotlib.pyplot as plt

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

def getSubjectList():
    url = inital.BASEURL + "grades"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'))
    grades = json.loads(response.text)
    gl=[]
    for grade in grades:
        try:
            if grade['subjectName'] not in gl:
                gl.append(grade['subjectName'])
        except:
            continue
    print(gl)



def getGradesGraphBySubject(subject=None):
    if subject == None:
        print("call me with one of the subjects from the list given in geSubjectList!")
        return 0
    if type(subject) != str:
        print('subject must be of type string!')
        return 0
    url = inital.BASEURL + "grades"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'))
    grades = json.loads(response.text)
    gi=1
    gx,gy=[],[]
    for grade in grades:
        try:
            if grade['subjectName'] == subject:
                gy.append(int(grade['grade']))
                gx.append(gi)
                gi+=1
        except:
            continue
    plt.title('grades in '+subject[::-1])
    plt.ylim(0,105)
    plt.plot(gx,gy,'b-')
    plt.plot(gx, gy, 'b.')
    plt.show()

def getGradesGraphAll():
    url = inital.BASEURL + "grades"
    response = requests.request("GET", url, data=inital.payload(), headers=inital.getHeader('GET'))
    grades = json.loads(response.text)
    gi=1
    gx,gy=[],[]
    for grade in grades:
        try:
            gy.append(int(grade['grade']))
            gx.append(gi)
            gi+=1
        except:
            continue
    plt.title('grades in all subjects')
    plt.ylim(0,105)
    plt.plot(gx,gy,'b-')
    plt.plot(gx, gy, 'b.')
    plt.show()


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