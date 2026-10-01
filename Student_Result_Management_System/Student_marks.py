class Student:
    COLLEGE_NAME = "Aditya Institute of Technology"
    total_students = 0
    PASS_MARKS = 35
    MAX_SUBJECTS = 5

    def __init__(self,name,roll_number,branch,marks=None):
        self.name = name
        self._roll_number = roll_number
        self._branch = branch
        first_marks = marks.copy() if marks is not None else {}
        if len(first_marks) > Student.MAX_SUBJECTS:
            raise ValueError("Subjects exceeded")
        self.__marks = first_marks
        Student.total_students += 1

    #has passed !!!

    #Roll Number
    @property
    def roll_number(self):
        return self._roll_number
    
    def average(self):
        if len(self.__marks) == 0:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)
    
    def grade(self):
        x = self.average()
        if x >= 90:
            return "A+"
        elif x >= 75:
            return "A"
        elif x >= 60:
            return "B"
        elif x >=35:
            return "C"
        else:
            return "F"
    

    def add_marks(self, sub, score):
        if sub not in self.__marks and len(self.__marks) >= Student.MAX_SUBJECTS:
            raise ValueError(f"Cannot add '{sub}'. Reached maximum limit of {Student.MAX_SUBJECTS} subjects!")
        if not (0 <= score <= 100):
            raise ValueError(f"Mark must be between 0 and 100, got {score}")
        self.__marks[sub] = score
    
    def get_marks(self):
        return self.__marks.copy()
    
    def has_passed(self):
        return all(x >= Student.PASS_MARKS for x in self.__marks.values())
    
    def change_branch(self, new_branch):
        old = self._branch
        new = new_branch
        self._branch = new_branch
        print(f"{self.name} moved from {old} to {new}")
    
    @classmethod
    def get_total_students(cls):
        return f"Total students: {cls.total_students}"
    
    @staticmethod
    def is_valid_mark(mark):
        return 0<= mark <= 100
    
    def __str__(self):
        return f"Student[{self._roll_number}] {self.name} | {self._branch} | Avg: {self.average()} | Grade: {self.grade()}"





    
