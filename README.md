# 🧠 Brain Tumor Classification

This repository contains a deep learning-powered web application for classifying brain tumors using MRI images. The system uses **Transfer Learning with VGG16**, modular ML pipelines, and **Flask** for deployment. Project pipelines are managed and version-controlled using **DVC (Data Version Control)**.

## 🚀 Features

- VGG16 Transfer Learning for brain tumor classification
- Modular architecture: ingestion, training, evaluation, prediction
- Flask web interface for real-time image classification
- DVC-integrated data and model versioning
- Conda-based environment setup

---

## 📁 Project Structure

```
├── artifacts/ # Stored artifacts (e.g., trained models)
├── config/ # Configuration files
├── logs/ # Logging info
├── research/ # Notebooks and experiments
├── src/ # Core package source code
├── templates/ # HTML templates for Flask app
├── .dvc/ # DVC configuration
├── app.py # Flask application
├── main.py # Pipeline execution script
├── params.yaml # Training/evaluation parameters
├── dvc.yaml # DVC pipeline file
├── requirement.txt # Required Python packages
├── README.md # Project documentation
└── setup.py # Package setup
```
## 🧪 Setup Instructions

### ✅ Create Conda Environment

```bash
conda create -n tumor-classifier python=3.10 -y
conda activate tumor-classifier
```
### 📦 Install Requirements

```bash
pip install -r requirement.txt
```
### 💾 DVC Setup (Optional but recommended)

```bash
dvc init
dvc repro
```
### 💻 Run the Flask Web App

```bash
python app.py
```
---
## 🖼️ Preview
<img width="947" height="413" alt="image" src="https://github.com/user-attachments/assets/d5b18cd7-9197-4c4e-80ef-ea40c8870401" />
<img width="947" height="411" alt="image" src="https://github.com/user-attachments/assets/49c14922-cd53-4b02-b858-147e6658e982" />
<img width="941" height="380" alt="image" src="https://github.com/user-attachments/assets/8ab2bcb6-eba0-4d5d-8fd7-5d7afc80195f" />
<img width="938" height="331" alt="image" src="https://github.com/user-attachments/assets/b9b588bc-6346-4802-bdd1-2c5141bd06ec" />
<img width="946" height="359" alt="image" src="https://github.com/user-attachments/assets/87e19335-14af-4494-8285-8df9c411a489" />

## 🙋‍♀️ Author
Mamoona Ramzan
(Software Engineering Student at NUST)
