APORIS – National Identity Analytics Dashboard
📌 Overview

APORIS is an interactive Streamlit-based analytics dashboard designed to analyze national identity enrolment data across Indian states and districts.
It provides executive insights, regional risk visualization, trend analysis, and forecasting for data-driven planning.

🚀 Features

Executive Overview

Key KPIs: total enrolments, coverage %, pending updates

Region-Wise Risk Analysis

State-level risk visualization based on enrolment and coverage

Trend & Anomaly Detection

Time-based enrolment trends with state-wise filtering

Forecast & Planning

Predictive enrolment trends for planning and capacity estimation

Dark / Light Mode UI

Modular Streamlit Architecture

🗂 Project Structure
APORIS/
├── dashboard/
│   ├── app.py
│   ├── pages/
│   └── assets/
├── data/
│   └── final_dataset.csv
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/APORIS.git
cd APORIS

2️⃣ Create a virtual environment (recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the Application

From the root APORIS folder, run:

streamlit run dashboard/app.py


The app will start at:

http://localhost:8501

📊 Data Source

data/final_dataset.csv

Columns:

state

total_enrolment

districts

🛠 Tech Stack

Python 3.10+

Streamlit

Pandas

Plotly

NumPy

📌 Notes

Virtual environments are not included in the repository.

All visualizations are generated dynamically from the dataset.

Forecasting is deterministic and intended for planning simulation (not statistical prediction).

📄 License

This project is for academic and research use.