print("===================================")
print(" Employee Leave Management System")
print("==================================")


employee_name = input("Enter employee name")
leave_available = int(input("Enter leave days available: "))
leave_requested = int(input("Enter leave days requested: "))


print()
print("Leave Summary")
print("================================")
print("Employee:", employee_name)
print("Available:", leave_available)
print("Requested Leave:", leave_requested)



if leave_requested <= 0:
    print("Invalid request.Please enter a valid number of days.")
    

elif leave_requested < leave_available:
    remaining_leave = leave_available - leave_requested
    print("Status: APPROVED")
    print("Remaining Leave:", remaining_leave, "days")


elif leave_requested == leave_available:
    print("Status: APPROVED")
    print("You have used all your leave days.")


else:
    print("Status: DENIED")
    print("Insufficient leave balance.")
    print("You are short by", leave_requested -  leave_available, "days")
        


print("===================================")
print("       Thank you for using ELM")
print("===================================")


          
