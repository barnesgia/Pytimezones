"""Python2.7.13
Georgia Barnes
Propose: A company has offices open in London, NYC and Portland that are open
    9:00am - 9:00pm. This program determines if the NYC and Lonodon offices are
    open based on PST
Assumes pytz is installed"""

import datetime
import pytz

def checkOpenClose(location,zone):
    UTCtime = datetime.datetime.now(tz=pytz.UTC)
    localtime = UTCtime.astimezone(pytz.timezone(zone)).hour
    if localtime >= 9 and localtime <=9:
        print location + " : Open"
    else:
        print location+ " : Closed"
    
checkOpenClose('NYC','US/Eastern')
checkOpenClose('London','Europe/London')
               

