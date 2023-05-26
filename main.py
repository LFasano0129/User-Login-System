# Open the file in read mode
user_database = []
with open("UD.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line[0:4] == 'USER':
            continue
        else:
            user_database.append(line)

logged_in = False
while not logged_in:

    # Ask user to login if an existing user or create a new login if a new user
    log_or_new = input("Login or create a new user?\nSelect L to login, select C to create a new user: ")
    print('\n')

    # If an invalid character is entered, return to step 2
    if log_or_new not in ['L', 'C']:
        print("Invalid, please try again.\n")
        continue

    # Prompt user for username
    elif log_or_new == 'L':
        input_user = input("Please enter your username and hit enter: ")
        print('\n')
        # Search username in database
        user_found = False
        for line in user_database:
            stored_user, stored_pass = line.strip().split(',')
            if stored_user == input_user:
                user_found = True
                # Username found, prompt for password
                input_pass = input("Enter Password: ")
                print('\n')
                # check password
                if stored_pass.strip() == input_pass:
                    print("You are logged in.")
                    logged_in = True
                else:
                    print("Wrong Password.")
        if not user_found:
            print("User not found")
    # if input C, prompt to create new user
    elif log_or_new == 'C':
        input_info = input("Please enter your first name, last name, and student ID, separated by a space: ")
        print('\n')
        first_name, last_name, student_id = input_info.split()
        new_user = first_name[0].lower() + last_name[:2].lower() + student_id[:3]
        print("Your new username is: {}".format(new_user))

        # prompt user for new password
        pass_verif = False
        while not pass_verif:
            new_pass = input("Please enter password: ")
            print('\n')
            # prompt user to reenter password to verify
            verify_pass = input("Please reenter password: ")
            print('\n')
            # Verify new password
            if new_pass == verify_pass:
                # save new user
                new_user_info = new_user + "," + new_pass
                user_database.append(new_user_info)
                with open("UD.txt", "w") as file:
                    file.write("\n".join(user_database))
                print("User created")
                pass_verif = True
            else:
                print("Passwords did not match")
