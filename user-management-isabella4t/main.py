import routes
"""
Make interface with option to login, register, or exit
"""
exit = False
while not exit:
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Make selection: ")
    if choice == '2':##register
        routes.clear_screen()
        uname = input("Create Username: ")
        passwo = input("Create Password: ")
        mel = input("Email: ")
        routes.register(uname,passwo,mel)
        routes.clear_screen()
    elif choice == '3': ##exit
        routes.clear_screen()
        exit = True
    elif choice == '1': ##login
        loguser = input("Username: ")
        logpass = input("Password: ")
        routes.login(loguser,logpass)
        routes.clear_screen()
