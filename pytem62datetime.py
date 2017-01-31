"""Python2.7.13
Georgia Barnes
Propose: A company has offices open in London, NYC and Portland that are open
    9:00am - 9:00pm. This program determines if the NYC and Lonodon offices are
    open based on PST
Assumes pytz is installed"""

import datetime
import pytz


#get localtime
UTCtime = datetime.datetime.now(tz=pytz.UTC)
PSTime = UTCtime.astimezone(pytz.timezone('US/Pacific'))

#get time difference
NYCdelta = datetime.timedelta(hours=3)
Londelta = datetime.timedelta(hours=8)

#get NYC and London local time
NYCTime = PSTime + NYCdelta
LondonTime =PSTime + Londelta

#NYC office hours
if NYCTime.hour > 9 and NYCTime.hour < 21:
    NYCOffice = 'Open'
else:
    NYCOffice = 'Closed'

#London office hours
if LondonTime.hour > 9 and LondonTime.hour < 21:
    LondonOffice = 'Open'
else:
    LondonOffice = 'Closed'
    
 
print ('The NYC office is: '+ NYCOffice)
print ('The London office is: '+LondonOffice)
