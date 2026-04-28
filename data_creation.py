import pandas as pd
import random
import os

# === PATH SETTINGS ===
base_path = r"E:\archive (4)\mimic-iv-clinical-database-demo-2.2\hosp"

# === LOAD REQUIRED FILES ===
print("📂 Loading CSV files...")

patients = pd.read_csv(os.path.join(base_path, "patients.csv"))
admissions = pd.read_csv(os.path.join(base_path, "admissions.csv"))
diagnoses = pd.read_csv(os.path.join(base_path, "diagnoses_icd.csv"))
d_diag = pd.read_csv(os.path.join(base_path, "d_icd_diagnoses.csv"))
procedures = pd.read_csv(os.path.join(base_path, "procedures_icd.csv"))
d_proc = pd.read_csv(os.path.join(base_path, "d_icd_procedures.csv"))
prescriptions = pd.read_csv(os.path.join(base_path, "prescriptions.csv"))

print("✅ Files loaded successfully!")


# === MERGE DESCRIPTION TABLES ===
print("🔗 Merging description tables...")

diagnoses = diagnoses.merge(d_diag, on="icd_code", how="left")
procedures = procedures.merge(d_proc, on="icd_code", how="left")

# === MERGE PATIENT AND ADMISSION INFO ===
merged = admissions.merge(patients, on="subject_id", how="left")

print("✅ Merged admissions + patients data!")


# === HELPER FUNCTION ===
def collect_text(df, hadm_id, text_col):
    """Collect and join multiple entries into a short text."""
    if "hadm_id" not in df.columns:
        return ""
    items = df[df["hadm_id"] == hadm_id][text_col].dropna().unique().tolist()
    if not items:
        return ""
    return "; ".join(items[:3])  # take only first few for brevity


# === GENERATE SYNTHETIC NOTES ===
print("🧠 Generating synthetic clinical notes...")

records = []
for i, row in merged.iterrows():
    hadm_id = row["hadm_id"]
    gender = row.get("gender", "Unknown")
    age = row.get("anchor_age", random.randint(25, 80))

    diag = collect_text(diagnoses, hadm_id, "long_title")
    proc = collect_text(procedures, hadm_id, "long_title")
    meds = collect_text(prescriptions, hadm_id, "drug")

    # If no diagnosis text found, create a placeholder
    if not diag:
        diag = random.choice([
            "general medical checkup",
            "chest pain evaluation",
            "hypertension management",
            "diabetes follow-up",
            "fever and infection control"
        ])

    note = (
        f"{gender} patient aged {age} years admitted for {diag}. "
        f"Underwent procedures: {proc or 'none listed'}. "
        f"Medications prescribed: {meds or 'not available'}. "
        f"Discharged with advice for follow-up."
    )

    records.append({
        "subject_id": row["subject_id"],
        "hadm_id": hadm_id,
        "admittime": row.get("admittime", ""),
        "dischtime": row.get("dischtime", ""),
        "note": note
    })

print(f"✅ Generated {len(records)} synthetic notes!")


# === CREATE FINAL DATAFRAME ===
synthetic_notes = pd.DataFrame(records)

# === SAVE AS CSV ===
output_path = os.path.join(base_path, "noteevents_synthetic.csv")
synthetic_notes.to_csv(output_path, index=False)
print(f"💾 Synthetic noteevents created successfully at:\n{output_path}")

# === DISPLAY SAMPLE ===
print("\n📄 Sample Rows:")
print(synthetic_notes.head(5))
