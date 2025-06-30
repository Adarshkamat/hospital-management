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
# create_medical_record(554, 101143, "LEG FRACTURE", "Rash Driving", [
#     {"medicine": "Metformin", "dosage": "500mg", "frequency": "Twice a day"},
#     {"medicine": "Glimepiride", "dosage": "2mg", "frequency": "Once a day"},
# ])

# manage_emergency_admission(554,'30-6-2025', "Accident", 8)
# register_patient(554,"John",{"age":21,"gender":"Male","blood_type":"O+"},"Leg Fracture",{"company":"TX HOSPITAL","policy_no":543332})

# manage_discharge_process(554,'30-6-2025', '6-07-2025', "Bed rest for 2 weeks")
# calculate_treatment_cost(554,{
#     "Emergency care and stabilization": 3000,
#     "X-ray and CT Scan": 5000,
#     "Surgery (Femur ORIF)": 45000,
#     "ICU stay (1 day)": 12000,
#     "Medication (Antibiotics + Painkillers)": 2500,
#     "Wound dressing and cleaning": 800,
#     "Physiotherapy sessions (6 weeks)": 6000,
#     "Hospital stay (10 days)": 20000,
#     "Follow-up consultation": 1000,
#     "Discharge summary and documentation": 500
# },{"company":"TX POLICY",
#    "policy":543332,
#    "coverage":70}
# )
# generate_patient_report(554,{
#     "Admission Report": "Details of patient admission, reason, and initial assessment.",
#     "Discharge Summary": "Summary of patient's hospital stay and follow-up instructions.",
#     "Progress Report": "Daily updates on patient condition and treatments.",
#     "Surgical Report": "Detailed record of surgical procedures and outcomes.",
#     "Lab Report": "Results of laboratory tests like blood or urine analysis.",
#     "Radiology Report": "Interpretation of imaging tests such as X-rays or CT scans.",
#     "Treatment Plan Report": "Planned procedures, medications, and therapies for the patient.",
#     "Nursing Report": "Notes by nurses on vitals, care given, and observations.",
#     "ICU Report": "Detailed monitoring and interventions for critical care patients.",
#     "Referral Report": "Information provided when referring the patient to a specialist.",
#     "Billing Report": "Itemized statement of medical charges and services used.",
#     "Insurance Claim Report": "Details needed for filing an insurance reimbursement.",
#     "Inventory Report": "Stock levels of medicines and medical equipment.",
#     "Appointment Report": "List of past and upcoming appointments for a patient.",
#     "Staff Roster Report": "Schedules and shifts of hospital staff members."
# }
# )