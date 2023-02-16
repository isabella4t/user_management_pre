## Intro to CS 2021-2022
# User Management

## Acknowledgements
This was made possible by the guidance of Daniel Kelley, my instructor at the time.
The project was assigned by him and the assignment is as follows:

## Challenge
For this project, you need to create a user management system.
That is, a program that allows users to register an account,
login with a username and password, and logout. The program should
also allow a user to edit their profile data and delete their
account. Your application needs to be able to register multiple users.

### Functions
To meet the goals of the challenge you will need to create at least
the following functions:

#### `register()`
This function needs to take all the profile data (minimum username
and password) and save it in a file. It should return an error if there
already exists a user with that username. Use `.gitignore` to avoid
committing sensitive user data to your repository!

#### `login()`
This function needs to take a username and password and check against
the data file containing users' info. It should return an error for
a non-existent username or incorrect password, it should return all the
user data on success. Save the user data in a variable in the main loop of
the program.

#### `logout()`
This function does not take any parameters. It clears the data containing
the logged in user from the main loop.

#### `edit()`
Only for a logged in user, this function should allow them to change their
username or password by editing the file containing all user data.

#### `delete()`
Only for a logged in user, this function should prompt the user with a
warning and then delete their data from the file containing all user data.
