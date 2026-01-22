from load_cleaned_data import load_enrolment, load_demographic, load_biometric
def clean_all():
    enrol = load_enrolment()
    demo = load_demographic()
    bio = load_biometric()
    for df in [enrol, demo, bio]:
        df.columns = df.columns.str.lower().str.strip()
    enrol["total_enrolment"] = (
        enrol["age_0_5"] + enrol["age_5_17"] + enrol["age_18_greater"]
    )
    return enrol, demo, bio
