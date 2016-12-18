#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Three things are missing from the line below - fill them in
my_user=UserAccount("alma18-meet","meetyear18","smile")

#Call the print_secret method (function) - it takes one input - a guess for the password.
my_user.print_secret("meeetyear18")
#Use the wrong password as input here
#my_user.password("meeetyear18")

#Use the right password here
#my_user.password("meetyear18")


my_user.print_secret("meetyear18")
