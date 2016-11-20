# import libraries and other files

import load as loader
import ptp, visual, csv

debug = True
if debug or raw_input('Enter def for default input or enter to continue manually: ') == 'def':
    students = loader.load_students('studenten_roostering.csv')
    courses = loader.load_courses('vakken.csv', students)
    rooms = loader.load_rooms('zalen.csv')
else:
    student_file = raw_input('Student input file: ')
    while not student_file:
        student_file = raw_input('Student input file(CSV Format): ')

    students = loader.load_students(student_file)

    course_file = raw_input('Course input file: ')
    while not course_file:
        course_file = raw_input('Course input file(CSV Format): ')

    courses = loader.load_courses(course_file, students)

    room_file = raw_input('Room input file: ')
    while not room_file:
        room_file = raw_input('Room input file(CSV Format): ')

    rooms = loader.load_rooms(room_file)


schedule = loader.load_schedule(rooms)

print '\n\tDONE LOADING!\n'

#
#
#   Put all loaded information into the algorithm
#

schedule_by_alg =ptp.alg(students, courses, rooms, schedule)

# test voor basic hillclimber algorithm
#print "HILLCLIMBER ELEMENTS"
b_hc = ptp.basic_hillclimber(schedule_by_alg, courses, 148)

#print [1,2,3,4] == [1,2,4,3]


#
#
#   Quick output function to get an easy schedule overview
#

def write_csv(schedule):
    with open("output_files/schedule2.csv", "wb") as csvfile:
        cursor = csv.writer(csvfile)

        for i, roomslot in enumerate(schedule):
            if roomslot.course:
                cursor.writerow([roomslot.day, roomslot.time, roomslot.room, roomslot.course.name, roomslot.type])

        print "Output file generated!"

write_csv(schedule)
