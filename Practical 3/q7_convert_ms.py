# Converting milliseconds to hours, minutes, and seconds
# by Yiyang 04/02/18

def convert_ms(mSec):
    
    # 1h = 60 mins = 3600 sec = 3600 * 1000 mSec
    secConverted = int(mSec/1000)       # < 1sec not counted
    _time = '{0}:{1}:{2}'.format(int(secConverted/3600), int((secConverted%3600)/60), secConverted%60 )
    
    return _time

mSec = int(input())
print(convert_ms(mSec))
