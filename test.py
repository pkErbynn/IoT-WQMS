data = {
        "temperature": 36,
        "turbidity": 7,
        "ph": 2,
        "water_level": 28
    }

for key, value in data.items():
    if key == "temperature":
        if (value < 23) | (value > 34) :
            check_error = f"Temperature out of range: {value} °C \n"
            print(check_error)
    if key == "turbidity":
        if (value < 0) | (value > 5) :
            check_error = f"Turbidity out of range: {value} °C \n"
            print(check_error)
    if key == "ph":
        if (value < 0) | (value > 4) :
            check_error = f"ph out of range: {value} °C \n"
            print(check_error)
    if key == "water_level":
        if (value < 5) | (value > 27) :
            check_error = f"Water_level out of range: {value} °C \n"
            print(check_error)
        
