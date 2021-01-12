count = 0

for tp in range(2):
    for p in range(3):
        if 100*p + 200*tp > 200:
            continue
        for ft in range(5):
            if 50*ft + 100*p + 200*tp > 200:
                continue
            for tt in range(11):
                if 20*tt + 50*ft + 100*p + 200*tp > 200:
                    continue
                for tn in range(21):
                    if 10*tn + 20*tt + 50*ft + 100*p + 200*tp > 200:
                        continue
                    for f in range(41):
                        if 5*f + 10*tn + 20*tt + 50*ft + 100*p + 200*tp > 200:
                            continue
                        for t in range(101):
                            if 2*t + 5*f + 10*tn + 20*tt + 50*ft + 100*p + 200*tp > 200:
                                continue
                            for o in range(201):
                                if o + 2*t + 5*f + 10*tn + 20*tt + 50*ft + 100*p + 200*tp == 200:
                                    count += 1

print(count)
