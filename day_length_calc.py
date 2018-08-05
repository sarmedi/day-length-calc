print("A day in 2017 is 23 hours 56 minutes and 4 seconds long.")
def time_to_seconds(h,m,s):
    seconds=((h*60)*60)+(m*60)+s
    return seconds
print("Which is equivalent to", time_to_seconds(23, 56, 4), "seconds.")
futureyear=int(input("Enter a future year => ", ))
print(futureyear)
futureyearconversion=(6)/(900000000)
yeardiff=futureyear-2017
def seconds_to_str(timeinseconds):
    h=int(timeinseconds//(60*60))
    m=int((timeinseconds%(60*60))//60)
    s=int((timeinseconds%(60*60))%60)
    string1=(str(h), "hours "+ str(m) +" mins "+ str(s)+" secs")
    string1=str(string1)
    string1=string1.replace("(", "")
    string1=string1.replace(")", "") 
    string1=string1.replace("'", "")
    string1=string1.replace(",", "")    
    return string1

newyearseconds=int((yeardiff*futureyearconversion*60*60+time_to_seconds(23, 56, 4)))
print("A day in year", futureyear, "will be", newyearseconds, "seconds long",)
print("which is equivalent to", seconds_to_str(newyearseconds))