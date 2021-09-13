import csv
from typing import Counter
with open("data.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)

data=Counter(new_data)
mode_range={
            "75-85":0,  
            "85-95":0,
            "95-105":0,
            "105-115":0,
            "115-125":0,
            "125-135":0,
            "135-145":0,
            "145-155":0,
            "155-165":0,
            "165-175":0
            }
for weight,occurence in data.items():
    if 75<weight<85:
        mode_range["75-85"] +=occurence

    elif 85<weight<95:
        mode_range["85-95"] +=occurence

    
    elif 95<weight<105:
        mode_range["95-105"] +=occurence

    
    elif 105<weight<115:
        mode_range["105-115"] +=occurence

    elif 115<weight<125:
        mode_range["115-125"] +=occurence

    elif 125<weight<135:
        mode_range["125-135"] +=occurence

    elif 135<weight<145:
        mode_range["135-145"] +=occurence

    elif 145<weight<155:
        mode_range["145-155"] +=occurence

    elif 155<weight<165:
        mode_range["155-165"] +=occurence

    elif 165<weight<175:
        mode_range["165-175"] +=occurence
    
mode_data_range,mode_occurence=0,0
for range,occurence in mode_range.items():
    if occurence > mode_occurence:
        mode_data_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
        mode=float((mode_data_range[0]+mode_data_range[1])/2)
print(f"mode is=>{mode:2f}")

