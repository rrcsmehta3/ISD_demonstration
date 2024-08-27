"""
Description: Unit tests for the Course class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_course.py
"""
import unittest
 
from department.department import Department
from course.course import Course, course
class Testclient(unittest.TestCase):
    def test_init_valid(self):
        course = Course("Intermedite software development", Department.COMPUTER_SCIENCE,6)