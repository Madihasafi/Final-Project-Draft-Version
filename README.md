# Final-Project-Draft-Version
# 🎓 Understanding Stress Factors Among University Students

> **A data-driven exploration of how stress affects academic performance and well-being**

---

## 📌 The Problem

University students today face mounting pressure from academic workloads, social expectations, financial concerns, and lifestyle demands. Stress has become one of the most reported mental health concerns among students globally, yet universities often lack clear, data-backed insights into *what* is driving that stress and *how* it connects to academic outcomes.

**Who is affected?**
- University and college students
- Academic institutions and student affairs offices
- Mental health support services and counselors
- Policymakers shaping higher education welfare programs

**Why does this matter now?**  
Post-pandemic academic environments have intensified student stress. Burnout, anxiety, and declining academic performance are increasingly documented, but interventions remain generic. Targeted, evidence-based recommendations require understanding the actual drivers: Is it sleep deprivation? Study overload? Social isolation? This project aims to find out.

---

## 🎯 Project Goal

To identify and quantify the key lifestyle and academic factors — such as sleep hours, study time, GPA, and social activity, that are most strongly associated with higher stress levels among university students.

**Core question:**  
*"Which factors most significantly predict higher stress in university students, and what practical steps can institutions take in response?"*

---

## 📊 Datasets

This project combines **five publicly available datasets** from Kaggle to build a rich, comprehensive view of student stress:

| # | Dataset | Source | Key Variables |
|---|---------|--------|--------------|
| 1 | Student Academic Stress | Kaggle | Aca_stage,	Peer_press,	Aca_press_home,	Study_environment,	Coping_strategy,	bad_habits,	Aca_comp_rate,	Aca_stress_rate,	year,	month,	day,	semester |
| 2 | Stress Level Dataset | [Kaggle]([https://www.kaggle.com/datasets/rxnach/student-stress-factors-a-comprehensive-analysis?resource=download]| anxiety_level,	self_esteem,	mental_health_history,	depression,	headache,	blood_pressure,	sleep_quality,	breathing_problem,	noise_level,	living_conditions,	safety,	basic_needs,	academic_performance,	study_load,	teacher_student_relationship,	future_career_concerns,	social_support,	peer_pressure,	extracurricular_activities,	bullying,	stress_level |
| 3 | Student Stress Factors | Kaggle | Kindly Rate your Sleep Quality,	How many times a week do you suffer headaches?,	How would you rate you academic performance?,	how would you rate your study load?,	How many times a week you practice extracurricular activities?,	How would you rate your stress levels?  |
| 4 | Mental Health Survey | Kaggle | gender,	age,	university,	degree_level,	degree_major,	academic_year,	cgpa,	residential_status,	campus_discrimination,	sports_engagement,	average_sleep,	study_satisfaction,	academic_workload, 	academic_pressure,	financial_concerns,	social_relationships,	depression,	anxiety,	Self-Efficacy,	isolation,	future_insecurity,	stress_relief_activities,	Mental-Health |
| 5 | Student Mental Health | Kaggle | Timestamp,	Choose your gender,	Age,	What is your course?,	Your current year of Study,	What is your CGPA?,	Marital status,	Do you have Depression?,	Do you have Anxiety?,	Do you have Panic attack?,	Did you seek any specialist for a treatment? |

> **Next step:** These five datasets will be cleaned and merged into a single unified dataset with consistent variable naming, handled missing values, and normalized scales; ready for analysis.

**Key variables of interest:**
| Variable                     | Meaning              |
| ---------------------------- | -------------------- |
| stress_level                 | Target variable      |
| academic_performance         | Outcome              |
| study_load                   | Academic pressure    |
| sleep_quality                | Lifestyle factor     |
| anxiety                      | Mental state         |
| depression                   | Mental state         |
| social_support               | Social factor        |
| peer_pressure                | Social stress        |
| teacher_student_relationship | Academic environment |
| living_conditions            | External environment |
| future_career_concerns       | Psychological stress |

---

## 🔍 Expected Insights

The analysis aims to uncover patterns such as:

- Whether **lack of sleep** is the single strongest predictor of high stress
- Whether **academic workload** or **social isolation** plays a larger role
- Whether certain student profiles (year of study, gender, field) show systematically higher stress
- Quantifying the relationship: *"Each hour less of sleep is associated with X increase in reported stress score"*

---

## 🛠️ Tools & Methods
## 🗂️ Notebook Structure
| Step | Title | Platform / Tool |
|------|-------|-----------------|
| 1 | Setup & Install Libraries | Google Colab |
| 2 | Load Datasets & First Look | pandas |
| 3 | Column Names & Data Types | pandas |
| 4 | Descriptive Statistics | pandas |
| 5 | Stress Level Distributions | Plotly |
| 6 | Sleep Quality vs Stress | Plotly |
| 7 | Study Load vs Stress | Plotly |
| 8 | Mental Health Breakdown (Depression/Anxiety) | Plotly |
| 9 | Gender & Year of Study Analysis | Plotly |
| 10 | Correlation Heatmap | Plotly |
| 11 | Cross-Dataset Comparison | Plotly |
| 12 | Regression Analysis | scikit-learn |
| 13 | DuckDB — SQL Queries on DataFrames | DuckDB |
| 14 | Key Findings & Recommendation | Markdown summary |
---

## 📁 Project Structure

```
├── README.md                  ← Project Proposal
├── data/
│   ├── raw/                   ← Original Kaggle datasets (5 files)
│   └── processed/             ← Cleaned & merged dataset 
├── notebooks/
│   └── Final Project Draft Version Code.ipynb           ← Exploratory data analysis 
├── src/
│   └── data_cleaning_script.py       ← Data processing scripts 
└── visuals/                   ← Exported charts and figures
```

---

## 🗺️ Roadmap

- [x] **Step 1 - Project Proposal:** Define problem, identify datasets, set up repository
- [x] **Step 2 - Draft Version:** Clean and merge all 5 datasets; initial EDA and first visualizations
- [ ] **Step 3 - Final Presentation:** Full analysis, key insights, actionable recommendations, 5-minute presentation

---

## 💡 Intended Audience & Impact

This analysis is designed to be useful for:

- **University student wellness offices** : to redesign support programs around actual stress drivers
- **Academic advisors** : to identify at-risk students earlier
- **Policymakers** : to allocate mental health resources more effectively

If the findings confirm that sleep deprivation and heavy academic workloads are the dominant stressors, universities could implement evidence-backed interventions: adjusted exam schedules, mandatory wellness breaks, and sleep health campaigns.






