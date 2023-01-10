#!/usr/bin/python3
"""
Defines a class student
"""


class Student:
    """
    A class that represents student objects
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student
        Args:
            first_name (str): The first name of the student
            last_name (str): the last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Getting the dic representation of the student
        """
        return self.__dict__
