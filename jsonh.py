import json

# Define global variables
x = 0
y = 0
tlat = 0
tlon = 0
confidence = 0

def process_message(json_str):
    global x, y, tlat, tlon, confidence

    try:
        data = json.loads(json_str)
        if "x" in data and "y" in data:
            x = data["x"]
            y = data["y"]
        elif "tlat" in data and "tlon" in data:
            tlat = data["tlat"]
            tlon = data["tlon"]
        elif "confidence" in data:
            confidence = data["confidence"]
        else:
            print("Unknown format")

        # Print all global variables in a single line
        print(f"x: {x}, y: {y}, tlat: {tlat}, tlon: {tlon}, confidence: {confidence}")

    except json.JSONDecodeError:
        print("Invalid JSON format")

# Your code continues here...

