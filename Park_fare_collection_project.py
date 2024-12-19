import webbrowser


def welcome_message():
    print("$#$#$#$# Welcome to Indira Park $#$#$#$#$#$#$#$")
    print("$#$#$#$# Enter your details to book tickets $#$#$#$#$#@\n")


def display_menu():
    print("Choose an Option:")
    print("1. Book Ticket")
    print("2. Check Price")
    print("3. Check Visitors")
    print("4. About Us")
    print("5. Exit")


def calculate_price(age):
    if age < 18:
        return 45  
    elif age > 60:
        return 47  
    else:
        return 50

def book_ticket(visitor_log):
    print("Enter your details as follows:")
    name = input("Enter your name: ")
    gender = input("Enter your gender: M?F")
    age = int(input("Enter your age: "))
    if age > 0:
        print("")
    else:
        print("Enter a positive integer")

    ticket_price = calculate_price(age)
    print("Ticket Price: {} Rs".format(ticket_price))  


    visitor_log.append({"name": name, "gender": gender, "age": age, "ticket_price": ticket_price})
    print("Ticket booked successfully!")

def check_prices():
    print("The prices and discounts are listed below:")
    print("- Children (under 18): 10% discount, Ticket Price = 45 Rs")
    print("- Senior Citizens (above 60): 5% discount, Ticket Price = 47 Rs")
    print("- Regular Ticket Price: 50 Rs")

def check_visitors(visitor_log):
    total_visitors = len(visitor_log)  
    total_revenue = sum(visitor["ticket_price"] for visitor in visitor_log) 

    print("Total Visitors: " + str(total_visitors)) 
    print("Total Revenue: " + str(total_revenue) + " Rs")  

def about_us():
    print("Opening the About Us page...")
    webbrowser.open("/home/prem-rupyz/pythoncode/aboutus.html")

def main():
    visitor_log = []
    welcome_message()

    while True:
        display_menu()
        user_choice = input("Select your choice: ")

        if user_choice == "1":
            book_ticket(visitor_log)
        elif user_choice == "2":
            check_prices()
        elif user_choice == "3":
            check_visitors(visitor_log)
        elif user_choice == "4":
            about_us()
        elif user_choice == "5":
            print("Thank you for visiting Indira Park! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

main()