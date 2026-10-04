performance_rating=int(input(" enter the rating:"))
durations=int(input("enter the time spent in the company: "))
if perfomance_rating>=4 and durations>=2:
    print("bonus valid")
else:
    print("bonus invalid")