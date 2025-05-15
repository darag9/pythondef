
# 1. Library Book Tracker
library:list=[]

def add_book(title:str="",author:str="",pages:int=0)->list:
    if pages > 0:    
        for book in library:
            if book == title.lower():
                print("The book you tried to add was already in the library.")
                return library
        library.append(title)
        library.append(author)
        library.append(pages)
        return library
    else:
        print(f"Book pages must be positive.")

def find_book(title:str="")->None:
    for book in library:
        if book == title.lower():
            return "Book was found."
    else:
        return f"Book not found."

def show_books():
    i:int=0
    for i in range(len(library)):
        print(library[i])

# 2. Student Grade Manager
students:list = []
def add_student(name:str="")->dict:
    for student in students:
        if student["name"].lower() == name.lower():
            print("The student was already added.")
            return students
    students.append({"name":name,"grades":[]})
    return students


def add_grade(name:str="",grade:float=0)->None:
    for student in students:
        if student["name"].lower() == name.lower():
            student["grades"].append(grade)
            print(student["grades"])

def get_average(name:str="")->float:
    suma:float = 0
    prom:float = 0
    i:int = 0
    for student in students:
        if student["name"].lower() == name.lower():
            for i in range(len(student["grades"])):
                suma += student["grades"][i]
            break
    prom = suma / len(student["grades"])
    return prom

# 3. Restaurant Menu Editor
menu:list = []
def add_dish(name:str="",price:float=0,quantity:int=0,availability:bool=True)->list:
    if quantity > 0:
        for dish in menu:
            if dish["name"].lower() == name.lower():
                print("The dish was already added.")
                return menu
        menu.append({"name":name,"price":price,"quantity":quantity,"availability":availability})
        return menu
    else:
        print("quantities must be positive.")

def change_availability(name:str="", availability:bool=True)->None:
    for dish in menu:
        if dish["name"].lower() == name.lower():
            dish["availability"] = availability
            break
    else:
        print("The dish couldn't be found.")
    

def total_available_price()->float:
    total:float = 0
    for dish in menu:
        if dish["availability"] == True:
            total += dish["quantity"] * dish["price"]
    return total

# 4. Warehouse Box Counter
warehouse:list = []
def add_box(boxtype:str="",quantity:int=0)->list:
    if quantity > 0:    
        for box in warehouse:
            if box["boxtype"].lower() == boxtype.lower():
                print("The box was already added.")
                return warehouse
        warehouse.append({"boxtype":boxtype,"quantity":quantity})
        return warehouse
    else:
        print("quantities must be positive.")
        return warehouse

    
def update_quantity(boxtype:str="",quantity:int=0)->None:
    if quantity > 0:    
        for box in warehouse:
            if box["boxtype"].lower() == boxtype.lower():
                box["quantity"] = quantity
                break
    else:
        print("Boxes quantity must be positive.")

def has_enough(boxtype:str="",quantity:int=0)->bool:
    enough:bool = True
    for box in warehouse:
        if box["boxtype"].lower() == boxtype.lower():
            enough = quantity == box["quantity"]
            break
    return enough

# 5. Movie Rating System
movies:list=[]
def add_movie(name:str="")->dict:
    for movie in movies:
        if movie["name"] == name:
            print("The movie was already added.")
            return movies
    movies.append({"name":name,"ratings":[]})

def rate_movie(name:str="",rating:float=0)->None:
    if rating >= 0 and rating <= 5:    
        for movie in movies:
            if movie["name"] == name:
                movie["ratings"].append(rating)
    else:
        print("Rating not in range.")


def average_rating(name:str="")->float:
    total:float = 0
    sum:float = 0
    i:int = 0
    for movie in movies:
        if movie["name"] == name:
            for i in range(len(movie["ratings"])):
                total += movie["ratings"][i]
            sum = total / len(movie["ratings"])
        break
    return sum 

# 6. Online Course Tracker
courses:list=[]
def add_course(title:str="",duration:int=0,enrolled:int=0)->list:
    if enrolled > 0 and duration > 19:
        for course in courses:
            if course["title"].lower() == title.lower():
                print("The course was already added.")
                return courses
        courses.append({"title":title,"duration":duration,"enrolled":enrolled})
        return courses
    else:
        print("There has to be atleast 1 member enrolled or The course must last more than 20 hours.")

def update_enrollment(title:str="",enrolled:int=0):
    if enrolled > 0:
        for course in courses:
            if course["title"] == title:
                course["enrolled"] = enrolled
                break
    else:
        print("There has to be atleast 1 member enrolled.")

def filter_by_hours(duration:int=0)->str:
    for course in courses:
        if course["duration"] == duration:
            return course["title"]
    else:
        return f"There's no courses with that duration."


# 7. To-Do List Organizer
todos:list = []
def add_task(name:str="",priority:str="")->dict:
    for task in todos:
        if task["name"].lower() == name.lower():
            print("The task was already added.")
            return todos
    todos.append({"name":name,"priority":priority,"status":False})
    return todos

def complete_task(name:str="")->None:
    for task in todos:
        if task["name"].lower() == name.lower():
            task["status"] = True
            break
    else:
        print("The task couldn't be found.")

def filter_tasks(priority:str="",status:bool=True)->list:
    filter:list = []
    for task in todos:
        if task["priority"] == priority and task["status"] == status:
            filter.append(task["name"])
    return filter

# 8. Digital Wallet
wallet:list = []
def add_expense(expense:str="",price:float=0)->list:
    for details in wallet:
        if details["expense"].lower() == expense.lower():
            details["price"] += price
    else:
        wallet.append({"expense":expense,"price":price})
    return wallet

def total_spent()->float:
    total:float = 0
    for details in wallet:
        total += details["price"]
    return total

def expense_percentages()->float:
    percentages = {}
    total = total_spent()
    if total == 0:
        return {item["expense"]: 0 for item in wallet}
    for details in wallet:
        percent = (details["price"] / total) * 100
        percentages[details["expense"]] = percent
    return percentages

# 9. Pet Adoption Center
pets:list = []
def add_pet(name:str="",species:str="",age:int=0)->list:
    if age > 0:    
        for pet in pets:
            if pet["name"].lower() == name.lower():
                print("The pet was already added.")
                return pets
        pets.append({"name":name,"species":species,"age":age})
        return pets
    else:
        print("Age must be positive.")

def find_by_species(species:str="")->list:
    found:list = []
    for pet in pets:
        if pet["species"].lower() == species.lower():
            found.append(pet)
    return found

def older_than(age:int=0)->list:
    older:list = []
    for pet in pets:
        if pet["age"] > age:
            older.append(pet)
    return older

# 10. Gym Membership System
members:list = []
def register_member(name:str="",plan:str="",status:str="")->list:
    for member in members:
        if member["name"].lower() == name.lower():
            print("The member was already added.")
            return members
    members.append({"name":name,"plan":plan,"status":status})
    return members

def change_plan(member:str="",plan:str="")->None:
    for member in members:
        if member["name"].lower() == member.lower():
            member["plan"] = plan
            break
    else:
        print("The member couldn't be found.")

def unpaid_members()->list:
    unpaid:list = []
    for member in members:
        if member["status"].lower() == "late":
            unpaid.append(member["name"])
    return unpaid
