APORIS
National Identity Analytics Dashboard

APORIS is a Streamlit-based analytics dashboard designed to monitor, analyze, and visualize national identity enrolment data across India. The system provides executive insights, regional risk analysis, trend evaluation, and forecast-based planning through an interactive interface.

Features

Executive-level overview of key enrolment metrics

Region-wise risk visualization across states and UTs

Trend and anomaly analysis with state-wise filtering

Forecast and planning view for future enrolment patterns

Light and Dark mode support

Modular, scalable architecture

Project Structure
APORIS/
│
├── dashboard/
│   ├── app.py
│   ├── pages/
│   │   ├── executive_overview.py
│   │   ├── region_wise_risk.py
│   │   ├── trend_analysis.py
│   │   └── forecast_planning.py
│   │
│   └── assets/
│       └── styles.css
│
├── data/
│   └── final_dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore

Requirements

Python 3.10 or higher

Streamlit

Pandas

NumPy

Plotly

All dependencies are listed in requirements.txt.

Installation

Clone the repository:

git clone https://github.com/<your-username>/APORIS.git
cd APORIS


(Optional but recommended) Create a virtual environment:

Windows

python -m venv venv
venv\Scripts\activate


Linux / macOS

python -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Running the Application

From the root directory of the project, run:

streamlit run dashboard/app.py


Once started, open your browser and navigate to:

http://localhost:8501

Dataset Description

Dataset location:

data/final_dataset.csv


Columns used:

state – State or Union Territory name

total_enrolment – Total enrolment count

districts – Number of districts covered

Notes

The dashboard uses processed and aggregated data.

Forecast and trend visualizations are illustrative and intended for planning insights.

Virtual environments are intentionally excluded from the repository.

License

This project is developed for academic and research purposes.

Status

System pipeline connected and dashboard operational.
