# Multimodal Real Estate Valuation using Satellite Imagery

This project implements a **Multimodal Deep Learning pipeline** to predict residential property values in King County, WA. By fusing traditional tabular data with high-resolution satellite imagery, the model captures geographic and environmental context that standard numerical datasets miss.

## 🚀 Project Overview
Traditional valuation relies on features like square footage and bedroom counts. This system adds a **Vision Branch** to "see" the property's surroundings (neighborhood density, greenery, and infrastructure), combining it with a **Tabular Branch** via a Late Fusion architecture to produce a highly accurate market appraisal.

## 📂 Repository Structure
* **`24123045_report.pdf`**: Comprehensive technical report detailing the EDA, Methodology, and Grad-CAM analysis.
* **`24123045_final.csv`**: Final price predictions for the test dataset.
* **`notebooks/`**: 
    - `preprocessing.ipynb`: Data cleaning, log-transformation, and geospatial EDA.
    - `model_training.ipynb`: Neural network architecture, training loops, and interpretability visualizations.
* **`src/`**: Contains `data_fetcher.py` used to programmatically download satellite images.

## 🧠 Model Architecture
* **Vision Branch:** Pre-trained **ResNet18** (CNN) used as a visual feature extractor.
* **Tabular Branch:** Multi-Layer Perceptron (MLP) for processing standardized house features.
* **Fusion:** A Late Fusion layer that concatenates visual and numerical embeddings.

## 📊 Key Results
* **Optimal Performance:** Achieved a validation loss of **0.0686** at Epoch 3.
* **Explainability:** Grad-CAM visualizations confirm the model focuses on structural footprints and plot boundaries.
* **Spatial Insight:** Geospatial mapping identifies high-value clusters in Seattle and Bellevue/Redmond.

## 🛠️ Tech Stack
* **Framework:** PyTorch
* **Computer Vision:** torchvision (ResNet18), Grad-CAM
* **Hardware:** Accelerated training on **Apple Silicon (MPS)**
