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

for course in courses:
    for prof in course.profs:
        if prof.status >s= prof.rank:
            continue
        for day in days:
            for hour in hours:
                if prof.is_occupied(day, hour):
                    continue
                rooms_assigned = True
                for _class in classes:
                    room_assigned = False
                    for room in rooms[_class.type]:
                         if not room.is_occupied(day, hour):
                             room_assigned = True
                             break
                    if not room_assigned:
