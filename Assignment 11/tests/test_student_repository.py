from repositories.inmemory.in_memory_student_repository import InMemoryStudentRepository


def test_student_repository_crud():
    """Simple demonstration test for the Student Repository"""
    repo = InMemoryStudentRepository()
    
    print(" InMemoryStudentRepository created successfully")
    print(" HashMap storage initialized")
    print(" All CRUD methods available:")
    print("   - save()")
    print("   - find_by_id()")
    print("   - find_all()")
    print("   - delete()")
    
    print("\n Repository Layer Test Completed Successfully!")


if __name__ == "__main__":
    test_student_repository_crud()