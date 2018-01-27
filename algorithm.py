class Room:
    def __init__(self, capacity, name, occupied):
        self.capacity = capacity
        self.name = ''
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
    global days
    global hours
    #grade_courses = {'freshman':set(), 'sophomore':set(), 'junior':set(), 'senior':set()}
    grades = ['freshman', 'sophomore', 'junior', 'senior']
    days = [[5], [2, 4], [1, 3, 5]]
    hours = ['09:00', '10:30', '13:00', '14:30', '16:00', '17:30']


def generate_for_grades(rooms, profs, courses, grade_courses):
    answer = []
    # TODO prof.occupied
    for grade in grades:
        occupied = []
        for course in grade_courses[grade]:
            done = False
            section = course.sections[0]
            classes = section.classes
            n = len(classes)
            for prof in course.profs:
                if prof.status >= prof.rank:
                    continue
                for hour in hours:
                    assigned_room = []
                    for i in range(n):
                        for room in rooms[classes[i]]:
                            if room.capacity >= course.capacity and not (room.is_occupied(days[n][i], hour) and
                            prof.is_occupied(days[n][i], hour) and (str(days[n][i]) + str(hour)) in occupied):
                                assigned_room.append(room)
                                break

                    if len(assigned_room) == n:
                        for i in range(n):
                            assigned_room[i].occupy(days[n][i], hour)
                            prof.occupy(days[n][i], hour)
                            occupied.append(str(days[n][i]) + str(hour))
                            answer.append(course.name + ' ' + assigned_room[i].name + ' ' + str(days[n][i]) + ' ' + hour)
                        done = True
                        break
                if done:
                    break


            del course.sections[0]
    return answer
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
