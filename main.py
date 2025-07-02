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
records=[]

def register_patient(patient_id,name,personal_info, medical_history, insurance_info):
    if patient_id in emergency:
        patient[patient_id].update({"name":name,"personal_info":personal_info,"medical_history":medical_history,"insurance_info":insurance_info})
        return
    if patient_id  not in patient:
        patient.update({ patient_id:{"name":name,
                "personal_info":personal_info,
                "medical_history":medical_history,
                "insurance_info":insurance_info}
    })
        print(f"Registration of {patient_id} ID successfull")

    else:
        print("Already Registered")



def add_medical_staff(staff_id, name, specialization=None, shift_schedule=None, contact_info=None):
 if staff_id not in medical_staffs:
   medical_staffs.update({
       staff_id:{"name":name,
            "specialization":specialization,
            "shift_schedule":shift_schedule,
            "contact_info":contact_info}   
   })
   print(f"Medical Staff ('ID'{staff_id}) is added ")
 else:
     print("The Staff already exists")



def schedule_appointment(patient_id, doctor_id, appointment_date, appointment_type):
    appt_datetime = datetime.strptime(appointment_date, "%d-%m-%Y %H:%M")

    if doctor_id not in appointment:
        appointment[doctor_id] = []
    for appt in appointment[doctor_id]:
        existing_time = datetime.strptime(appt["appointment_date"], "%d-%m-%Y %H:%M")
        if existing_time == appt_datetime:
            print("Appointment Conflict")
            return

    if patient_id in patient and doctor_id in medical_staffs:
        appointment[doctor_id].append({
            "patient_id": patient_id,
            "appointment_date": appointment_date,
            "appointment_type": appointment_type
        })
        print(f"""The appointment has been scheduled at {appointment_date}
with {medical_staffs[doctor_id]['name']}""")
        patient[patient_id].update({"doctor":doctor_id})
    else:
        print("Register the patient or doctor first")


def doctors_schedule(doctor_id):
    if doctor_id not in appointment or doctor_id not in medical_staffs:
        print("Doctor not found or has no appointments")
        return

    doctor = medical_staffs[doctor_id]
    print(f"{doctor['name']} - ({doctor['specialization']})")
    today = datetime.today().date()
    print(datetime.strftime(datetime.today(), "%B %d, %Y")) 
    found_today = False
    for appt in appointment[doctor_id]:
        appt_datetime = datetime.strptime(appt["appointment_date"], "%d-%m-%Y %H:%M")
        if appt_datetime.date() == today:
            if not found_today:
                print("Today's Appointments:")
                print("----------------------")
                found_today = True
            print(f"{appt_datetime.strftime('%H:%M')} - Patient ID: {appt['patient_id']} ({appt['appointment_type']})")

    if not found_today:
        print("No appointments today.")

rooms={
        "general room":{"beds":20,
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


def manage_discharge_process(patient_id,admission_date, discharge_date, follow_up_instructions):
    if patient_id in assigned_rooms:
        room_ty=patient[patient_id]["room_type"]#genrerl room
        rooms[room_ty]["beds"]+=1
        a=patient[patient_id].pop("room_type")
        print(f"The patient has been Discharged from {a} ")
    discharged_patients.update({patient_id:{"discharge_date":discharge_date,"follow_up_instructions":follow_up_instructions}})
    hopspital_efficiency.append({"patient_id":patient_id,"admission_date":admission_date,"discharge_date":discharge_date})


def manage_emergency_admission(patient_id,doctor_id,admission_date,emergency_type, severity_level):
    emergency.update({
        patient_id:{"emergency_type":emergency_type,"admission_date":admission_date,"severity_level":severity_level}
    })
    patient.update({ patient_id:{"name":None,
                "personal_info":None,
                "medical_history":"Emergency",
                "insurance_info":None}
    })
    
    assigned_rooms.update( {patient_id :{"room_type":"emergency room","admission_date":admission_date,"exp_duaration":None}
                            })
    rooms["emergency room"]["beds"]-=1
    patient[patient_id]["room_type"]="emergency room"
    patient[patient_id["doctor"]]=doctor_id
    
   

def create_medical_record(patient_id, doctor_id, treatment, prescription, diagnosis ):
    if patient_id in emergency:
        medical_record[patient_id].update({"doctor_id":doctor_id, "diagnosis":diagnosis, "treatment":treatment, "prescription":prescription})
 
    for app in appointment[doctor_id]:
        if patient_id == app["patient_id"]:
            medical_record.update({
                patient_id:{"doctor_id":doctor_id, "diagnosis":diagnosis, "treatment":treatment, "prescription":prescription}
            })
            print("Medical record Created")
            break
    else:
        print("Register the patient ")


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


def process_billing(patient_id, services_list, insurance_coverage=None):
    billing.update({
        patient_id:{
        "service_list":services_list,
        "insurance_coverage":insurance_coverage}
    })
    
    u=assigned_rooms[patient_id]["admission_date"]
    admi_date=datetime.strptime(u, "%d-%m-%Y")
    v=discharged_patients[patient_id]["discharge_date"]
    disc_date=datetime.strptime(v,"%d-%m-%Y")
   
    
    print(f"""=== BILLING SUMMARY ===
Patient: {patient[patient_id]["name"]}
Admission Date: {admi_date.strftime('%B %d,%Y')}
Discharge Date: {disc_date.strftime('%B %d,%Y')}
Service Charges:""")
    for key,value in services_list.items():
        print(f"{key}:{value}")
        
    sum_of_services=sum(cost for services,cost in services_list.items()) 
    Sum_fo_Serices=sum_of_services
    print(f"Total bill : {Sum_fo_Serices}")
    if billing[patient_id]["insurance_coverage"] :
        after_insurance=(billing[patient_id]["insurance_coverage"])/100*Sum_fo_Serices
        print(f"Insurance ({billing[patient_id]["insurance_coverage"]}) : {after_insurance}")
        print(f"patient responsibility : {Sum_fo_Serices-after_insurance}")
    else:
        print("You have no insurance coverage")
        print(f"Patient Responsibility : {Sum_fo_Serices}")

def calculate_treatment_cost(patient_id, treatment_plan, insurance_details):
    ins=insurance_details
    cost=0
    for plan,price in treatment_plan.items():
        cost+=price
        
    admi_date=datetime.strptime(assigned_rooms[patient_id]["admission_date"], "%d-%m-%Y")
    disc_date=datetime.strptime(discharged_patients[patient_id]["discharge_date"],"%d-%m-%Y")
    print(f"""=== BILLING SUMMARY ===
Patient: {patient[patient_id]["name"]}
Admission Date: {datetime.strftime(admi_date, "%B %d, %Y")}
Discharge Date: {datetime.strftime(disc_date, "%B %d, %Y")}""")
    print(f"The cost of the Treatment : {cost}")
    if ins["coverage"]:
        ins_cost=cost*ins["coverage"]/100
        print(f"The insurance coverage {ins["coverage"]} % : {ins_cost}")
        print(f"Patients responsibility :{cost-ins_cost}")
    else:
        print("You have no insurance coverage")
        print(f"Patients Responsibility : {cost}")



def generate_patient_report(patient_id, report_type):
 if patient_id in medical_record:
    patient_report.update({patient_id:report_type})
    print()
    print("---PATIENT REPORT---")
    print(f"""Patient Name : {patient[patient_id]["name"]} ('ID'{patient_id})
Age : {patient[patient_id]["personal_info"]["age"]}| Gender :{patient[patient_id]["personal_info"]["gender"]}| Blood Type : {patient[patient_id]["personal_info"]["blood_type"]}
Insurance : {patient[patient_id]["insurance_info"]["company"]} ('ID'{patient[patient_id]["insurance_info"]["policy_no"]})""")
    if patient_id in discharged_patients:
        status = "Discharged"
    elif patient_id in assigned_rooms:
        status = "Inpatient"
    else :
        status = "Outpatient"
    admi_date=datetime.strptime(assigned_rooms[patient_id]["admission_date"], "%d-%m-%Y")
    print(f"Current Status : {status}")
    print(f"Room : {assigned_rooms[patient_id]["room_type"]}")
    print(f"Admitted : {datetime.strftime(admi_date, "%B %d, %Y")}")
    dis=patient[patient_id]["doctor"]
    doc_name=medical_staffs[dis]["name"]

    print(f"Attending Doctor : {doc_name} ")
    today=datetime.today()
    print(f"Recent Vitals ({datetime.strftime(today,"%B %d, %Y - %H:%M %p")}:)")
    for key,value in report_type.items():
        print(f"{key}:{value}")
    print("Active Medications : ")
    for i in medical_record[patient_id]["prescription"]:
        print(f"{i["medicine"]} ({i["dosage"]}) : {i["frequency"]}")
        
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
    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")

    total_stay_days = 0
    total_patients = 0
    occupied_bed_days = 0

    for record in hopspital_efficiency:
        admission = datetime.strptime(record["admission_date"], "%d-%m-%Y")
        discharge = datetime.strptime(record["discharge_date"], "%d-%m-%Y")

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



while True:
    print("--------------------------------------------")
    print("1.To Register a Patient\n2.To add a Medical Staff\n3.To view the Medical Staff\n4.To schedule an Appointment\n5.Emergency Admission\n6.Create medical record\n7.To Assign Room\n8.Discharge from room\n9.Process Biling\n10.Generate Patient Report \n11.Analyze Hospital Efficieny\n12.Exit")
    ch=input("Enter option : ")
    if ch=="1":
        p_id=int(input("Enter patient id : "))
        p_name=input("Enter name : ")
        age=int(input("Enter age : "))
        gender=input("Enter Gender : ")
        blood_type=input("Enter Blood Type : ")
        person_info={"age":age,"gender":gender,"blood_type":blood_type}
        medic_history=input("Enter Medical history : ")
        ins_com,ins_policy=input("Enter Insurance Details [company] [policy no] : ").split()
        insurance={"company":ins_com,"policy":ins_policy}
        register_patient(p_id,p_name,person_info, medic_history, insurance)
       
    elif ch=="2":
        staff=int(input("Enter Staff id [Unique]: "))
        d_name=input("Enter Staff Name : ")
        if d_name[0:2]=="Dr":
            speciality=input("Enter Specialization : ")
            shift=input("Enter Shift Schedule : ")
            contact=input("Enter the contact number : ")
            add_medical_staff(staff, d_name, speciality, shift, contact)
        else:
            shift=input("Enter Shift Schedule : ")
            contact=input("Enter the contact number : ")
            add_medical_staff(staff, d_name, shift, contact)
    
    elif ch=="3":
        for doc_id,value in medical_staffs.items():
            print(f"Doctor Id : {doc_id}")
            for key,val in value.items():
                print(f"{key} : {val}")
            print("-----------------------")
    elif ch=="4":
        p_id=int(input("Enter Patient Id : "))
        d_id=int(input("Enter Doctor Id : "))
        appt_date=input("Enter Appointment date [DD-MM-YYYY H:M] : ")
        appt_type=input("Enter Appintment Type : ")
        schedule_appointment(p_id, d_id, appt_date, appt_type)

    elif ch=="5":
        p_id=int(input("Enter Patient Id : "))
        for doc_id,value in medical_staffs.items():
            print(f"Doctor Id : {doc_id}")
            for key,val in value.items():
                print(f"{key} : {val}")
            print("-----------------------")
        d_id=int(input("Enter Doctor Id : "))
        admi_date=input("Enter Admission date [DD-MM-YYYY] : ")
        emergency_type=input("Enter Emergency Type : ")
        s_Level=input("Enter Severity level : ")
        manage_emergency_admission(p_id,d_id,admi_date,emergency_type, s_Level)

    elif ch=="6":
        p_id=int(input("Enter Patient Id : "))
        d_id=int(input("Enter Doctor Id : "))
        diag=input("Enter Diagnosis : ")
        treatment=input("Enter Treatment : ")
        num=int(input("No of Medicines : "))
        prescription={}
        for i in range(num):
            medi=input("Enter Medicine Name : ")
            dosage=input("Enter Dosage [ex:500mg] : ")
            freq=input("Enter Frequency [ex:Twice Daily] : ")
            prescription.update({"medicine":medi,"dosage":dosage,"frequency":freq})
        create_medical_record(p_id, d_id, diag, treatment, prescription)
    elif ch=="7":
        p_id=int(input("Enter Patient Id : "))
        room_type=input("Enter room_type : ")
        admi_date=input("Enter Admission date [DD-MM-YYYY] : ")
        exp_duaration=input("Enter Expected Duration : ")
        assign_room(p_id, room_type, admi_date, exp_duaration)
    elif ch=="8":
        p_id=int(input("Enter Patient Id : "))
        admi_date=input("Enter Admission date [DD-MM-YYYY] : ")
        disc_date=input("Enter Discharge date [DD-MM-YYYY] : ")
        follow_up_instr=input("Enter Follow Up Instruction : ")

        manage_discharge_process(p_id, admi_date, disc_date, follow_up_instr)

    elif ch=="9":
        p_id=int(input("Enter Patient Id : "))
        lis=int(input("Enter Number of Services Provided : "))
        serv_list={}
        for i in range(lis):
            a=input("Enter the Services and Price [Services:Price] : ")
            services,price=a.spilt(":")
            serv_list[services]=price
        yn=input("Does the patient has insurance coverage[yes or no] : ").lower()
        if yn=="yes":
            c=int(input("Enter Insurance Coverage (ex:60): "))
            process_billing(p_id, serv_list, c)
        else:
            process_billing(p_id, serv_list)

    elif ch=="10":
        p_id=int(input("Enter Patient Id : "))
        num=int(input("Enter number of report provided : "))
        r_type={}
        for i in range(num):
            a=input("Enter Patient's Report [BP:67] : ")
            b,c=a.split(":")
            r_type[b]=c
        generate_patient_report(p_id, r_type)

    elif ch=="11":
        time_period=tuple(input("Enter time period (DD-MM_YYYY,DD-MM-YYYY) : "))
        print("""Enter Metrics Type \n1.average_length_of_stay\n2.bed_occupancy_rate\n3.patient_throughput """)
        ch=input("Enter Choice : ")
        if ch=="1":
            analyze_hospital_efficiency("average_length_of_stay", time_period)
        elif ch=="2":
            analyze_hospital_efficiency("bed_occupancy_rate", time_period)
        elif ch=="3":
            analyze_hospital_efficiency("patient_throughput ", time_period)
            

        
    elif ch=="12":
        print("THANK YOU")
        break