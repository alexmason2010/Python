"""
DateTime Exercise 1:

You want to display a message letting customers know what day their purchase will be shipped.
Assume, if your store promises "5 day shipping on all items!".
Finally, print out Items purchased today will be shipped on YYYY-MM-DD 
(where the date is 5 days from the current date).
"""

"""
Desired Output: Items purchased today will be shipped on YYYY-MM-DD
"""

import datetime

# Create a variable today that holds the current date (no time)
today = datetime.date.today()
                            
# Create a variable ships that holds the date five days from today
ships = today + datetime.timedelta(days=5)
                            
# Write the message shown in "Desired Output" to the screen 
print('Items purchased today will be shipped on', ships.strftime("%Y-%m-%d"))
     
