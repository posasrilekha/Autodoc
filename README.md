# 🩺 AutoDoc – Clinical Note Summarizer

AutoDoc is an AI-powered clinical note summarization system that converts unstructured medical notes into structured summaries using modern NLP techniques and transformer-based models.


## 🚀 Project Overview

AutoDoc helps in transforming lengthy clinical notes into a structured format:

* **Complaint**
* **History**
* **Medication**
* **Plan**

This improves readability, reduces manual effort, and assists healthcare professionals in faster decision-making.

## 📌 Features

* 🔍 Clinical note summarization using AI
* 🧠 Powered by GroqCloud (LLaMA-based model)
* 📊 Synthetic dataset generation (MIMIC-IV inspired)
* 🧾 Structured output formatting
* 🌐 Interactive UI using Streamlit
* ⚡ Fast inference with optimized API calls

## 🏗️ Project Structure

```
AutoDoc/
│── streamlit_app.py        # Main Streamlit UI app
│── data_creation.py        # Synthetic dataset generation
│── target.py               # Rule-based summary extraction
│── autodoc_dataset.json    # Structured dataset
│── noteevents_synthetic.csv
│── check.py               # Library checker
│── install.txt            # Required dependencies
│── Auto_Doc_Training.ipynb # Model training notebook
```

## 🧪 Sample Input

```
A 65-year-old male presents with chest pain radiating to the left arm...
```

## ✅ Sample Output

```
🩺 Complaint: Chest pain  
📜 History: Hypertension, Diabetes  
💊 Medication: Metformin  
🧭 Plan: Cardiac monitoring and aspirin
```


## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AutoDoc.git
cd AutoDoc
```

### 2️⃣ Install dependencies

```bash
pip install -r install.txt
```



## ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```


## 🧠 Model Details

* **Model Used:** `openai/gpt-oss-20b` (via Groq API) 
* **Frameworks:** Streamlit, Pandas, NumPy, PyTorch
* **Approach:** Prompt-based structured summarization


## 📊 Dataset

* Synthetic dataset generated using MIMIC-IV inspired clinical records 
* Includes:

  * Patient demographics
  * Diagnoses
  * Procedures
  * Medications
* Structured JSON dataset for training and evaluation 


## 🧩 How It Works

1. User inputs clinical note
2. Prompt is generated for structured summarization
3. Groq API processes the input
4. Output is formatted into readable sections
5. Results displayed via Streamlit UI


## 🛠️ Dependencies

Some key libraries used:

* TensorFlow, Keras
* NumPy, Pandas
* PyTorch
* Scikit-learn
* Streamlit
* Groq API

(See full list in `install.txt`) 

## 💡 Future Improvements

* 🔬 Fine-tuned medical NLP models
* 🏥 Integration with real hospital EHR systems
* 📱 Mobile app version
* 🌍 Multi-language support
* 📈 Evaluation metrics (ROUGE, BLEU)


## 📜 License

This project is for academic and research purposes.

## ⭐ Acknowledgements

* MIMIC-IV Dataset (inspiration)
* GroqCloud API
* Open-source AI community



Just tell 👍
