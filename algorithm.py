from random import randint
import random

class Room:
    def __init__(self, capacity, name, occupied):
        self.capacity = capacity
        self.name = name
        self.occupied = []

    def is_occupied(self, day, hour):
        return ((str(day) + str(hour)) in self.occupied)

    def occupy(self, day, hour):
        self.occupied.append(str(day) + str(hour))

class Course:
    def __init__(self, id, capacity, name, grade, sections):
        self.id = id
        self.capacity = capacity
        self.name = name
        self.grade = grade
        self.sections = sections
        self.profs = []

    def __str__(self):
        return self.name


class Prof:
    def __init__(self, rank, name, occupied):
        self.rank = rank
        self.status = 0
        self.name = name
        self.occupied = occupied

    def is_occupied(self, day, hour):
        return ((str(day) + str(hour)) in self.occupied)

    def occupy(self, day, hour):
        self.occupied.append(str(day) + str(hour))

class Section:
    def __init__(self, id, classes):
        self.id = id
        self.classes = classes

def init_constants():
    #global grade_courses
    global grades
    global hours
    global day_str
    global hour_end
    #grade_courses = {'freshman':set(), 'sophomore':set(), 'junior':set(), 'senior':set()}
    grades = ['freshman', 'sophomore', 'junior', 'senior']
    hours = ['09:00', '10:30', '13:00', '14:30', '16:00', '17:30']
    hour_end = {'09:00':'-10:15', '10:30':'-11:45', '13:00':'-14:15', '14:30':'-15:45', '16:00':'-17:15', '17:30':'-18:15'}
    day_str = {'1':'MON', '2':'TUE', '3':'WED', '4':'THU', '5':'FRI'}


def generate_for_grades(rooms, profs, courses, grade_courses):
    for room in rooms['lecture']:
        print(room.name)
    days_comb = [[]]
    days_comb.append([[1], [2], [3], [4], [5]])
    days_comb.append([[1, 3], [2, 4], [1, 4], [1, 5], [2, 5], [3, 5], [4, 5], [1, 2], [2, 3], [3, 4]])
    days_comb.append([[1, 3, 5], [1, 3, 4], [1, 2, 4], [1, 2, 5], [2, 4, 5], [2, 3, 5]])
    answer = []
    data = {}
    data['sections'] = []
    # TODO prof.occupied
    # TODO room.type
    for grade in grades:
        occupied = []
        for classes_cnt in range(3, 0, -1):
            for course in grade_courses[grade]:
                if len(course.sections) == 0:
                    continue
                done = False
                section = course.sections[0]
                classes = section.classes
                n = len(classes)
                if classes_cnt != n:
                    continue
                for prof in course.profs:
                    if prof.status >= prof.rank:
                        continue
                    if n == 1:
                        random.shuffle(days_comb[n])
                    elif n == 2:
                        p1 = randint(0, 2)
                        days_comb[n][0], days_comb[n][p1] = days_comb[n][p1], days_comb[n][0]
                        p2 = randint(1, 2)
                        days_comb[n][1], days_comb[n][p2] = days_comb[n][p2], days_comb[n][1]
                    else:
                        random.shuffle(days_comb[n])
                    for days in days_comb[n]:
                        for hour in hours:
                            assigned_room = []
                            for i in range(n):
                                for room in rooms[classes[i]]:
                                    if room.capacity >= course.capacity:
                                        if not (room.is_occupied(days[i], hour) or prof.is_occupied(days[i], hour) or ((str(days[i]) + str(hour)) in occupied)):
                                            assigned_room.append(room)
                                            break

                            if len(assigned_room) == n:
                                tmp_list = []
                                for i in range(n):
                                    assigned_room[i].occupy(days[i], hour)
                                    prof.occupy(days[i], hour)
                                    occupied.append(str(days[i]) + str(hour))
                                    answer.append(course.name + ' ' + assigned_room[i].name + ' ' + str(days[i]) + ' ' + hour)
                                    tmp_list.append({'day':day_str[str(days[i])], 'hour':(hour+hour_end[hour]), 'room':assigned_room[i].name})
                                tmp_dict = {'section_id':section.id, 'classes':tmp_list, 'prof':prof.name, 'course_name':course.name}
                                data['sections'].append(tmp_dict)
                                prof.status = prof.status + 1
                                done = True
                                break
                        if done:
                            break
                    if done:
                        break

                del course.sections[0]

    #answer = generate_others(rooms, profs, courses, answer)
    #return answer
    data = generate_others(rooms, profs, courses, answer, data)
    return data

def generate_others(rooms, profs, courses, answer, data):
    days_comb = []
    days_comb.append([[1], [2], [3], [4], [5]])
    days_comb.append([[1, 3], [2, 4], [3, 5], [1, 4], [1, 5], [2, 5], [4, 5], [1, 2], [2, 3], [3, 4]])
    days_comb.append([[1, 3, 5], [1, 3, 4], [1, 2, 4], [1, 2, 5], [2, 4, 5], [2, 3, 5]])
    for course in courses:
        print(course.name)
        for section in course.sections:
            done = False
            classes = section.classes
            n = len(classes)
            for prof in course.profs:
                if prof.status >= prof.rank:
                    continue
                if n == 1:
                    random.shuffle(days_comb[n])
                elif n == 2:
                    p1 = randint(0, 2)
                    days_comb[n][0], days_comb[n][p1] = days_comb[n][p1], days_comb[n][0]
                    p2 = randint(1, 2)
                    days_comb[n][1], days_comb[n][p2] = days_comb[n][p2], days_comb[n][1]
                else:
                    random.shuffle(days_comb[n])

                for days in days_comb[n]:
                    for hour in hours:
                        assigned_room = []
                        for i in range(n):
                            for room in rooms[classes[i]]:
                                if room.capacity >= course.capacity:
                                    if not (room.is_occupied(days[i], hour) or prof.is_occupied(days[i], hour)):
                                        assigned_room.append(room)
                                        break

                        if len(assigned_room) == n:
                            tmp_list = []
                            for i in range(n):
                                assigned_room[i].occupy(days[i], hour)
                                prof.occupy(days[i], hour)
                                answer.append(course.name + ' ' + assigned_room[i].name + ' ' + str(days[i]) + ' ' + hour)
                                tmp_list.append({'day':day_str[str(days[i])], 'hour':(hour+hour_end[hour]), 'room':assigned_room[i].name})
                            tmp_dict = {'section_id':section.id, 'classes':tmp_list, 'prof':prof.name, 'course_name':course.name}
                            data['sections'].append(tmp_dict)

                            prof.status = prof.status + 1
                            done = True
                            break
                    if done:
                        break

                if done:
                    break
    return data
