# DNA Sequence Classifier

## Overview
This project aims to classify DNA sequences into species (Human and Dog) using k-mer feature extraction and machine learning models such as LightGBM and Random Forest.

## Key Components
- **Data Preparation**: Extracts fragments from chromosome 1 of human and dog genomes.
- **Feature Extraction**: Uses k-mer vectors (e.g., k=5) to represent sequences, including N-ratio.
- **Modeling**: Trains LightGBM and Random Forest classifiers with class balancing.
- **Evaluation**: Measures accuracy, AUC, and other metrics on test data.

## Requirements
- Python libraries: pandas, numpy, scikit-learn, lightgbm, matplotlib, seaborn
- Custom modules: extract_chr, prepare_fragments

## Usage
1. Run the Jupyter notebook `dna_classifier.ipynb`.
2. Adjust parameters like k-mer size and model hyperparameters as needed.
3. Evaluate results using confusion matrix, ROC curve, and classification reports.

## Results
- Achieves high accuracy (e.g., ~79%) with optimized thresholds.
- Best performance with k=5 and balanced class weights.