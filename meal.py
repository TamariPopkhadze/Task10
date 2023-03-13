def main():
 time = input()
 if time != "11:11":
  time = convert(time)
  if time >= 18:
    print("its dinner time")
  elif time >= 12:
    print("its lunch time")
  elif time >= 7:
    print("its breakfast time")
  else:
    print("its not good time for eating") 



def convert(time):
 hours, minutes = time.split(":")
 hours = float(hours)
 minutes = float(minutes)
 minutes = minutes / 60.0
 time = hours + minutes
 return time  


if __name__ == "__main__":
    main()
