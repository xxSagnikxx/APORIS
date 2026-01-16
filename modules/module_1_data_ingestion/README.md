## 1. Datasets Used

This project utilises three large-scale datasets sourced from official UIDAI APIs to analyse Aadhaar enrolment and update activity across India.

---

### 1.1 Aadhaar Enrolment Dataset

**Source:** UIDAI API – Enrolment Activity  
**Records:** 1,006,029  
**Coverage:** 55 States/UTs, 984 Districts, 19,463 Pincodes  
**Date Range:** 2 March – 31 December 2025 (304 days)  
**Frequency:** Daily  

#### Columns
| Column | Type | Description | Example |
|------|------|-------------|---------|
| `date` | Date | Date of enrolment activity | 2025-03-02 |
| `state` | String | State / UT name | Uttar Pradesh |
| `district` | String | District name | Kanpur Nagar |
| `pincode` | String (6-digit) | Postal PIN code | 208001 |
| `age_0_5` | Integer | Aadhaar enrolments (ages 0–5) | 29 |
| `age_5_17` | Integer | Aadhaar enrolments (ages 5–17) | 82 |
| `age_18_greater` | Integer | Aadhaar enrolments (ages 18+) | 12 |

**Total Enrolments:** 5,435,702  

**Key Insight:**  
Approximately **51% of enrolments correspond to children (ages 0–17)**, indicating strong linkage between Aadhaar enrolment, birth registration, and school systems.

---

### 1.2 Demographic Updates Dataset (Non-Biometric)

**Source:** UIDAI API – Profile Updates  
**Records:** 2,071,700  
**Date Range:** 1 March – 29 December 2025  
**Frequency:** Daily  

**Includes:** Name changes, address updates, mobile number linking, email updates, marital status changes, and related demographic modifications.

#### Columns
| Column | Type | Description |
|------|------|-------------|
| `date` | Date | Date of demographic update |
| `state` | String | State / UT name |
| `district` | String | District name |
| `pincode` | String | Postal PIN code |
| `demo_age_5_17` | Integer | Demographic updates (ages 5–17) |
| `demo_age_17_` | Integer | Demographic updates (ages 17+) |

**Total Demographic Updates:** 49,295,187  

**Key Insight:**  
High demographic update intensity in certain regions (e.g., **Chandigarh: 30,602 updates per 1,000 enrolments**) reflects significant population mobility and extensive Aadhaar–KYC seeding.

---

### 1.3 Biometric Updates Dataset

**Source:** UIDAI API – Biometric Updates  
**Records:** 1,861,108  
**Date Range:** 1 March – 29 December 2025  
**Frequency:** Daily  

**Includes:** Fingerprint re-capture, iris scan updates, and photograph updates.

#### Columns
| Column | Type | Description |
|------|------|-------------|
| `date` | Date | Date of biometric update |
| `state` | String | State / UT name |
| `district` | String | District name |
| `pincode` | String | Postal PIN code |
| `bio_age_5_17` | Integer | Biometric updates (ages 5–17) |
| `bio_age_17_` | Integer | Biometric updates (ages 17+) |

**Total Biometric Updates:** 69,763,095  

**Key Insight:**  
Exceptionally high biometric update rates in small UTs (e.g., **Daman & Diu: 99,318 updates per 1,000 enrolments**) may indicate a small enrolment base or potential data aggregation artefacts.

---

### Data Quality Summary

| Metric | Enrolment | Demographic | Biometric |
|------|-----------|-------------|-----------|
| Records | 1,006,029 | 2,071,700 | 1,861,108 |
| Duplicate Records* | 2.28% | 22.86% | 5.10% |
| Negative Counts | 0 | 0 | 0 |
| Missing Dates | 0 | 0 | 0 |
| Geographic Coverage | 55 states, 984 districts | 65 states, 982 districts | 57 states, 973 districts |

\*Duplicates primarily arise from batch-wise district or state-level reporting and are resolved through aggregation during analysis.

---

## 2. Methodology

### 2.1 Data Ingestion
- Each dataset was provided in multiple CSV partitions (up to five files per dataset).
- All partitions were loaded and concatenated vertically using **pandas**.
- **Approximate code length:** ~10 lines per dataset.

### 2.2 Field Standardisation
- Parsed dates into datetime format.
- Standardised state and district names (whitespace removal, consistent casing).
- Converted pincodes to fixed 6-character strings to preserve leading zeros.
