print("--23--6--25--")
hospital=[]
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

def register_patient(patient_id, personal_info, medical_history, insurance_info):
    if patient_id  not in patient:
        patient.update({ patient_id:{
                "personal_info":personal_info,
                "medical_history":medical_history,
                "insurance_info":insurance_info}
    })
        print(f"Registration of {patient_id} ID successfull")

    else:
        print("Already Registered")

def add_medical_staff(staff_id, name, specialization, shift_schedule, contact_info):
   medical_staffs.update({
       staff_id:{"name":name,
            "specialization":specialization,
            "shift_schedule":shift_schedule,
            "contact_info":contact_info}   
   })


def schedule_appointment(patient_id, doctor_id, appointment_date, appointment_type):
    if patient_id in patient:
        appointment.update({
        patient_id:{"doctor_id":doctor_id,
                    "appointment_date":appointment_date,
                    "appointment_type":appointment_type}
    })
        print(f"""The appointment has been scheduled on {appointment_date}
        with Dr.{medical_staff[doctor_id]["name"]}""")
    else:
        print("Register the patient ")


# def create_medical_record(patient_id, doctor_id, diagnosis, treatment, prescription):
    if patient_id in patient:
#     medical_record.update({
#         patient_id:{"doctor_id":doctor_id, "diagnosis":diagnosis, "treatment":treatment, "prescription":prescription}
#     })
    else:
        print("Register the patient ")


def process_billing(patient_id, services_list, insurance_coverage):
    billing.update({
        patient_id:{
        "service_list":services_list,
        "insurance_coverage":insurance_coverage}
    })
    sum_of_services=sum(cost for services,cost in services_list) 
    if billing[patient_id]["insurance_coverage"] :
        sum_of_services+=(billing[patient_id]["insurance_coverage"])/100*sum_of_services
    
    if patient_id in assigned_rooms :
        admi_date=assigned_rooms[patient_id]["admission_date"]
    if patient_id in discharged_patients:
        disc_date=discharged_patients[patient_id]["discharge_date"]
    print(f"""=== BILLING SUMMARY ===
Patient: {patient[patient_id]["personal_info"]["name"]}
Admission Date: {admi_date}
Discharge Date: {disc_date}
Service Charges:
Room Charges ( days):  """)
    for key,value in services_list:
        print(f"{key}:{value}")
    sum_of_services=sum(cost for services,cost in services_list) 
    print(f"Total bill : ",sum_of_services)
    if billing[patient_id]["insurance_coverage"] :
        after_insurance=(billing[patient_id]["insurance_coverage"])/100*sum_of_services+sum_of_services
    print(f"Insurance ({billing[patient_id]["insurance_coverage"]}) : {after_insurance}")
    print(f"patient responsibility : {sum_of_services-after_insurance}")
    


# def manage_emergency_admission(patient_id, emergency_type, severity_level):
#     emergency.update({
#         patient_id:{"emergency_type":emergency_type,"severity_level":severity_level}
#     })
#    

# def track_medication_inventory(medication_id, quantity, expiry_date, supplier):
#     medicine.update({
#         medication_id:{"quantity":quantity,"expiry_date":expiry_date,"supplier":supplier}
#     })
rooms={
        "general-ward":{"beds":20,
        "price":1500},
        "private room":{"beds":15,
        "price":3000},
        "emergency room":{"beds":10,
        "price":5000}
    }    
# def assign_room(patient_id, room_type, admission_date, expected_duration):
#    
#     room_type=room_type.lower()
#     if rooms[room_type]["beds"]>0:
#         assigned_rooms.update({patient_id:{"room_type":room_type,"admission_date":admission_date,"exp_duaration":expected_duration}})
#         rooms[room_type]["beds"]-=1
#     else:
#         print(f"Currently the {room_type} is unavailable Opt for other rooms")

def calculate_treatment_cost(patient_id, treatment_plan, insurance_details):
    pass
def generate_patient_report(patient_id, report_type):
    patient_report.update({patient_id:report_type})
    return patient_report
def analyze_hospital_efficiency(metrics_type, time_period):
    pass
def manage_discharge_process(patient_id, discharge_date, follow_up_instructions):
    if patient_id in assigned_rooms:
        room=assigned_rooms[patient_id]["room_type"]["beds"]
        rooms[room]+=1
        assigned_rooms.pop(patient_id)
    discharged_patients.update({patient_id:{"discharge_date":discharge_date,"follow_up_instructions":follow_up_instructions}})
    return discharged_patients