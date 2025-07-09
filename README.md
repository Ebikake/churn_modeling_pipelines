````markdown

\# Churn Modeling Pipelines



A modular and production-ready Python package for end-to-end customer churn prediction.  

Built with best practices in mind, it enables streamlined preprocessing, feature engineering, model building, evaluation, and business insight generation.



---



\## 📦 Features



This package includes six powerful modules:



| Module | Description |

|--------|-------------|

| `ChurnPreprocessor` | Cleans, encodes, and scales your dataset for churn modeling |

| `CustomerJourneyClassifier` | Segments customers into journey stages and computes churn risk per stage |

| `ChurnModelBuilder` | Builds seven churn models with multiple hyperparameter variants |

| `ChurnEvaluator` | Evaluates each model variant using Accuracy, Precision, Recall, F1-Score, and Cost |

| `ChurnPlotter` | Plots confusion matrices, ROC curves, and radial performance charts |

| `ModelComparator` | Extracts best model variants and ranks them using composite scores |



---



\## 📊 Supported Models



\- Logistic Regression  

\- Decision Tree  

\- K-Nearest Neighbors  

\- Naive Bayes  

\- Support Vector Machine  

\- Random Forest  

\- XGBoost



Each model supports up to 5 hyperparameter variants for optimal performance.



---



\## 🧠 Business-Aware Evaluation



Includes \*\*cost-sensitive evaluation\*\* of false positives and false negatives, ensuring models are selected not just for accuracy but for \*\*business impact\*\*.



---



\## 🔧 Installation



Install from GitHub Releases:



```bash

pip install https://github.com/Ebikake/churn\_modeling\_pipelines/releases/download/v0.1.0/churn\_modeling\_pipelines-0.1.0-py3-none-any.whl

````



---



\## 🧪 How to Use



```python

from churn\_modeling\_pipelines import (

&nbsp;   ChurnPreprocessor,

&nbsp;   CustomerJourneyClassifier,

&nbsp;   ChurnModelBuilder,

&nbsp;   ChurnEvaluator,

&nbsp;   ChurnPlotter,

&nbsp;   ModelComparator

)

```



Refer to `example\_usage.ipynb` for a full demonstration in Google Colab.



---



\## 📁 Folder Structure



```

churn\_modeling\_pipelines/

├── churn\_modeling\_pipelines/

│   ├── \_\_init\_\_.py

│   ├── ChurnPreprocessor.py

│   ├── CustomerJourneyClassifier.py

│   ├── ChurnModelBuilder.py

│   ├── ChurnEvaluator.py

│   ├── ChurnPlotter.py

│   └── ModelComparator.py

├── dist/

│   └── churn\_modeling\_pipelines-0.1.0-py3-none-any.whl

├── example\_usage.ipynb

├── setup.py

├── README.md

└── LICENSE

```



---



\## 📄 License



This project is licensed under the MIT License – see the \[LICENSE](LICENSE) file for details.



---



\## 🙌 Author



Developed by \*\*John Ebikake\*\*

GitHub: \[@Ebikake](https://github.com/Ebikake)







