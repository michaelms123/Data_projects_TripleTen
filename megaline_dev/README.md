# Megaline User's Plan Probability #
Megaline (mobile carrier) want's to better understand subscriber behaviour/recommend the most suitable plan: Smart/Ultra

In this project develop a **classification model** to predict subsriber's plan based on monthly behaviour. Goal is to achieve accuracy above 0.75 while also evaluating metrics like F1 score and ROC-AUC to ensure reliable predictions:

## Dataset: ##
- The dataset is included in the repository. 'users_behavior'
- Description: each row represents a subscriber's monthly behaviour, features include:
    'calls': no. of calls
    'minutes': total call duration
    'messages': no. of text messages
    'mb_used': internet usage (MB)
    'is_ultra': target (plan for the month); 1 = Ultra, 0 = Smart

## Project Steps: ##
1) **Data Exploration/Preprocessing:**
   - Checked missing/duplicate/anomalous values
   - Confirmed data types, value ranges and class imbalance
2) **Data Splitting:**
   - Stratified split to maintain class balance:
     - Training set: 60%
     - Validation set: 20%
     - Test set: 20%
3) **Model Training/Testing:**
   - Tested multiple classifiers (DecisionTree, RandomForest, LogisticRegression)
   - Tested against a dummy classifier for a sanity check.
   - Final model: RandomForest (best performing across all metrics in particular accuracy (key metric) and ROC-AUC (how well model ranks positive instances above negative ones)
4) **Evaluation:**
   - Metrics used for training, validation, test sets:
     - Accuracy (key metric)
     - F1 score
     - ROC-AUC

## Final Recommended Model Results: ##
- **Accuracy:** 0.80 
- **F1 score:** 0.64
- **ROC-AUC:** 0.80


   
