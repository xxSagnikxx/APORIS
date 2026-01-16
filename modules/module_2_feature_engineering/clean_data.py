from load_cleaned_data import (
    load_enrolment,
    load_demographic_updates,
    load_biometric_updates
)

#missing ar negative value handle korar jonne

def clean_all():
    enrol = load_enrolment()
    demo = load_demographic_updates()
    bio = load_biometric_updates()

    enrol = enrol[enrol["enrolments"] >= 0]
    demo = demo[demo["updates"] >= 0]
    bio = bio[bio["updates"] >= 0]

    return enrol, demo, bio
