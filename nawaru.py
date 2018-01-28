while has unused permutation:
    days = list unused permutation of days
    for hour in hours:
        assigned_room = []
        for i in range(n):
            for room in rooms[classes[i]]:
                if room.capacity >= course.capacity:
                    if not (room.is_occupied(days[i], hour) or prof.is_occupied(days[i], hour) or ((str(days[i]) + str(hour)) in occupied)):
                        assigned_room.append(room)
                        break

        if len(assigned_room) == n:
            for i in range(n):
                assigned_room[i].occupy(days[i], hour)
                prof.occupy(days[i], hour)
                occupied.append(str(days[i]) + str(hour))
                answer.append(course.name + ' ' + assigned_room[i].name + ' ' + str(days[i]) + ' ' + hour)
            prof.status = prof.status + 1
            done = True
            break

days1 = [[1], [2], [3], [4], [5]]
days2 = [[1, 3], [2, 4], [1, 4], [1, 5], [2, 5], [3, 5], [4, 5], [1, 2], [2, 3], [3, 4]]
days3 = [[1, 3, 5], [1, 3, 4], [1, 2, 4], [1, 2, 5], [2, 4, 5], [2, 3, 5]]

{'sections':[
    {
        'section_id':
        'course_name':
        'prof':
        'classes': [{
            'day':
            'hour':
            'room':
        },]
    },
]}
