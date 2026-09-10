seats = list(range(0, 11))
booked = []

while True:
    print("\n----- BUS TICKET BOOKING SYSTEM -----")
    print("1. Book Ticket")
    print("2. View Seat Availability")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Passenger Name: ")
        age = int(input("Enter Passenger Age: "))

        print("Available Seats:")
        for seat in seats:
            print(seat," ")

        print()
        seat = int(input("Enter Seat Number: "))

        if seat in seats:
            seats.remove(seat)
            booked.append(seat)

            price = 500

            if age > 60:
                price = 350
                print("Senior Citizen Discount Applied")

            print("Ticket Booked Successfully")
            print("Seat Number: ",seat)
            print("Final Ticket Price: ",price)

        else:
            print("Seat not available")

    elif choice == 2:
        print("Available Seats: ")
        for seat in seats:
            print(seat," ")
        print()

    elif choice == 3:
        seat = int(input("Enter Seat Number to Cancel: "))

        if seat in booked:
            booked.remove(seat)
            seats.append(seat)
            seats.sort()
            print("Ticket Cancelled Successfully")
        else:
            print("Seat not found")

    elif choice == 4:
        print("Thank You for Using Bus Ticket Booking System")

    else:
        print("Invalid choice")