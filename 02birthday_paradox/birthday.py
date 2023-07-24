"""
Birthday Paradox, by Al Sweigart al@inventwithpython.com
--snip--
How many birthdays shall I generate? (Max 100)
> 23
Here are 23 birthdays:
Oct 9, Sep 1, May 28, Jul 29, Feb 17, Jan 8, Aug 18, Feb 19, Dec 1, Jan 22,
May 16, Sep 25, Oct 6, May 6, May 26, Oct 11, Dec 19, Jun 28, Jul 29, Dec 6,
Nov 26, Aug 18, Mar 18
In this simulation, multiple people have a birthday on Jul 29
Generating 23 random birthdays 100,000 times...
Press Enter to begin...
Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
--snip--
90000 simulations run...
100000 simulations run.
Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95 % chance of
having a matching birthday in their group.
That's probably more than you would think!
"""
def generateBirthdays(num_days):
    start_date = datetime.date(2010, 1, 1)
    birthdays = []
    for day in range(num_days):
        rand_days = datetime.timedelta(random.randint(0, 364))
        birthdays.append(start_date + rand_days)
    return birthdays

def findMatch(birthdays):
    for i, birthdayI in enumerate(birthdays):
        for j, birthdayJ in enumerate(birthdays[i + 1 :]):
            if birthdayI == birthdayJ:
                return True
    return False

import datetime
import random
random.seed

date_print = []
num_days = 20
num_cycles = 100000
matches_found = 0

print("The Birthday Paradox: \nIn a relatively small set of birthdays it is common to find two that are the same.  \nThis program allows you to set how many days and how many tests you'd like to run to see just how likely it is")
num_days = int(input("How many days tested per set?"))
num_cycles = int(input("How many cycles should be run?"))

birthdays = generateBirthdays(num_days)
MONTHES = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

print("Displaying a sample list of {} birthdays".format(num_days))
for day in birthdays:
    temp_date = '{} {}'.format(MONTHES[day.month - 1], day.day)
    date_print.append(temp_date)
print(date_print)

print("Generating and comparing {} sets of {} birthdays".format(num_cycles, num_days))
for i in range(num_cycles):
    if i % 10000 == 0 and i != 0 :
        print("Starting cycle {}".format(i))
    birthdays = generateBirthdays(num_days)
    found = findMatch(birthdays)
    if(found): matches_found += 1

odds_of_match = matches_found / num_cycles * 100
print("Out of {} cycles, {} sets had at least one pair of matching birthdays. \nThe odds of finding a pair in a set of {} birthdays is {}%".format(num_cycles, matches_found, num_days, odds_of_match))
