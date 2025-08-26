# ========triathlon event=======

print("===========Welcome to a triathlon event===========")

# Prompt user for details 

swim = int(input("Please enter your swimming time in minutes: "))
cycle = int(input("Please eneter the total time for cycling: "))
run = int(input("Please enter the total time you tok to run: "))

def triathlon(swim, cycle, run):

    total_time = swim + cycle + run
    return total_time

def triat_logic(total_time):

    if total_time <=100:
        return "Award: Provincial colours"
    elif total_time <= 105:
        return "Award: Provincial half colours"
    elif total_time <= 110:
        return "Award: Provincial scroll"
    else:
        return "No Award"

total_time = triathlon(swim, cycle, run)

print(f"Total time taken for the triathlon: {total_time} minutes")
print(triat_logic(total_time))   

