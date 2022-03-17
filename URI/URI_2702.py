fd, bd, md = input().split()
fd, bd, md = int(fd), int(bd), int(md)
fr, br, mr = input().split()
fr, br, mr = int(fr), int(br), int(mr)
tf = 0
tb = 0
tm = 0
if fr > fd:
    tf = fr - fd
if br > bd:
    tb = br - bd
if mr > md:
    tm = mr - md

print(tf + tb + tm)