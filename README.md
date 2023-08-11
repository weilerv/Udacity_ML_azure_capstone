# Capstone Project - Azure Machine Learning Engineer nanodegree

The project's goal was to train different models in Azure with AutoML and Hyperdrive, then chose and deploy the best performing one as a web service and test the endpoints to predict if someone has diabetes or not based on their gender, age, bmi, smoking habits, etc.


## Project Set Up and Installation
Diabetes dataset from Kaggle was used through Kaggle API so extra code should be run from terminal to access data:

pip install kaggle

export KAGGLE_USERNAME="weilerv"
export KAGGLE_KEY="d35c74c3259b8916fdb3ad6c9d7307c0"

kaggle datasets download -d sudheerp2147234/salary-dataset-based-on-country-and-race

## Dataset

### Overview
Diabetes dataset from (Kaggle)[https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset] was used for the project, 

### Task
It is a binary classification problem deciding if somebody has cancer or not. 
Features:
* gender
* age
* hypertension
* heart_disease
* smoking_history
* bmi
* HbA1c_level
* blood_glucose_level


### Access
Data was downloaded (as a zip file) in the current working directory onto my Azure workspace and extracted through code in my notebook
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/58d4fa42-4c65-49d8-a754-981875f825f5)

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/c5d05553-f6aa-4d32-adee-38bc444b87d1)
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/8b1c1eab-3404-442f-b4b8-94b3c460b3fa)
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/82193c77-7f1f-4997-86e1-7a9f865f4fea)


    "class_name": "XGBoostClassifier",
    "module": "automl.client.core.common.model_wrappers",
    "param_args": [],
    "param_kwargs": {
        "booster": "gbtree",
        "colsample_bytree": 0.5,
        "eta": 0.2,
        "gamma": 0,
        "max_depth": 7,
        "max_leaves": 7,
        "n_estimators": 25,
        "objective": "reg:logistic",
        "reg_alpha": 0,
        "reg_lambda": 0.20833333333333334,
        "subsample": 1,
        "tree_method": "auto"
    },
    "prepared_kwargs": {},
    "spec_class": "sklearn"
}

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/5c476684-1642-45dd-9273-f160bf44f9dc)
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/07d24c81-5d10-4bf2-844f-b32bf482f765)
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/daf75847-ebae-4273-98c6-0ea270a667dc)




## Hyperparameter Tuning
Since our task is a classification, logistic regression model was used since it's relatively not complex but efficient. 
For hyperparameters the following inverse regulation strength and maximum number of iterations was used:
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/b8751370-98c3-4c1c-886f-8f751679fe8e)

For early termination policy the Bandit policy was used:
![image](https://github.com/weilerv/Udacity_ML_azure_capstone/assets/37341293/48797ea9-99eb-4fd0-a5d3-e48f4daf4fda)


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

#### Improvement possibilities:
We could run the experiment longer and with more parameter options or we could try other models.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
