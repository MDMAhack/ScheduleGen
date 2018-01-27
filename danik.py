class Room:
    def __init__():
        this.capacity = 0
        this.name = ''
        this.occupied = []

class Course:
    def __init__():
        this.capacity = 0
        this.name = ''
        this.sections_num = 0
        this.grade = 0
        this.classes = []
        this.profs = []

class Prof:
    def __init__():
        this.rank = 0
        this.status = 0
        this.name = ''
        this.occupied = []

class Class:
    def __init__():
        this.time = ''
        this.id = 0
        this.type = ''

days = [1, 3, 5, 2, 4, 6]

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
                        is_assigned = False
                        for room in rooms[_class.type]:
                             if not room.is_occupied(day, hour, len(classes)):
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
