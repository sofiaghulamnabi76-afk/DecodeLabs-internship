# DecodeLabs AI  Internship

**Batch:** 2026
**Role:** Artificial Intelligence  Intern
**Organization:** DecodeLabs

## Overview

This repository documents the projects completed during my AI Engineering internship at
DecodeLabs. Each project builds on core machine learning and software engineering
concepts, moving from rule-based systems toward supervised learning and predictive
modeling.

---

## Project 1: Rule-Based Chatbot

**Status:** ✅ Completed

**Description:**
A Python desktop GUI chatbot built with Tkinter, using rule-based response logic. The
interface follows a WhatsApp-style dark theme with quick-reply buttons and a clear-chat
function for a clean, familiar user experience.

**Key Skills:** GUI development, event-driven programming, rule-based logic design

---

## Project 2: Data Classification Using AI

**Status:** ✅ Completed

**Description:**
A supervised machine learning project that predicts heart disease risk from patient
clinical data. The project follows the DecodeLabs Input → Process → Output framework,
going beyond the base requirements with exploratory data analysis, hyperparameter
tuning, and multi-model benchmarking.

**Dataset:** UCI Heart Disease dataset — 303 patient records, 13 clinical features
(age, cholesterol, blood pressure, chest pain type, etc.), binary target
(disease / no disease).

**Pipeline:**
1. Load and understand the dataset (shape, missing values, class balance)
2. Exploratory Data Analysis (correlation heatmap, boxplots, scatter plots)
3. Feature scaling (`StandardScaler`)
4. Train-test split (80/20, stratified)
5. Model training — K-Nearest Neighbors (primary algorithm)
6. Hyperparameter tuning — sweeping K from 1–20 to find the optimal value
7. Model comparison — KNN vs. Logistic Regression vs. Decision Tree
8. Evaluation — accuracy, precision, recall, F1-score, confusion matrix, ROC/AUC curve

**Result:** Tuned KNN (k=12) achieved **86.9% accuracy**, outperforming both Logistic
Regression (80.3%) and a Decision Tree (78.7%) on the same test set.

**Files:**
- `heart.csv` — dataset
- `heart_disease_classification.ipynb` — full executed notebook
- `heart_disease_classification.py` — equivalent standalone script
- `requirements.txt` — dependencies

**Key Skills:** Data handling, supervised learning, model training, hyperparameter
tuning, model evaluation, data visualization

**How to run:**
```bash
pip install -r requirements.txt
python heart_disease_classification.py
# or open the notebook:
jupyter notebook heart_disease_classification.ipynb
```

---

## Tech Stack

`Python` · `pandas` · `NumPy` · `scikit-learn` · `matplotlib` · `seaborn` · `Tkinter`

## About Me

DS student building hands-on AI and software projects through the DecodeLabs
internship program, alongside coursework in databases, networking, and applied
programming.

---
