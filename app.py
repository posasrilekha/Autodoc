# streamlit_app.py
import streamlit as st
from groq import Groq
import os
import re

# ------------------------
# 2️⃣ Page configuration
# ------------------------
st.set_page_config(
    page_title="AutoDoc - Clinical Note Summarizer",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)
groq_client = Groq(api_key="gsk_aboYD5BcSaqcRWMs2mbzWGdyb3FYBUjFAuojGOBlEPThSvDztKKo0")
# ------------------------
# 3️⃣ Sidebar Information
# ------------------------
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("**Model:** AutoDoc (GroqCloud LLaMA-3)")
    st.markdown("**Dataset:** Synthetic MIMIC-IV Demo")
    st.markdown("**Developer:** Your Name")
    st.markdown("---")
    st.info("💡 Paste any clinical note or click *Try Sample Note* to test AutoDoc.")


# ------------------------
# 4️⃣ Main App Interface
# ------------------------
st.markdown("<h1 style='text-align:center;'>🩺 AutoDoc – Clinical Note Summarizer</h1>", unsafe_allow_html=True)

# --- Sample note ---
sample_note = (
    "A 65-year-old male presents with chest pain radiating to the left arm and shortness of breath "
    "for the past two days. Past medical history includes hypertension and type 2 diabetes mellitus. "
    "Patient is currently taking metformin and lisinopril. ECG shows mild ST depression. "
    "Plan to admit for cardiac monitoring and start aspirin."
)

# --- Input area ---
note = st.text_area("Paste Clinical Note Here:", height=150, placeholder="Type or paste clinical note text...")
if st.button("🧪 Try Sample Note"):
    note = sample_note
    st.session_state["note"] = note
    st.experimental_rerun()

# --- Summarize button ---
if st.button("🔍 Summarize"):
    if not note.strip():
        st.warning("⚠️ Please enter or paste a clinical note first.")
    else:
        st.info("⏳ Generating summary... please wait.")

        # Build prompt (unchanged)
        prompt = (
            f"Summarize the following clinical note into structured format:\n"
            f"Complaint:\nHistory:\nMedication:\nPlan:\n\n{note}"
        )

        # ------------------------
        # 5️⃣ GroqCloud Generation (NEW)
        # ------------------------
        with st.spinner("🧠 Contacting Transformer..."):
            try:
                response = groq_client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=250,
                    temperature=0.2,
                )
                summary = response.choices[0].message.content

            except Exception as e:
                st.error(f"Transformer Error: {e}")
                summary = "Error generating summary."

        # ------------------------
        # 6️⃣ Format summary neatly (unchanged)
        # ------------------------
        formatted = re.sub(r"(Complaint:)", r"\n\n🩺 **\1**", summary)
        formatted = re.sub(r"(History:)", r"\n\n📜 **\1**", formatted)
        formatted = re.sub(r"(Medication:)", r"\n\n💊 **\1**", formatted)
        formatted = re.sub(r"(Plan:)", r"\n\n🧭 **\1**", formatted)

        st.success("✅ Summary Generated Successfully!")
        st.markdown("### 🧾 Summary Output")
        st.markdown(formatted)


