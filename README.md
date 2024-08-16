# Heart Disease Prediction Using Enhanced Whale Optimization Algorithm (EWOA)

## Project Overview

This project aims to predict heart disease risk using an advanced feature selection method, the Enhanced Whale Optimization Algorithm (EWOA), combined with various machine learning models. The project seeks to improve the accuracy and efficiency of heart disease prediction models by selecting the most relevant features and applying state-of-the-art machine learning techniques.

## Problem Statement

Heart disease remains the leading cause of death globally, accounting for over 12 million deaths annually. Early and accurate prediction of heart disease is crucial for timely intervention and treatment. The existing methods for heart disease prediction involve several machine learning techniques, but there is a need for more efficient and accurate models that can handle large and complex datasets.

## Existing Solutions

Current heart disease prediction models use machine learning algorithms such as:
- Support Vector Machine (SVM)
- Random Forest
- Neural Networks
- Logistic Regression

These models are evaluated using metrics like accuracy and precision. Feature selection techniques, including Enhanced Whale Optimization Algorithm (EWOA) and Genetic Algorithms (GA), play a crucial role in enhancing model performance. Meta-heuristic approaches like FSWOA help reduce dataset dimensions while maintaining accuracy.

## Dataset Description

The dataset used in this project is derived from the Framingham Heart Study, available on Kaggle. It includes over 4000 records with 15 attributes, covering demographic, behavioral, medical history, and current medical condition variables. The target variable is the 10-year risk of coronary heart disease (CHD), which is binary (1 = Yes, 0 = No).

### Key Features:
- **Demographic**: Sex, Age
- **Behavioral**: Current Smoker, Cigs Per Day
- **Medical History**: BP Meds, Prevalent Stroke, Prevalent Hyp, Diabetes
- **Current Medical**: Tot Chol, Sys BP, Dia BP, BMI, Heart Rate, Glucose

## Proposed Model and Methodology

### Algorithms Used:
- **Decision Tree Classifier**
- **Random Forest Classifier**
- **AdaBoost Classifier**
- **Gradient Boosting Classifier**
- **LightGBM Model**

### Feature Selection:
The Enhanced Whale Optimization Algorithm (EWOA) is used to select the most relevant features, which are then used to train the models. EWOA optimizes the feature selection process by placing significant features at the top of a multi-level tree structure and utilizing entropy to calculate their importance.

### Model Training and Evaluation:
- The selected features are used to train various machine learning models.
- The models are evaluated based on metrics such as accuracy, precision, and F1 score.
- Comparative analysis is conducted to determine the best-performing model.

## Simulation Results and Comparison

The results indicate that the models with optimized feature selection perform better in terms of accuracy and computational efficiency. The use of EWOA in feature selection significantly improves the model's ability to predict heart disease.

## Potential Applications

- **Early Detection**: Identifying patients at risk of heart disease for timely intervention.
- **Healthcare Integration**: Assisting healthcare professionals in diagnosing and treating heart disease more effectively.

## Pros and Cons

### Pros:
- Improved feature selection leads to higher model performance.
- Increased accuracy compared to standard techniques.

### Cons:
- High computational cost due to the complex optimization process.
- Handling imbalanced datasets remains a challenge.

## References

1. Heart Disease Pred - Logit Lasso DecisionTree (Kaggle)
2. [Electronic Resources - IEEE](https://ieeexplore-ieee-org.libproxy.library.unt.edu/stamp/stamp.jsp?tp=&arnumber=10428617)
3. [Streamlit Documentation](https://docs.streamlit.io/)
4. [Scikit-Learn User Guide](https://scikit-learn.org/stable/user_guide.html)

