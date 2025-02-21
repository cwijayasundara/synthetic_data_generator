data_gen_prompt = """
You are a helpful assistant designed to generate data. You will be given a format for the data to generate and some examples of the data.

When generating Patient IDs, use the format 'P' followed by a three-digit number (e.g., P006, P941, P319).

Intentionally make some mistakes in the data generation and document them in the appropriate columns ('Is Valid' and 'Issue') if the row of data is invalid.

The types of mistakes to include are:

- **Allergy Contradictions**: Prescribing a medication that the patient is allergic to (e.g., prescribing Penicillin to a patient allergic to Penicillin).
- **Medical History and Medication Mismatch**: A patient with a medical condition not receiving appropriate medication (e.g., a diabetic patient not prescribed any diabetes medication).
- **Lab Results and Diagnosis Mismatch**: Lab results that do not support the diagnosis (e.g., normal glucose levels but diagnosed with Diabetes Type 2).
- **Other Plausible Mistakes**: Any other realistic errors that could occur in medical records, such as incorrect gender entries, impossible dates of birth, or inconsistent treatment plans.

Ensure that when 'Is Valid' is 'False', the 'Issue' column clearly explains the problem.

Return 100 rows of data for the user. Your response should strictly be in the format of a valid CSV.

Generate Synthetic Medical Records Dataset with the following columns:
    - Patient ID: A randomly generated patient id
    - Date of Birth: Date of birth of the patient
    - Gender: M/F
    - Medical History: Past diagnoses
    - Current Medications: Medication the patient is taking
    - Allergies: Identified allergies
    - Lab Results (Glucose mg/dL)
    - Diagnoses: Current diagnosis
    - Treatment Plan: Current treatment plan
    - Is Valid: Whether or not the current row of data is valid (True/False)
    - Issue: If the row of data is not valid, what the issue is

{examples}

"""

data_examples = """
Patient ID,Date of Birth,Gender,Medical History,Current Medications,Allergies,Lab Results (Glucose mg/dL),Diagnoses,Treatment Plan,Is Valid,Issue
P001,1980-05-14,M,Hypertension,Lisinopril,None,110,Hypertension,Continue Lisinopril,True,
P002,1975-11-30,F,Diabetes Type 2,Metformin,Penicillin,90,Diabetes Type 2,Continue Metformin,True,
P003,1990-07-22,F,Asthma,Albuterol,Aspirin,85,Asthma,Prescribe Albuterol,True,
P004,2000-03-10,M,None,Amoxicillin,Penicillin,95,Infection,Prescribe Amoxicillin,False,Prescribed Amoxicillin despite Penicillin allergy
P005,1985-09-18,F,Hyperlipidemia,Atorvastatin,None,200,Hyperlipidemia,Continue Atorvastatin,True,
P006,1978-12-05,M,Hypertension; Diabetes Type 2,Lisinopril; Insulin,None,55,Diabetes Type 2,Adjust insulin dosage,False,Low glucose level not properly addressed
"""