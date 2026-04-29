class CourseBuilder:
    """Builder Pattern - constructs complex Course objects step by step"""
    def __init__(self, course_id: int, title: str, instructor):
        self._course_id = course_id
        self._title = title
        self._instructor = instructor
        self._has_quizzes = False
        self._has_certificate = False
        self._has_projects = False

    def add_quizzes(self):
        self._has_quizzes = True
        return self

    def add_certificate(self):
        self._has_certificate = True
        return self

    def add_projects(self):
        self._has_projects = True
        return self

    def build(self):
        print(f"✅ Course '{self._title}' built with:")
        if self._has_quizzes:
            print("   • Quizzes included")
        if self._has_certificate:
            print("   • Certificate included")
        if self._has_projects:
            print("   • Projects included")
        return f"Course: {self._title} (ID: {self._course_id})"