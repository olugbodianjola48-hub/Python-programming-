import sqlite3

# Main function to manage database operations
def main():
    connection = None  # so we can access it in finally block

    try:
        # connect to MSQLite database (creates schools.db if it doesn't exist)
        connection = sqlite3.connect('schools.db')
        print("Database connected successfully!")

        # create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # create the students table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        ''')
        print("Table 'students' created successfully!")

        # DELETE previous data to avoid duplicate entries during testing
        cursor.execute("DELETE FROM students")
        print("Old data cleared")

        # Insert student records
        cursor.execute('''
            INSERT INTO students (name, age, grade)
            VALUES (?, ?, ?)
        ''', ("jane smith", 17, "11th"))
        print("Student data inserted successfully!")

        # commit the changes to save to the database
        connection.commit()

        # Retrieve and display all student records
        cursor.execute('SELECT * FROM students')
        all_students = cursor.fetchall()
        print("\n--- ALL Students ---")
        for student in all_students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            connection.close()
            print("\nDatabase connection closed.")

# Run the program
main()
