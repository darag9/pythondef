from functions import *

# 1. Library Book Tracker
def test_library():
    library.clear()
    add_book("1984", "George Orwell", 328)
    assert "1984" in library
    assert find_book("Unknown") == "Book not found."
    show_books()

# 2. Student Grade Manager
def test_grades():
    students.clear()
    print(add_student("Alice"))
    print(add_student("pepe"))
    print(add_student("pepe"))
    add_grade("pepe", 70)
    add_grade("pepe", 70)
    add_grade("Alice", 90)
    add_grade("Alice", 80)
    assert get_average("Alice") == 85.0

# 3. Restaurant Menu Editor
def test_menu():
    menu.clear()
    add_dish("Pizza", 10.0, 5, True)
    add_dish("Salad", 5.0, 10, False)
    change_availability("Salad", True)
    assert total_available_price() == 100.0

# 4. Warehouse Box Counter
def test_warehouse():
    warehouse.clear()
    add_box("BoxA", 5)
    update_quantity("BoxA", 8)
    assert has_enough("BoxA", 8) is True

# 5. Movie Rating System
def test_movies():
    movies.clear()
    add_movie("Inception")
    add_movie("Inception")
    rate_movie("Inception", 5)
    rate_movie("Inception", 4)
    assert average_rating("Inception") == 4.5

# 6. Online Course Tracker
def test_courses():
    courses.clear()
    add_course("Python", 40, 20)
    assert "Python" in filter_by_hours(40)

# 7. To-Do List Organizer
def test_todos():
    todos.clear()
    add_task("Task1", "high")
    complete_task("Task1")
    filtered = filter_tasks(priority="high", status=True)
    assert len(filtered) == 1

# 8. Digital Wallet
def test_wallet():
    wallet.clear()
    add_expense("food", 100)
    add_expense("transport", 50)
    percentages = expense_percentages()
    print(percentages)
    assert round(percentages, 1) == 66.7

# 9. Pet Adoption Center
def test_pets():
    pets.clear()
    add_pet("Buddy", "dog", 5)
    older = older_than(3)
    assert any(p["name"] == "Buddy" for p in older)

# 10. Gym Membership System
def test_gym():
    members.clear()
    register_member("John", "monthly", "late")
    assert "John" in unpaid_members()

def main():
    # test_grades()
    # print(get_average("Alice"))
    # print(get_average("pepe"))
    # print(students)
    
    test_wallet()
main()
