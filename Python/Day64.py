class Job:

    name = ""
    salary = 0.00
    hours_worked = 0

    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_self(self):
        print(f"I am a {self.name} who earns {self.salary}. I work for {self.hours_worked} hours.")

class Doctor(Job):
    experience = ""
    specialty = ""

    def __init__(self, salary, hours_worked, experience, specialty):
        self.experience = experience
        self.specialty = specialty
        self.name = "Doctor"
        self.salary = salary
        self.hours_worked = hours_worked

    def print_self(self):
        print(f"I am a {self.name} who earns {self.salary}. My specialty is {self.specialty} and I work for {self.hours_worked} hours.")

class Teacher(Job):
    subject = ""
    position = ""

    def __init__(self, salary, hours_worked, subject, position):
        self.subject = subject
        self.position = position
        self.name = "Teacher"
        self.salary = salary
        self.hours_worked = hours_worked
        
    def print_self(self):
        print(f"I am a {self.name} who earns {self.salary}. My position is {self.subject} {self.position} and I work for {self.hours_worked} hours.")


lawyer = Job("Lawyer", 4500.60, 8)
lawyer.print_self()

doctor = Doctor(450.60, 12, "7", "Neurosurgeon")
doctor.print_self()

teacher = Teacher(2000, 8, "Computer Science", "Teacher")
teacher.print_self()

