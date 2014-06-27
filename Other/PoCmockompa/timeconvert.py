
import re

timelist = ["1:09.45Y","1:45.54!","2:02.33Y","2:00.00Y","1:58.09!", "59.09", "59", "09Y", "0:9.22!" "22.22Y","59.0!"]

# handles the ":","Y","!" and converts 1:05.00.22Y into 65.22
def getSec(s):
    try: 
        y = s.split('Y')
        l = y[0].split(':')
        r = float(l[0]) * 60 + float(l[1])
    except ValueError:
        try: 
            y = s.split('!')
            l = y[0].split(':')
            r = float(l[0]) * 60 + float(l[1])
        except IndexError:
            y = s.split('!')
            r = float(y[0])
    except IndexError:
        try:
            y = s.split('Y')
            r = float(y[0])
        except ValueError:
            y = s.split('!')
            r = float(y[0])
    return r


for times in timelist:
    timeID = timelist.index(times)
    timelist[timeID]= float(re.match(r'[-+]?\d*\.\d+|\d+', str(getSec(times))).group())

print timelist

