student_id = input("Student ID: ").strip().upper()
school_code = student_id[:2]
student_number = student_id[-6:]

is_valid = (
    len(student_id) == 8
    and school_code.isalpha()
    and student_number.isdigit()
)

if is_valid:
    masked_id = f"{school_code}****{student_number[-2:]}"
    print(f"Valid ID   School code: {school_code}   Student number: {student_number}   Masked ID: {masked_id}")
elif len(student_id) != 8:
    print("Invalid ID - ID must be exactly 8 characters bro.")
elif not school_code.isalpha():
    print("Invalid ID - First 2 characters MUST be letters bro.")
else:
    print("Invalid ID - Last 6 characters MUST be numbers bro.")