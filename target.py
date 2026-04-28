import pandas as pd
import re
import os
import random
import json

# === PATH SETTINGS ===
base_path = r"E:\archive (4)\mimic-iv-clinical-database-demo-2.2\hosp"
notes_path = os.path.join(base_path, "noteevents_synthetic.csv")

print("📂 Loading synthetic notes...")
notes = pd.read_csv(notes_path)
print(f"✅ Loaded {len(notes)} synthetic notes.")

# === HELPER: EXTRACT STRUCTURED SECTIONS ===
def generate_summary(note):
    """
    Generate a basic structured summary from synthetic clinical note text.
    """
    note_lower = note.lower()

    # --- Complaint (Reason for Admission) ---
    complaint_match = re.search(r"admitted for (.*?)(?:\.|;|$)", note_lower)
    complaint = complaint_match.group(1).strip().capitalize() if complaint_match else "General checkup"

    # --- History (if something like 'history of' exists) ---
    history_match = re.search(r"history of (.*?)(?:\.|;|$)", note_lower)
    history = history_match.group(1).strip().capitalize() if history_match else random.choice([
        "No significant medical history",
        "Known case of hypertension",
        "Known case of diabetes"
    ])

    # --- Medication (from 'medications prescribed') ---
    meds_match = re.search(r"medications prescribed: (.*?)(?:\.|;|$)", note_lower)
    meds = meds_match.group(1).strip().capitalize() if meds_match else "Not available"

    # --- Plan (after 'discharged') ---
    plan_match = re.search(r"discharged (.*?)(?:\.|;|$)", note_lower)
    plan = plan_match.group(1).strip().capitalize() if plan_match else "Follow-up as needed"

    return {
        "Complaint": complaint,
        "History": history,
        "Medication": meds,
        "Plan": plan
    }

# === GENERATE STRUCTURED SUMMARIES ===
print("🧠 Extracting structured summaries...")

structured_records = []
for _, row in notes.iterrows():
    summary = generate_summary(row["note"])
    structured_records.append({
        "subject_id": row["subject_id"],
        "hadm_id": row["hadm_id"],
        "note": row["note"],
        "summary": summary
    })

print(f"✅ Extracted structured summaries for {len(structured_records)} notes!")

# === SAVE TO JSON FILE ===
output_json = os.path.join(base_path, "autodoc_dataset.json")
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(structured_records, f, indent=2)

print(f"💾 Saved structured dataset at:\n{output_json}")

# === DISPLAY SAMPLE ===
print("\n📄 Sample Entry:")
print(json.dumps(structured_records[0], indent=2))
