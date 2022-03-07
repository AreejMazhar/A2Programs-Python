RaceHours = int
RaceMins = int
RaceSecs = int
RaceTime = int

RaceTime = 0

RaceHours = int(input("Enter race hours: "))
RaceMins = int(input("Enter race minutes: "))
RaceSecs = int(input("Enter race seconds: "))

RaceTime = (RaceHours*3600) + (RaceMins*60) + RaceSecs
print ("The race time is " , RaceTime, "seconds.")
