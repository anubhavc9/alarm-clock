import sys
from time import *

sa = sys.argv

length_sa = len(sys.argv)
if length_sa != 3:
    print("\nInvalid arguments!")
    print("USAGE: python file_name.py mins_value secs_value")
    print("Example: python alarm_clock.py 10 35")
    print("Use a value of 0 minutes 0 seconds for testing the alarm immediately.")
    print("Press Ctrl-C to terminate the alarm clock early.")
    sys.exit(1)

n = int(input("\nEnter the number of times you want to ring the bell: "))

try:
    minutes = int(sa[1])
    seconds = int(sa[2])
except ValueError:
    print("Invalid numeric value (%s) for minutes (%s) seconds", sa[1], sa[2])
    print("Should be an integer >= 0")
    sys.exit(1)

if minutes < 0:
    print("Invalid value for minutes, should be >= 0")
    sys.exit(1)

if seconds < 0:
    print("Invalid value for seconds, should be >= 0")
    sys.exit(1)

time = minutes * 60 + seconds

try:
    if minutes >= 0 and seconds >= 0:
        print("\nAlarm set at: " + ctime() + " - for " + str(minutes) + " minutes & " + str(seconds) + " seconds")
        print("\nSleeping for " + str(minutes) + " minutes " + " & " + str(seconds) + " seconds")
        sleep(seconds)
    print("\nWake up!")
    for i in range(n):
        sleep(2)
        print(chr(7))

except KeyboardInterrupt:
    print("Alarm terminated.")
    sys.exit(1)