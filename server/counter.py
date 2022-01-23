global count
count = int(open("counter.txt").read())

def inc():
    global count
    count += 1
    with open("counter.txt", "w") as file:
        file.write(str(count))
    return ""
