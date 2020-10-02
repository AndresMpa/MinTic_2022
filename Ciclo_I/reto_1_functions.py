"""
PROBLEMA #I:
Un profesor debe calcular el promedio de la nota de quinces de sus estudiantes para
subirla a la plataforma de notas finales. Sin embargo, el profesor acordó con sus
estudiantes que los ayudará eliminando la peor de las 5 notas antes de calcular el
promedio que finalmente resportará. Adicionalmente, el profesor se ha dado cuenta
que las notas registradas en su plantailla se encuentra en una escala de números
enteros entre 0 y 100, pero la plataforma está diseñada para recibir el promedio
únicamente en la escala estandar de la universidad de 0 a 5, redondeado a 2 decimales.

REQUERIMIENTOS:
Escriba una funcion que reciba una cadena con el codigo alfanumerico del estudiante
y cinco números enteros (n1, n2, n3, n4, n5), que representa las notas de los quinces
del semestre y retorne una cadena de caracteres que le proporciona al profesor la
información que desea obtener. La cadena debe de tener la siguiente estructura: "El
promedio ajustado del estudiantes [codigo] es [promedio]" donde, el promedio reportado
debe cumplir con las siguientes especificaciones mencionadas anteriormente (redondeando
a dos decimales, en escala de 0 a 5 y eliminando del calculo la peor de las 5 notas del
estudiante).

#TEST
    print(nota_quices("AA0010276", 19, 90, 38, 55, 68))
    print(nota_quices("IS0020162", 37, 10, 50, 19, 79))
    print(nota_quices("BIO220181", 45, 46, 33, 74, 22))
    print(nota_quices("IQ1022018", 57, 100, 87, 93, 21))
    print(nota_quices("MA0020152", 5, 14, 76, 91, 5))

#OUTPUT
    El promedio ajsutado del estudiante AA0010276 es: 3.14
    El promedio ajustado del estudiante IS0020162 es: 2.31
    El promedio ajustado del estudiante BIO220181 es: 2.48
    El promedio ajustado del estudiante IQ1022018 es: 4.21
    El promedio ajustado del estudiante MA0020152 es: 2.33
"""


def adjust_grades(nota_actual):
    return nota_actual * 0.05


def worst_grade(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5):
    worst = min(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5)
    return quiz_1 + quiz_2 + quiz_3 + quiz_4 + quiz_5 - worst


def final_grade_calc(grades):
    return grades / 4


def quiz_grades(code, grade_1, grade_2, grade_3, grade_4, grade_5):
    grade_1 = adjust_grades(grade_1)
    grade_2 = adjust_grades(grade_2)
    grade_3 = adjust_grades(grade_3)
    grade_4 = adjust_grades(grade_4)
    grade_5 = adjust_grades(grade_5)

    nota_final = final_grade_calc(worst_grade(grade_1, grade_2, grade_3, grade_4, grade_5))

    return "El promedio ajustado del estudiante " + code + " es: " + str(round(nota_final, 2))


print(quiz_grades("AA0010276", 19, 90, 38, 55, 68))
print(quiz_grades("IS0020162", 37, 10, 50, 19, 79))
print(quiz_grades("BIO220181", 45, 46, 33, 74, 22))
print(quiz_grades("IQ1022018", 57, 100, 87, 93, 21))
print(quiz_grades("MA0020152", 5, 14, 76, 91, 5))
