import time
FILENAME = "Data.txt"
SORTED_FILENAME = "Sorted_Data.txt"
class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = [0.0] * 6
        self.grade = ''
def menu():
  print("\n1.Read Data")
  print("2.Write Data")
  print("3.Read & Write Data")
  print("4.Update Data")
  print("5.Delete Data")
  print("6.Delete Records")
  print("7.Sort")
  print("8.Exit")
  return int(input("Enter your choice: "))
def count_existing_records():
    try:
        with open(FILENAME, 'r') as fp:  # Opens file in read mode
            # List comprehension: reads all non-empty lines and removes whitespace
            lines = [line.strip() for line in fp if line.strip()]
            if not lines:  # If no lines exist (empty list)
                return 0
            # Returns the maximum serial number (first number in each line)
            return max(int(line.split()[0]) for line in lines)
    except FileNotFoundError:  # If file doesn't exist
        return 0
def check_duplicate_roll(roll_no):
    try:
        with open(FILENAME, 'r') as fp:
            for line in fp:
                if line.strip():
                    parts = line.strip().split()
                    existing_roll = int(parts[-8])  # Roll number is 8th from end
                    if existing_roll == roll_no:
                        return True
        return False
    except FileNotFoundError:
        return False
def calculate_grade(marks):
    total =sum(marks)
    avg=total/6
    subject_pass=all(mark>33 for mark in marks)
    total_pass=total>240
    if subject_pass and total_pass:
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'E'  # Passing but lower grade
    else:
        return 'F'  # Fail if either condition not met
def sort():
    try:
        # Read all records into a list of dictionaries
        records = []
        with open(FILENAME, 'r') as fp:
            for line in fp:
                if line.strip():
                    parts = line.strip().split()
                    record = {
                        'roll_no': int(parts[-8]),
                        'name': " ".join(parts[1:-8]),
                        'marks': [float(x) for x in parts[-7:-1]],
                        'grade': parts[-1]
                    }
                    records.append(record)
    
        # Sort records by roll number
        sorted_records = sorted(records, key=lambda x: x['roll_no'])
        
        # Write sorted records to new file with new serial numbers
        with open(SORTED_FILENAME, 'w') as fp:
            for i, record in enumerate(sorted_records, 1):  # Start serial number from 1
                fp.write(f"{i} {record['name']} {record['roll_no']}")
                fp.write(" " + " ".join(f"{m:.2f}" for m in record['marks']))
                fp.write(f" {record['grade']}\n")
            print(f"Records sorted by roll number and saved to {SORTED_FILENAME}")
    except FileNotFoundError as e:
        print("Error: Original file not found", e)            
def write():
  last_serial_no = count_existing_records()
  serial_no = last_serial_no + 1
  num_students=int(input("Enter the number of students:"))
  try:
      with open(FILENAME,"a+") as fp:
        for i in range (num_students):
            print(f"\nEnter Details for student {i + 1}:")
            student = Student()
            student.name = input("Enter student name: ")
            while True:
                roll_no = int(input("Enter roll number: "))
                if check_duplicate_roll(roll_no):
                  print(f"Roll number {roll_no} already exists. Please enter a unique roll number.")
                else:
                    student.roll_no = roll_no
                    break
                
            print("Enter Marks: Phy Chem Math IT Eng Odia")
            student.marks = [float(x) for x in input().split()]
            student.grade = calculate_grade(student.marks)
            fp.write(f"{serial_no} {student.name} {student.roll_no}")
            fp.write(" " + " ".join(f"{m:.2f}" for m in student.marks))
            fp.write(f" {student.grade}\n")
            serial_no += 1
        print("Written Successfully..")
  except FileNotFoundError as e:
      print("Error",e)
  
def read():
    try:
        with open(FILENAME, 'r') as fp:
            print("\nStudent Records from File:")
            for line in fp:
                if line.strip():
                    parts = line.strip().split()
                    serial_no = int(parts[0])
                    roll_no = int(parts[-8])
                    marks = [float(x) for x in parts[-7:-1]]
                    grade = parts[-1]
                    name = " ".join(parts[1:-8])
                    
                    print(f"SI:{serial_no:<2} | Name: {name:<30} | RN: {roll_no:<3} | Marks: {' '.join(f'{m:.2f}' for m in marks)} | Grade: {grade}")

    except FileNotFoundError as e:
      print("Error",e)

def control(choice):
    if choice == 1:
        read()
    elif choice == 2:
        write()
    elif choice == 3:
        write()
        read()
    elif choice == 7:
        sort()
    elif choice == 8:
        print("\nExiting..")
        return False
    else:
        print("\nInvalid Choice or Function Not Implemented")
    return True



def main():
    try:
        open(FILENAME, 'a').close()
    except:
        print("Error creating file")
        return
    while True:
        # time.sleep(5)

        if not control(menu()):        
            # time.sleep(5)
            break

if __name__ == "__main__":
    main()
