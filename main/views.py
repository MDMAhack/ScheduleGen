from django.shortcuts import render
import json
from django.http import HttpResponse
from algorithm import *

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

rooms = {}
profs = []
courses = []

def init_data(data):
    hours = ['09:00', '10:30', '13:00', '14:30', '16:00', '17:30']
    global rooms
    global profs
    global courses
    global grade_courses

    grade_courses = {'freshman':set(), 'sophomore':set(), 'junior':set(), 'senior':set()}
    rooms = {}
    profs = []
    courses = []



    for room_dic in data['rooms']:
        if not (room_dic['type'] in rooms.keys()):
            rooms[room_dic['type']] = []
        print('Fuck you', int(room_dic['capacity']))
        rooms[room_dic['type']].append(Room(int(room_dic['capacity']), room_dic['name'], []))

    for course_dic in data['courses']:
        section_list = []
        capacity = course_dic['capacity']
        course_name = course_dic['name']
        grade = course_dic['grade']
        course_id = course_dic['id']

        for section_number in range(int(course_dic['sectionCnt'])):
            class_list = []
            for class_dic in course_dic['classList']:
                class_list.append(class_dic['type'])
            section_id = course_name + str(section_number)
            tmp_section = Section(section_id, class_list)
            section_list.append(tmp_section)

        courses.append(Course(course_id, capacity, course_name, grade, section_list))
        grade_courses[grade].add(courses[-1])
        #print(grade + ' : ', grade_courses[grade])

    for prof_dic in data['profs']:
        time_list = []
        for i, isAvailable in enumerate(prof_dic['isAvailable']):
            if not isAvailable:
                time = str(i // 6 + 1) + hours[i % 6]
                time_list.append(time)
        profs.append(Prof(int(prof_dic['rank']), prof_dic['name'], time_list))

        for course_id in prof_dic['coursesAvailable']:
            for course in courses:
                if course.id == int(course_id):
                    course.profs.append(profs[-1])

@csrf_exempt
def generate(request):
    raw = request.body.decode('utf-8')
    data = json.loads(raw)
    #print(data)
    init_constants()
    init_data(data)
    #print(grade_courses)
    data = generate_for_grades(rooms, profs, courses, grade_courses)
    raw = json.dumps(data)
    #print(grade_courses)
    return HttpResponse(raw);

def index(request):
    return render(request, 'main/index.html')
