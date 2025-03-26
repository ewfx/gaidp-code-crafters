# Comprehensive Architecture and Solution Documentation for AI-Powered Data Profiling Solution

## Table of Contents

1. Introduction
2. Problem Statement
3. Objectives and Goals
4. System Architecture
5. Solution Components
6. Data Flow and Processing Steps
7. Detailed Module Descriptions
   - Configuration Management
   - Prompt Preparation and Validation Generation
   - Data Preprocessing
   - Anomaly Detection
   - Anomaly Verification
   - Reporting
8. Error Handling and Logging
9. Scalability and Performance Considerations
10. Security and Compliance
11. Conclusion

---

## 1. Introduction

This document provides a comprehensive overview of the architecture and solution design of the AI-powered data profiling solution. The solution is specifically designed for banking regulatory reporting, leveraging Generative AI for validation rule generation, unsupervised machine learning for anomaly detection, and automated report generation to support compliance and operational decision-making.

---

## 2. Problem Statement

In the banking sector, ensuring data quality is critical for regulatory compliance, risk management, fraud detection, and operational efficiency. Manual data profiling methods are time-consuming, prone to errors, and difficult to scale. Existing solutions often lack flexibility, automation, and intelligence to identify anomalies accurately. This project aims to address these challenges through an AI-powered, automated data profiling pipeline.

---

## 3. Objectives and Goals

- Automate the data profiling process using AI and machine learning.
- Generate accurate Python validation code using Generative AI.
- Identify anomalies using unsupervised learning algorithms.
- Provide explainable results and actionable insights.
- Streamline regulatory reporting with minimal human intervention.

---

## 4. System Architecture

### High-Level Overview

- **Input Layer:** CSV data files, configuration files, and prompt instructions.
- **Processing Layer:** Core modules for data preprocessing, validation code generation, anomaly detection, and verification.
- **Output Layer:** CSV reports summarizing anomalies and validation results.
- **User Interface:** Streamlit-based web interface for managing the workflow.

### Architectural Components

1. **Data Input Management**: Handles input data in CSV format.
2. **Configuration Management**: Centralizes settings using a YAML configuration file.
3. **AI-based Validation Generation**: Uses Google Gemini AI for validation code generation.
4. **Data Preprocessing**: Cleans and transforms data for anomaly detection.
5. **Anomaly Detection Engine**: Detects anomalies using DBSCAN clustering.
6. **Anomaly Verification**: Validates detected anomalies against generated rules.
7. **Reporting Module**: Generates a comprehensive regulatory report.

---

## 5. Solution Components

### **5.1 Configuration Management**

- Configuration parameters are stored in a `config.yml` file.
- It includes paths for input/output data, model parameters, and logging settings.
- The `ConfigLoader` class reads and validates configurations at runtime.

### **5.2 Prompt Preparation and Validation Generation**

- Multiple input files (`prompt.txt`, `Instruction.txt`, `column_instructions.txt`) are merged to generate a final prompt.
- The Google Gemini AI uses this prompt to generate executable Python validation code.
- Validation code is stored in `validations.py` for further use.

### **5.3 Data Preprocessing**

- Missing values are handled using imputation strategies.
- Low-variance and single-value columns are removed.
- Categorical columns are encoded using frequency-based encoding.
- Date-time features are transformed into separate components (e.g., Year, Month, Day).

### **5.4 Anomaly Detection**

- DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is applied for anomaly detection.
- Optionally, PCA (Principal Component Analysis) is used for dimensionality reduction to improve clustering efficiency.
- Anomalies are identified based on cluster density and labeled as outliers.

### **5.5 Anomaly Verification**

- Validation rules are applied to detected anomalies.
- The `VerifyAnomalies` class ensures compliance with pre-defined rules.
- Verified anomalies are saved for reporting.

### **5.6 Reporting**

- The `RegulatoryReportingFactory` class generates reports containing detailed insights into anomalies and rule violations.
- Reports are exported as CSV files for regulatory submissions and internal review.

---

## 6. Data Flow and Processing Steps
Input (CSV) → Configuration Management → Prompt Preparation → Validation Code Generation ↓ ↓ Data Preprocessing → Anomaly Detection → Anomaly Verification → Report Generation → Output (CSV)

---

## 7. Detailed Module Descriptions

### **7.1 Configuration Management**

- `ConfigLoader` validates YAML files for correct parameter structure.
- Default values are applied when parameters are missing.
- Error handling ensures invalid configurations are reported.

### **7.2 Prompt Preparation and Validation Generation**

- AI prompt templates are dynamically constructed using financial instructions.
- Google Gemini AI generates optimized Python code for data validation.
- The code is stored in `validations.py` and executed during anomaly verification.

### **7.3 Data Preprocessing**

- Advanced imputation techniques like median or mean replacement are used.
- Feature scaling and normalization ensure better anomaly detection results.
- Dimensionality reduction using PCA is applied when necessary.

### **7.4 Anomaly Detection**

- DBSCAN is chosen for its efficiency in detecting irregular patterns in high-dimensional data.
- Parameters like epsilon and minimum samples are dynamically tuned for optimal detection.

### **7.5 Anomaly Verification**

- Validation rules from `validations.py` are applied to anomalies.
- Logs are generated for failed validations with detailed error messages.

### **7.6 Reporting**

- Reports are generated in CSV format containing anomaly summaries, validation status, and recommendations.
- Additional visualizations like scatter plots are provided for easier interpretation.

---

## 8. Error Handling and Logging

- Python's `logging` module is used to capture system events.
- Errors are logged in a structured format for easy debugging.
- Custom exceptions are implemented for critical modules.

---

## 9. Scalability and Performance Considerations

- The pipeline supports horizontal scaling using parallel processing.
- DBSCAN’s performance is optimized using dimensionality reduction.
- Incremental processing is supported for large datasets.

---

## 10. Security and Compliance

- Data is processed in-memory to minimize data exposure.
- Audit logs are maintained for regulatory compliance.
- Secure APIs are used for AI model interactions.

---

## 11. Conclusion

The AI-powered data profiling solution automates anomaly detection and regulatory reporting with high accuracy. By leveraging Generative AI and unsupervised machine learning, it reduces manual effort, improves data quality, and ensures regulatory compliance efficiently.

