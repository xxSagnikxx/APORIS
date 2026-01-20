# APORIS - Aadhaar Predictive Operations and Risk Intelligence System

![UIDAI Hackathon 2026](https://img.shields.io/badge/UIDAI%20Hackathon-2026-003366?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Prototype%20Ready-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white&style=for-the-badge)

> **Submission for UIDAI Data Hackathon 2026** > **Theme:** Smart Governance / Fraud Detection  
> **Problem Statement:** Unlocking Societal Trends in Aadhaar Enrolment and Updates

---

## 📖 Overview

**APORIS** is an end-to-end predictive analytics pipeline designed to monitor the health of the Aadhaar enrolment ecosystem. By moving beyond traditional reactive reporting, APORIS leverages machine learning and time-series forecasting to identify operational anomalies, predict future resource loads, and quantify risk at the state and district levels.

The system serves as a **Single Source of Truth** for administrators, transforming raw API logs into actionable intelligence.

---

## 🚩 Problem Statement

**Unlocking Societal Trends in Aadhaar Enrolment and Updates** *Identify meaningful patterns, trends, anomalies, or predictive indicators and translate them into clear insights or solution frameworks that can support informed decision-making and system improvements.*

**The Challenge:**
- **Data Silos:** Disconnected analysis of Enrolment vs. Update streams.
- **Reactive Audits:** Inability to catch update fraud (e.g., non-biometric spikes) in real-time.
- **Resource Mismatch:** Lack of forward-looking data to plan enrolment kit deployment.

---

## 🏗️ System Architecture

The project is structured into **7 Analytical Modules** feeding into a central Dashboard:

1.  **Ingestion:** Unifying Enrolment, Demographic, and Biometric datasets.
2.  **Engineering:** Creating derived features like `update_ratio` and `future_load_pressure`.
3.  **Analytics:** Establishing baseline demographic norms (e.g., Child vs. Adult enrolment).
4.  **Forecasting:** Predicting future system load using **Facebook Prophet**.
5.  **Anomaly Detection:** Flagging outliers using **Isolation Forest** (Unsupervised Learning).
6.  **Classification:** Diagnosing the root cause of anomalies (e.g., "High Update Frequency").
7.  **Risk Engine:** Generating a unified **Risk Score (0-100)** for every state.

---

## 📂 Project Structure

```text
APORIS/
├── dashboard/                  # Streamlit Admin Portal
│   └── app.py                  # Interactive Dashboard logic
├── docs/                       # Documentation & Reports
│   ├── main.tex                # LaTeX Source Code
├── modules/                    # Core Analytical Pipeline
│   ├── module_1_data_ingestion # Raw Data Processing
│   ├── module_2_feature_eng    # Feature Extraction
│   ├── module_3_descriptive    # Statistical Analysis
│   ├── module_4_forecasting    # Prophet Time-Series Models
│   ├── module_5_anomaly_det    # Isolation Forest Models
│   ├── module_6_cause_class    # Root Cause Classifier
│   └── module_7_risk_scoring   # Decision Support Engine
├── data/                       # Dataset Directory (Git LFS)
└── requirements.txt            # Python Dependencies
