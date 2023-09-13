#!/usr/bin/python3
"""
Student class v 2
"""


class Student():
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """init func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if type(attrs) == list:
            for attr in attrs:
                if not isinstance(attr, str):
                    return self.__dict__
            return{k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
