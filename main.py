from utils.tracker import add_session, show_sessions, show_stats

def main():
    while True:
        print("\n===== STUDY TRACKER =====")
        print("1. Add study session")
        print("2. View study sessions")
        print("3. View statistics")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            subject = input("Subject: ")

            try:
                minutes = int(input("Study duration (minutes): "))
                if minutes <= 0:
                    print("Duration must be positive.")
                    continue

                add_session(subject, minutes)
                print("Session saved!")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            show_sessions()

        elif choice == "3":
            show_stats()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()