from repositories.course_repository import CourseRepository


class DatabaseCourseRepository(CourseRepository):
    """
    STUB for future Database implementation.
    This shows the repository layer is future-proof.
    """
    
    def __init__(self):
        print("DatabaseCourseRepository initialized (STUB)")

    def save(self, course):
        raise NotImplementedError("Database implementation coming soon!")

    def find_by_id(self, course_id):
        raise NotImplementedError("Database implementation coming soon!")

    def find_all(self):
        raise NotImplementedError("Database implementation coming soon!")

    def delete(self, course_id):
        raise NotImplementedError("Database implementation coming soon!")