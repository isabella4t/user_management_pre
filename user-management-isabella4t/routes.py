import sys
import os
import sendgrid
import time
import secrets
from sendgrid.helpers.mail import *
##secrets.token_hex(16)
"""
moving clearscreen to routes
"""

def clear_screen():
    """
    Detect operating system and clear terminal
    """
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear') #Mac or Linux

def makedatabase():
    """
    Function to test whether database exists on the computer
    """
    try:
        database = open('database.txt','r')
    except FileNotFoundError:
        database = open('database.txt','w')
        database.close()

def makeuserinfo(username):
    """
    make Funct to test if user info database exists
    """
    try:
        profile = open(username + '.txt','r')
    except FileNotFoundError:
        profile = open(username + '.txt','w')
        profile.close()


def register(username,password,email):
    """
    Make function to store password and username in text file
    """
    makedatabase()
    database = open('database.txt','r')
    other_users = database.readlines()
    database.close()

    database = open('database.txt','w')
    for record in other_users:
        database.write(record)
    database.write('%s,%s,%s\n' % (username,password,email))
    database.close()
    makeuserinfo(username)
    profile = open(username + '.txt','w')
    profile.write("Nickname: %s" % (username))
    profile.close()


def login(username,password):
    """
    Make function to test username and Password
    """
    makedatabase()
    lobg = False
    database = open('database.txt','r')
    for line in database:
        astr = line.strip('\n')
        asplt = astr.split(',')
        if username == asplt[0] and password == asplt[1]: ##idk why its not logging in ## fixed
            lobg = True
    if lobg == False: ## at the very end
        clear_screen()
        print("Sorry, incorrect username or password")
        time.sleep(0.5)
    else:
        loggedin(lobg,username)
    database.close()

def loggedin(truer,usernamer):
    """
    Make interface for when logged in
    """
    clear_screen()
    print("Successfully logged in")
    time.sleep(0.5)
    clear_screen()
    while truer:
        print("1.Edit nickname")
        print("2.Edit bio")
        print("3.Reset password")
        print("4.Delete account")
        print('5.Log out')
        choice = input("Make selection: ")
        if choice == '1':
            clear_screen()
            nickname(usernamer)
        elif choice == '2':
            clear_screen()
            biog(usernamer)
        elif choice == '3':
            clear_screen()
            uss = input("Enter your username: ")
            addre = input("Enter your email: ")
            print("Check your email for reset token")
            changerequest(uss,addre)
            truer = False
        elif choice == '4':
            password = input("Please enter your password: ")
            clear_screen()
            deleteaccount(usernamer,password)
            truer = False
        elif choice == '5':
            truer = False ## confused by time

def nickname(oldname):
    """
    Writing nickname changer
    """
    makeuserinfo(oldname)
    profile = open(oldname +'.txt','r')
    oldinfo = profile.readline()
    otherinfo = profile.readlines()
    profile.close()
    profile = open(oldname +'.txt','w')
    print(oldinfo)
    newname = input("Write new nickname: ")
    profile.write("Nickname: %s" % (newname))
    profile.write("\n")
    for i in otherinfo:
        profile.write(i)
    profile.close()
    clear_screen()

def biog(usname):
    """
    Writing bio
    """
    makeuserinfo(usname)
    profile = open(usname +'.txt','r')
    nickname = profile.readline()
    bide = profile.readline()
    bio = profile.readlines()
    profile.close()
    profile = open(usname +'.txt','w')
    profile.write("%s" % (nickname))
    profile.write("Biography:")
    print("Current bio: ")
    for i in bio:
        print(i)
    print("1.Edit bio")
    print("2.Back")
    choice = input()
    if choice == '1':
        edit = input("Write your bio: ")
        profile.write("\n%s" % (edit))
        profile.close()
    elif choice == '2':
        for i in bio:
            profile.write(i)
    clear_screen()

def deleteaccount(username,password):
    """
    funct to delete account
    """
    makedatabase() ##opens database
    log = True
    print("Are you sure you want to delete your account?")
    print("1.Yes")
    print("2.Cancel")
    choice = input()
    if choice == '1':
        counter = -1
        datao = open('database.txt','r')
        for line in datao:
            counter += 1
            astr = line.strip('\n')
            asplt = astr.split(',')
            print(asplt)
            if username == asplt[0] and password == asplt[1]:
                theline = counter
        datao = open("database.txt", "r")
        lines = datao.readlines()
        datao.close()
        del lines[theline]
        revise = open("database.txt", "w")
        for line in lines:
            revise.write(line)
        revise.close()
        log = False
    elif choice == '2':
        log = True
    return log
    time.sleep(3)
    clear_screen()
    datao.close()

def changerequest(username,email):
    """
    sends the email with the token
    """
    key = (secrets.tokenhex(16))
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("itusermanager@gmail.com")
    to_email = To("%s" % (email))
    subject = "Password Reset"
    content = Content("text/plain", "Welcome to password reset. \nTo reset your password, enter the following token into the terminal" + str(key))
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    moo = input("Please enter the token: ")
    if key = moo:
        choice = input("Enter new password: ")
        changepass(username,choice,email)
    else:
        print('An error has occurred')
def changepass(username,newpass,email):
    """
    changes the Password
    """
    looker = open('database.txt','r')
    counter = -1
    for line in datao:
        counter += 1
        astr = line.strip('\n')
        asplt = astr.split(',')
        print(asplt)
        if username == asplt[0]:
            theline = counter
    datao = open("database.txt", "r")
    lines = datao.readlines()
    datao.close()
    revise = open("database.txt", "w")
    counting = -1
    for line in lines:
        counting += 1
        if counting == theline:
            revise = write("%s,%s,%s" % (username,newpass,email))
            revise.close()
        else:
            revise.write(line)
            revise.close()
