# from datetime import datetime

# # Input dates in DD-MM-YYYY format
# admission_date_str = "20-06-2025"
# discharge_date_str = "26-06-2025"

# # Convert string to datetime object using correct format
# admission_date = datetime.strptime(admission_date_str, "%d-%m-%Y")
# discharge_date = datetime.strptime(discharge_date_str, "%d-%m-%Y")

# # Calculate difference
# stay_duration = (discharge_date - admission_date).days

# # Optional: Treat same-day discharge as 1 day
# if stay_duration == 0:
#     stay_duration = 1

# # Output
# print("Days stayed in hospital:", stay_duration)
# di={
#   34:{"name":"Ad"}
#  }

# di[34]={"name":"ADAS"}
# print(di[34])
a=["bhavan","maneesh","adarsh"]
i=0
l=[]
n=len(a)
while i<len(a):
    empty=""
    if i==n-1:
        empty=a[i]+a[((i+1)%n)]
    else:
        empty=a[i]+a[i+1]
    l.append(empty[0:len(a[i])+2])
    i+=1
print(l)
    
dic={"patient_id":11,
                    "appointment_date":23,
                    "appointment_type":2}
            
for j,k in dic.items():
    print(f"{k}:{j}")

# for i in dic:
#     print(i)
#     for j in dic[i]:
#         print(f"{j}:{dic[i][j]}")


rooms={
        "general ward":{"beds":20,
        "price":1500},
        "private room":{"beds":15,
        "price":3000},
        "emergency room":{"beds":10,
        "price":5000}
    } 
Sum=0
for i in rooms:
    for j in rooms[i]:
        if j!="price":
            Sum+=rooms[i][j]
print(Sum)