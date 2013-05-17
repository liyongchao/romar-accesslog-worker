'''
Created on May 15, 2013

@author: outman
'''

#filePath="example/example.log"

fpos = 0

filePath="test.log"

def get_lines_from_file():
    global fpos
#    fpos = 0
    try:
        f = open(filePath, 'r')
        f.seek(fpos)
        lines = f.readlines()
        fpos = f.tell()
        f.close()
        return lines
    except IOError:
            pass
        
def get_minute_from_line(line):
    pos = line.find("/",16,26)
    minute = line[pos+12:pos+14]
    return minute

def get_date_from_line(line):
    pos = line.find("/",16,26)
    date_string = line[pos-2:pos+14]
    return date_string
 
def get_status_from_line(line):
    rpos = line.rfind('"');
    length = len(line)
    end = line[rpos+2:length-1]
    status = end.split(" ")[0]
    return status

def cmp_string(str1, str2):
    return cmp(str1, str2)

def send_data(log_date, count):
    print log_date
    print count

if __name__ == '__main__':
    count = 0
    minuteNow = ""
    minute = ""
    fpos = 0
    log_date = ""
#    f = open(filePath, 'r')

#    while True:
#        line = ""
#        line = f.readline()
#        if line == '':
#            pos=f.tell()
#            f.close()
#            f = open(filePath, 'r')
#  
#            if pos != 0:     
#                f.seek(pos)
#            continue
    while True:
        lines=get_lines_from_file()
        
        while len(lines)==0:
            lines=get_lines_from_file()
            
        for line in lines: 
            if line == '\n':
                continue   
            minute = get_minute_from_line(line)
            status = get_status_from_line(line)
            
            if len(minuteNow) == 0 or cmp("", minuteNow) == 0:
                minuteNow=get_minute_from_line(line)
                log_date=get_date_from_line(line)
                
            if cmp_string(minuteNow, minute) == 0 and cmp_string(status,"200") == 0:
                count = count+1
                
            if cmp(minuteNow,minute) != 0:
                send_data(log_date, count)
                log_date = get_date_from_line(line)
                minuteNow = minute
                count = 1