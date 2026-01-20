# BEGIN
# // setup
# variables
# DECLARE
# choice as INTEGER
#
# // Loop
# to
# display
# menu
# until
# correct
# choice
# made
# REPEAT
#
# // display
# menu
# OUTPUT
# "-------------"
# OUTPUT
# "1 - Add item"
# OUTPUT
# "2 - Delete item"
# OUTPUT
# "3 - Exit"
# OUTPUT
# "-------------"
#
# // get
# choice
# OUTPUT
# "Please enter choice"
# INPUT
# choice
#
# // Display
# error if not valid
# option
# IF
# choice < 1
# OR
# choice > 3
# THEN
# OUTPUT
# "Not an option, try again!!"
# ENDIF
#
# UNTIL
# choice >= 1
# AND
# choice <= 3
#
# // make
# decisions
# on
# a
# valid
# choice
# IF
# choice == 1
# THEN
# OUTPUT
# "Add item"
# ELSE
# IF
# choice == 2
# THEN
# OUTPUT
# "Delete item"
# ELSE
# OUTPUT
# "Exit"
# ENDIF
# END
