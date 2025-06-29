from datetime import datetime
print("--23--6--25--")

medical_staffs={}
patient= {}


appointment={}
medical_record={}
billing={}

emergency={}

medicine={}
assigned_rooms={}
patient_report={}
discharged_patients={}

hopspital_efficiency=[]
records={}

def register_patient(patient_id,name,personal_info, medical_history, insurance_info):
    if patient_id in emergency:
        patient[patient_id]={"name":name,"personal_info":personal_info,"medical_history":medical_history,"insurance_info":insurance_info}
    if patient_id  not in patient:
        patient.update({ patient_id:{"name":name,
                "personal_info":personal_info,
                "medical_history":medical_history,
                "insurance_info":insurance_info}
    })
        print(f"Registration of {patient_id} ID successfull")

    else:
        print("Already Registered")
register_patient(123,"Romi",{"age":21,"gender":"Male","blood_type":"O+"},"Diabetes",{"company":"Star Health","policy_no":92394412})

# shift_schedule = [
#     {"day": "Monday", "start_time": "08:00", "end_time": "16:00", "location": "ICU"},
# ]

def add_medical_staff(staff_id, name, specialization, shift_schedule, contact_info):
   medical_staffs.update({
       staff_id:{"name":name,
            "specialization":specialization,
            "shift_schedule":shift_schedule,
            "contact_info":contact_info}   
   })
   print(f"Medical Staff ('ID'{staff_id}) is added ")
add_medical_staff(101123,"Dr.Subhash Rao","General Doctor",[
    {"day": "Monday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "OPD"},
    {"day": "Tuesday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "OPD"},
    {"day": "Wednesday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Wards"},
    {"day": "Thursday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "Emergency"},
    {"day": "Friday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "OPD"},
    {"day": "Saturday", "shift": "Full Day", "start": "08:00", "end": "20:00", "location": "OPD/Wards"},
    {"day": "Sunday", "shift": "Off", "start": "-", "end": "-", "location": "-"}] , 9929929292)
add_medical_staff(101243,"Dr.Jay Kumar","Cardiologist",[
    {"day": "Monday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Cardiology OPD"},
    {"day": "Tuesday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Cardiology Ward"},
    {"day": "Wednesday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "ICU"},
    {"day": "Thursday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Cath Lab"},
    {"day": "Friday", "shift": "Full Day", "start": "08:00", "end": "20:00", "location": "OPD & Ward"},
    {"day": "Saturday", "shift": "On Call", "start": "-", "end": "-", "location": "-"},
    {"day": "Sunday", "shift": "Off", "start": "-", "end": "-", "location": "-"}
], 8800978213)
add_medical_staff(101143,"Dr.Santosh","Neurologist",[
    {"day": "Monday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "Neuro OPD"},
    {"day": "Tuesday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Neuro Ward"},
    {"day": "Wednesday", "shift": "Full Day", "start": "08:00", "end": "20:00", "location": "Neurology & ICU"},
    {"day": "Thursday", "shift": "Off", "start": "-", "end": "-", "location": "-"},
    {"day": "Friday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "Neuro OPD"},
    {"day": "Saturday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Neuro Ward"},
    {"day": "Sunday", "shift": "Off", "start": "-", "end": "-", "location": "-"}
], 7800978543)


def schedule_appointment(patient_id, doctor_id, appointment_date, appointment_type,charges):
    if patient_id in patient and doctor_id in medical_staffs:
        appointment.update({
        doctor_id:{"patient_id":patient_id ,
                    "appointment_date":appointment_date,
                    "appointment_type":appointment_type,
                    "charges":charges}
    })
        print(f"""The appointment has been scheduled at {appointment_date}
with {medical_staffs[doctor_id]["name"]}""")
    else:
        print("Register the patient ")

schedule_appointment(123, 101123, '21-7-2025', "Consultation",1500)
def doctors_schedule(doctor_id):
    print(f"{medical_staffs[doctor_id]["name"]} - ({medical_staffs[doctor_id]["specialization"]})")
    today=datetime.today()
    print(datetime.strftime(today,"%B %d, %Y"))

    for i in appointment[doctor_id]:
        if i=="charges":
            break
        print(f"{i}:{appointment[doctor_id][i]}")
doctors_schedule(101123)
        


def create_medical_record(patient_id, doctor_id, diagnosis, treatment, prescription):
 
    if patient_id in appointment[doctor_id]:
        medical_record.update({
            patient_id:{"doctor_id":doctor_id, "diagnosis":diagnosis, "treatment":treatment, "prescription":prescription}
        })
    else:
        print("Register the patient ")


def process_billing(patient_id, services_list, insurance_coverage):
    billing.update({
        patient_id:{
        "service_list":services_list,
        "insurance_coverage":insurance_coverage}
    })
    
    
    if patient_id in assigned_rooms :
        global admi_date
        admi_date=datetime.strptime(assigned_rooms[patient_id]["admission_date"], "%d-%m-%Y")
    if patient_id in discharged_patients:
        disc_date=datetime.strptime(discharged_patients[patient_id]["discharge_date"],"%d-%m-%Y")
    doctor=create_medical_record[patient_id]["doctor_id"]
    print(f"""=== BILLING SUMMARY ===
Patient: {patient[patient_id]["name"]}
Admission Date: {datetime.strftime(admi_date, "%B %d, %Y")}
Discharge Date: {datetime.strftime(disc_date, "%B %d, %Y")}
Service Charges:
Room Charges ({(disc_date-admi_date).days}days): {((disc_date-admi_date).days)*assigned_rooms[patient_id]["room_type"]["price"]}
Doctor Consultation : {appointment[doctor]["charges"]}""")
    for key,value in services_list:
        print(f"{key}:{value}")
    sum_of_services=sum(cost for services,cost in services_list) 
    Sum_fo_Serices=sum_of_services+{appointment[doctor]["charges"]}+{((disc_date-admi_date).days)*assigned_rooms[patient_id]["room_type"]["price"]}
    print(f"Total bill : {Sum_fo_Serices})
    if billing[patient_id]["insurance_coverage"] :
        after_insurance=(billing[patient_id]["insurance_coverage"])/100*Sum_fo_Serices+Sum_fo_Serices
        print(f"Insurance ({billing[patient_id]["insurance_coverage"]}) : {after_insurance}")
        print(f"patient responsibility : {Sum_fo_Serices-after_insurance}")
    else:
        print("You have no insurance coverage")
        print(f"Patient Responsibility : {Sum_fo_Serices}")
    


def manage_emergency_admission(patient_id, emergency_type, severity_level):
    emergency.update({
        patient_id:{"emergency_type":emergency_type,"severity_level":severity_level}
    })
    patient.update({ patient_id:{"name":None,
                "personal_info":None,
                "medical_history":"Emergency",
                "insurance_info":None}
    })
   

def track_medication_inventory(medication_id, quantity, expiry_date, supplier):
    expiry_date=datetime.strptime(expiry_date,"%d-%m-%Y")
    today=datetime.today()
    if expiry_date>=today:
        print("THE MEDICINE HAS EXPIRED")
    else:
        medicine.update({
            medication_id:{"quantity":quantity,"expiry_date":expiry_date,"supplier":supplier}
        })
        print("The Medicine has been added to the inventory!")
rooms={
        "general ward":{"beds":20,
        "price":1500},
        "private room":{"beds":15,
        "price":3000},
        "emergency room":{"beds":10,
        "price":5000}
    }    
def assign_room(patient_id, room_type, admission_date, expected_duration):
   
    room_type=room_type.lower()
    if rooms[room_type]["beds"]>0:
        assigned_rooms.update({patient_id:{"room_type":room_type,"admission_date":admission_date,"exp_duaration":expected_duration}})
        rooms[room_type]["beds"]-=1
        patient[patient_id]["room_type"]=room_type
    else:
        print(f"Currently the {room_type} is unavailable Opt for other rooms")

def calculate_treatment_cost(patient_id, treatment_plan, insurance_details):
    ins=insurance_details
    cost=0
    for plan,price in treatment_plan.items():
        cost=sum(price)
    if patient_id in assigned_rooms :
        
        admi_date=datetime.strptime(assigned_rooms[patient_id]["admission_date"], "%d-%m-%Y")
    if patient_id in discharged_patients:
        disc_date=datetime.strptime(discharged_patients[patient_id]["discharge_date"],"%d-%m-%Y")
    doctor=create_medical_record[patient_id]["doctor_id"]
    print(f"""=== BILLING SUMMARY ===
Patient: {patient[patient_id]["name"]}
Admission Date: {datetime.strftime(admi_date, "%B %d, %Y")}
Discharge Date: {datetime.strftime(disc_date, "%B %d, %Y")}""")
    print(f"The cost of the Treatment : {cost}")
    if ins["coverage"]:
        ins_cost=cost+cost*ins["coverage"]*100
        print(f"The insurance coverage {ins["coverage"]} % : {ins_cost}")
        print(f"Patients responsibility :{cost-ins_cost}")
    else:
        print("You have no insurance coverage")
        print(f"Patients Responsibility : {cost}")
    

def generate_patient_report(patient_id, report_type):
 if patient_id in medical_record:
    patient_report.update({patient_id:report_type})
    print(f"""Patient Name : {patient[patient_id]["name"]} ('ID'{patient_id})
          Age : {patient[patient_id]["personal_info"]["age"]}| Gender :{patient[patient_id]["personal_info"]["gender"]}| Blood Type : {patient[patient_id]["personal_info"]["blood_type"]}
Insurance : {patient[patient_id]["insurance_info"]["company"]} ('ID'{patient[patient_id]["insurance_info"]["policy_no"]})""")
    if patient_id in discharged_patients:
        status = "Discharged"
    elif patient_id in assigned_rooms:
        status = "Inpatient"
    else :
        status = "Outpatient"
    print(f"Current Status : {status}")
    print(f"Room : {[patient[patient_id]["room_type"]}")
    print(f"Admiited : {datetime.strftime(admi_date, "%B %d, %Y")}")
    print(f"Attending Doctor : ------------ ")
    today=datetime.today()
    print(f"Recent Vitals ({datetime.strftime(today,"%B %d, %Y - %H:%M %p")}:)")
    for key,value in report_type:
        print(f"{key}:{value}")
    print("Active Medications : ")
    for key,value in medical_record[patient_id]["prescription"]:
        print(f"-{key}:{value}")
 else:
     print("Create the Medical Record of the pateint")
def analyze_hospital_efficiency(metrics_type, time_period):
    Sum=0
    for i in rooms:
        for j in rooms[i]:
            if j!="price":
                Sum+=rooms[i][j]
    TOTAL_BEDS=Sum
    start_date, end_date = time_period
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    total_stay_days = 0
    total_patients = 0
    occupied_bed_days = 0

    for record in hopspital_efficiency:
        admission = datetime.strptime(record["admission_date"], "%Y-%m-%d")
        discharge = datetime.strptime(record["discharge_date"], "%Y-%m-%d")

        if discharge < start_date or admission > end_date:
            continue
        actual_admission = max(admission, start_date)
        actual_discharge = min(discharge, end_date)
        stay_duration = (actual_discharge - actual_admission).days + 1

        total_stay_days += stay_duration
        total_patients += 1
        occupied_bed_days += stay_duration

    if total_patients == 0:
        print("No patient data available for the selected period.")
        return

    if metrics_type == "average_length_of_stay":
        avg_stay = total_stay_days / total_patients
        print(f"Average Length of Stay: {avg_stay:.2f} days")
    elif metrics_type == "bed_occupancy_rate":
        analysis_days = (end_date - start_date).days + 1
        bed_occupancy_rate = (occupied_bed_days / (TOTAL_BEDS * analysis_days)) * 100
        print(f"Bed Occupancy Rate: {bed_occupancy_rate:.2f}%")
    elif metrics_type == "patient_throughput":
        print(f"Patient Throughput: {total_patients} patients")
    else:
        print("Invalid metrics type. Please choose from: 'average_length_of_stay', 'bed_occupancy_rate', or 'patient_throughput'.")

def manage_discharge_process(patient_id,admission_date, discharge_date, follow_up_instructions):
    if patient_id in assigned_rooms:
        room=assigned_rooms[patient_id]["room_type"]["beds"]
        rooms[room]+=1
        assigned_rooms.pop(patient_id)
        a=patient.pop(patient[patient_id]["room_type"])
        print(f"The patient has been Discharged from {a} Room")
    discharged_patients.update({patient_id:{"discharge_date":discharge_date,"follow_up_instructions":follow_up_instructions}})
    records.update({"patient_id":patient_id,"admission_date":admission_date,"discharge_date":discharge_date})
    hopspital_efficiency.append(records)
    

