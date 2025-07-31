
# Employee feed back application by github copilot.py

def add_feedback():
    name = input("Enter employee name: ")
    feedback = input("Enter feedback: ")
    with open('feedback.txt', 'a') as f:
        f.write(f"{name}: {feedback}\n")
    print("Feedback added successfully.\n")

def view_feedback():
    print("\n--- All Feedback ---")
    try:
        with open('feedback.txt', 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No feedback found.\n")

def main():
    while True:
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_feedback()
        elif choice == '2':
            view_feedback()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()