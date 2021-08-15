def area_calc(ancho, alto):
    area: object = ancho * alto
    return area


width = 10
height = 12

print(area_calc(width, height))


# this version is better because it will accept
# both lists and dictionaries.

def mean(value):
    if type(value) == dict:  # comparing datatype to dic (dictionary datatype)
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


student_grades = {"Marry": 9.1, "Jose": 38, "John": 7.5}
student_scores = [9.1, 38, 8.8, 7.5]

print(mean(student_grades))  # average from dictionary

print(mean(student_scores))  # average from list
