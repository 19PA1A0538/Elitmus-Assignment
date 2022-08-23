def numLeapYear(m,y):
    if(m <= 2):
        y = y-1
    res = int(y/4) - int(y/400)
    return res

def days_diff(d,m,y):
    res = 0
    mDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(0,m):
        res += mDays[i]
    res += (y*365)
    res += d
    res += numLeapYear(m,y)
    return res

def date_diff(strt_date,ed_date):
    diff = strt_date-ed_date
    return abs(diff)


print("Enter valid start_date in dd/mm/yyyy format:")
start_date = input()
print("Enter valid end_date in dd/mm/yyyy format:")
end_date = input()

d1 = list(map(int,start_date.split('/')))
d2 = list(map(int,end_date.split('/')))
m=[1,2,3,4,5,6,7,8,9,10,11,12]
if ((d1[0]>=31 and (d1[1]==m[0] or m[2] or m[4] or m[6] or m[7] or m[9] or m[10])) or (d2[0]>=31 and (d2[1]==m[0] or m[2] or m[4] or m[6] or m[7] or m[9] or m[10])) or (d1[1]>12) or (d2[1]>12)):
    print("You have given Invalid date")
else:
    numofdays1 = days_diff(d1[0],d1[1],d1[2])
    numofdays2 = days_diff(d2[0],d2[1],d2[2])
    print(date_diff(numofdays1,numofdays2))