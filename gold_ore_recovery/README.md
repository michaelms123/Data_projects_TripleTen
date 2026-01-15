# Gold Recovery Prediction from Ore Processing: 
**Link to full repository with all datasets and .venv included: https://github.com/michaelms123/gold-ore-recovery**

**Link to Jupyter Notebook: https://github.com/michaelms123/gold-ore-recovery/blob/main/gold_ore_pj.ipynb**
## Project Overview: ##
This project focuses on predicting gold recovery rates at different stages of an industrial gold extraction process using machine learning.
The goal is to model and predict:
- Rougher concentrate recovery
- Final concentrate recovery
Accurate recovery predictions help optimize production efficiency and reduce financial losses in mining operations. The project follows a real-world industrial workflow, where not all features are available at prediction time, and model evaluation requires a custom metric (sMAPE).

## Technological Process Description: ##
Gold extraction from ore consists of several key stages:
**1. Flotation (Rougher Process)**
- Crushed ore is mixed with water and reagents
- Air bubbles bind to gold particles
- Produces:
  - Rougher gold concentrate
  - Rougher tails (waste material)
- The stability of this process depends on pulp chemistry, particle size, air flow, and reagent dosage.

**2. Purification (Cleaner Process)**
- The rougher concentrate undergoes:
  - Primary cleaning
  - Secondary cleaning
- Final outputs:
  - Final gold concentrate
  - Final tails

## Dataset Description: ##
- ***gold_recovery_train.csv***:Training dataset (includes targets)
- ***gold_recovery_test.csv***:	Test dataset (no targets, missing late-stage features)
- ***gold_recovery_full.csv***:	Full raw dataset (train + test, all features)
- Index:
  - Date and time of measurement
  - Neighboring timestamps often have similar values

## Feature Naming Convention: ##
- Features follow this structure:
  
  [stage].[parameter_type].[parameter_name]

- Stages:
  - ***rougher*** – flotation
  - ***primary_cleaner*** – first purification
  - ***secondary_cleaner*** – second purification
  - ***final*** – final characteristics
    
- Parameter Types
  - ***input*** – raw materials
  - ***output*** – process results
  - ***state*** – process conditions
  - ***calculation*** – derived values
  - 
- Example:  **rougher.input.feed**

## Recovery Calculation: ##
Gold recovery is calculated using the formula:

	 Recovery = C x (F-T) / F x (C - T) 

Where:
- **C** — gold concentration in the concentrate
- **F** — gold concentration in the feed
- **T** — gold concentration in the tails

- This formula is used to:
  - Validate target correctness
  - Understand the physical meaning behind predictions

## Evaluation Metric: sMAPE:
- This project uses symmetric Mean Absolute Percentage Error (sMAPE):
  - Scale-independent
  - Penalizes over- and under-predictions equally
  - Suitable for industrial processes with varying magnitudes
- Final Score:
  - *Final sMAPE = 0.25 x sMAPE(rougher) + 0.75 x sMAPE(final)*

## Project Workflow: ##
**1) Data Preparation:**
- Loaded and inspected all datasets
- Verified recovery calculation correctness (MAE ≈ 0)
- Identified features unavailable in the test set
- Handled:
  - Missing values
  - Time-based alignment
  - Feature selection to prevent data leakage

**2) Exploratory Data Analysis:**
- Tracked Au, Ag, Pb concentration changes across stages
- Compared feed particle size distributions (train vs test)
- Analyzed total concentration anomalies
- Removed physically impossible values from both samples

**3) Modeling:**
- Implemented a custom sMAPE function
- Trained and evaluated multiple models using cross-validation
- Selected the best-performing model
- Evaluated final performance on the test dataset
- Cross-validation was used to ensure robust and unbiased evaluation.

## Models Used: ##
- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor

## Key Findings: ##
- Gold concentration increases consistently through purification stages
- Particle size distributions between train and test sets are similar, ensuring valid evaluation
- Removing total concentration anomalies improves model stability
- The final model achieves strong predictive performance under sMAPE
