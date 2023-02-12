import datetime

time = datetime.datetime.now()
print(f"It's {time.hour}:{time.minute}")
if time.hour == 19:
    print("It's 19 hours, time to leave")
elif time.hour > 19:
    print("Ey bro, It's more than 19 hours, stop with it... go home!")
elif time.hour < 19:
    print(f"It's not time to go yet, there are still {19-time.hour} missing")