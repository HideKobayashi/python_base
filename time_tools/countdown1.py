from time import sleep

print("Enter 'q' or type Ctrl-c to terminate.")
while True:
    inp_s = input("Specify a number in seconds >> ")
    if inp_s == "q":
        break
    try:
        when_to_stop = int(inp_s)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break
    except:
        print("Not a number!")
        continue
    
    while when_to_stop > 0:
        try:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left, end="\r")
            sleep(1)
            when_to_stop -= 1
        except KeyboardInterrupt:
            print(f"KeyboardInterrupt at {time_left}")
            break
        except Exception as e:
            print("Exception: ", e)
    print()
