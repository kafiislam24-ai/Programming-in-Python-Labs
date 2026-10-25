students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],     
    [206, "Kamal", [70, 90, 80]],    
    [207, "Jamal", [105, -5, 90]],   
    [208, "Suma", []]                
]

def calculate_average(marks):
    """1. Returns the average of a student's marks."""
    if not marks:
        return None
    
    for mark in marks:
        if mark < 0 or mark > 100:
            return None 
            
    return sum(marks) / len(marks)

def classify_performance(average):
    """2. Returns a performance category based on the average."""
    if average is None:
        return "Invalid/No Data"
        
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def display_report(student_list):
    """3. Displays each student's ID, name, average, and performance category."""
    print(f"{'ID':<5} | {'Name':<10} | {'Average':<8} | {'Performance'}")
    print("-" * 45)
    
    for student in student_list:
        s_id = student[0]
        name = student[1]
        marks = student[2]
        
        avg = calculate_average(marks)
        category = classify_performance(avg)
        
        if avg is None:
             print(f"{s_id:<5} | {name:<10} | {'N/A':<8} | {category}")
        else:
             print(f"{s_id:<5} | {name:<10} | {avg:<8.2f} | {category}")

display_report(students)