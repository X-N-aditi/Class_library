class student:
    class student_details:
        def __init__(self, fname, lname):
            self.fname = input("Enter your first name: ")
            self.lname = input("Enter your last name: ")
    s1 = student_details("fname", "lname")
    print(s1.fname, s1.lname)
    class student_details2:
        def __init__(self, student_id, course, branch, year):
            self.student_id = input("Enter your student ID: ")
            self.course = input("Enter your course: ")
            self.branch = input("Enter your branch: ")
            self.year = input("Enter your year: ")
    s2 = student_details2("student_id", "course", "branch", "year")
    print(s2.student_id, s2.course, s2.branch, s2.year)
    class lend_book:
        def __init__(self, book_name):
            self.book_name = input("Enter books name: ")
    s3 = lend_book("book_name")
    print(s3.book_name)
    



