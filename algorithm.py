class Room:
    def __init__(self):
        self.capacity = 0
        self.name = ''
        self.occupied = []

    def is_occupied(day, hour):
        return ((str(day) + str(hour)) in occupied)

    def occupy(day, hour):
        occupied.append(str(day) + str(hour))

class Course:
    def __init__(self):
        self.capacity = 0
        self.name = ''
        self.sections_num = 0
        self.grade = 0
        self.classes = []
        self.profs = []


class Prof:
    def __init__(self):
        self.rank = 0
        self.status = 0
        self.name = ''
        self.occupied = []

    def is_occupied(day, hour):
        return ((str(day) + str(hour)) in occupied)

    def occupy(day, hour):
        occupied.append(str(day) + str(hour))

class Class:
    def __init__():
        self.time = ''
        self.id = 0
        self.type = ''

grade_courses = []
grades = ['freshman', 'sophomore', 'junior', 'senior']
days = [[5], [2, 4], [1, 3, 5]]
hours = ['09:00', '10:30', '13:00', '14:30', '16:00', '17:30']

class Table:
    def __init__(self):

def generate_for_grades():
    for grade in grades:
        occupied = []
        for course in grade_courses[grade]:
            section = course.sections[0]
            classes = section.classes
            n = len(classes)
            for prof in course.profs:
                if prof.status >= prof.rank:
                    continue

                for hour in hours:
                    assigned_room = []
                    for i in range(n):
                        for room in rooms[classes[i].type]:
                            if room.capacity >= course.capacity
                            and not (room.is_occupied(days[n][i], hour)
                            and prof.is_occupied(days[n][i], hour
                            and (str(day) + str(hour)) in occupied):
                                assigned_room.append(room)
                                break

                    if len(assigned_room) == n:
                        for i in range(n):
                            assigned_room[i].occupy(days[n][i], hour)
                            prof.occupy(days[n][i], hour)
                            occupied.append(str(day) + str(hour))
                            answer.append(course.name + ' ' + assigned_room[i]
                            + ' ' + days[n][i] + ' ' + hour +)

            del course.sections[0]
'''
for course in courses:
    for section in course.sections:
        done = False
        for prof in course.profs:
            if prof.status >= prof.rank:
                continue
            for day in days:
                for hour in hours:
                    classes = section.classes
                    if prof.is_occupied(day, hour, len(classes)):
                        continue
                    rooms_assigned = []
                    for _class in classes:
                        room_assigned = False
                        for room in rooms[_class.type]:
                             if not room.is_occupied(day, hour, len(classes)) and room.capacity >= course.capacity:
                                 room_assigned = True
                                 rooms_assigned.append(room)
                                 break
                        if not room_assigned:
                            break

                    if len(rooms_assigned) == len(classes):
                        prof.occupy(day, hour, len(classes))
                        prof.status = prof.status + 1
                        for room in rooms_assigned:
                            room.occupy(day, hour, len(classes))
                        done = True
                        break
                    else:
                        rooms_assigned = []
                if done:
                    break
            if done:
                break
'''
