print("--23--6--25--")
hospital=[]
medical_staffs={}
patient=[]
add={}
appointment={}
medical_record={}
billing={}
emerg={}
emergency={}
medi={}
medicine={}
assigned_rooms={}

def register_patient(patient_id, personal_info, medical_history, insurance_info):
    add.update({"patient_id":patient_id,
                "personal_info":personal_info,
                "medical_history":medical_history,
                "insurance_info":insurance_info

    })
    patient.append(add)

def add_medical_staff(staff_id, name, specialization, shift_schedule, contact_info):
   medical_staffs.update({
       name:{"staff_id":staff_id,
            "specialization":specialization,
            "shift_schedule":shift_schedule,
            "contact_info":contact_info}   
   })

add_medical_staff(101,"Dr.Shubhash","Cardiologist","Night-Schedule",9393933300)
print(medical_staffs)
print(medical_staffs['Dr.Shubhash']["specialization"])
  
def schedule_appointment(patient_id, doctor_id, appointment_date, appointment_type):
    appointment.update({
        patient_id:{"doctor_id":doctor_id,
                    "appointment_date":appointment_date,
                    "appointment_type":appointment_type}
    })

schedule_appointment(123,1021,"21-09-2025","General Ward")
print(appointment)
print(appointment[123]["doctor_id"])
def create_medical_record(patient_id, doctor_id, diagnosis, treatment, prescription):
    medical_record.update({
        patient_id:{"doctor_id":doctor_id, "diagnosis":diagnosis, "treatment":treatment, "prescription":prescription}
    })
# create_medical_record(123,1021,"Heart Attack","cardiac arrest","sunflowdiem")
# print(medical_record[123])

def process_billing(patient_id, services_list, insurance_coverage):
    billing.update({
        "patient_id":patient_id,
        "service_list":services_list,
        "insurance_coveerage":insurance_coverage
    })
    return sum(cost for services,cost in services_list)
print(process_billing(123,[["x-ray",430],["bed",900]],0.8))
print(billing)


def manage_emergency_admission(patient_id, emergency_type, severity_level):
    emerg.update({
        patient_id:{"emergency_type":emergency_type,"severity_level":severity_level}
    })
    emergency.update(emerg)
manage_emergency_admission(123,"accident",9)
print(emergency)
def track_medication_inventory(medication_id, quantity, expiry_date, supplier):
    medi.update({
        medication_id:{"quantity":quantity,"expiry_date":expiry_date,"supplier":supplier}
    })
    medicine.update(medi)
def assign_room(patient_id, room_type, admission_date, expected_duration):
    rooms={
        "general-ward":0,
        "private room":5,
        "emergency room":10
    }
    room_type=room_type.lower()
    if rooms[room_type]>0:
        assigned_room.update({patient_id:{"room_type":room_type,"admission_date":admission_date,"exp_duaration":expected_duration
        }})
        rooms[room_type]-=1
    else:
        print(f"Currently the {room_type} is unavailable Opt for other rooms")
assign_room(123,"GEneral-Ward","21-02-2021",12)
# def calculate_treatment_cost(patient_id, treatment_plan, insurance_details)
# def generate_patient_report(patient_id, report_type)
# def analyze_hospital_efficiency(metrics_type, time_period)
# def manage_discharge_process(patient_id, discharge_date, follow_up_instructions)
