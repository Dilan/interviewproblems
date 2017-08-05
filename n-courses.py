# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites,
# for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1. So it is impossible.

def create_graph(list):
    courses = {}
    for pair in list:
        if pair[1] not in courses:
            courses[pair[1]] = { "list": [], "id": pair[1], "visited": False }
        if pair[0] not in courses:
            courses[pair[0]] = { "list": [], "id": pair[0], "visited": False }

        courses[pair[0]]['list'].append(courses[pair[1]])
    return courses

def dfs(course, parents, sorted):
    if not course['visited']:
        course['visited'] = True

        for item in course['list']:
            if item['id'] in parents:
                print 'Error.... in', course['id'], 'and', item['id']
                return False

            # remember all parents for this item
            parents[course['id']] = True

            if not dfs(item, parents, sorted):
                return False

        sorted.append(course['id'])

    return True

def is_it_possible_to_finish_all_courses(list):
    courses = create_graph(list)

    sorted = []
    for id in courses.keys():
        if not dfs(courses[id], {}, sorted):
            return False

    print sorted

    return True

# print is_it_possible_to_finish_all_courses([[0,1], [1,0]])
# print is_it_possible_to_finish_all_courses([[0,1], [1,2], [1,3], [2,4]])
print is_it_possible_to_finish_all_courses([[0,1], [1,2], [1,3], [2,4], [3,0]])
# print is_it_possible_to_finish_all_courses([[0,1], [2,3]])
print is_it_possible_to_finish_all_courses([[4,10], [3,6], [3,4]])

