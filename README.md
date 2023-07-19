# SMS Spam Classifier

![Python](https://img.shields.io/badge/python-v3.9-blue)
![Streamlit](https://img.shields.io/badge/streamlit-v0.87-orange)
![GitHub](https://img.shields.io/github/license/yourusername/sms-spam-classifier)

This repository contains a SMS spam classifier project built using Natural Language Processing (NLP) and Streamlit. The goal of this project is to develop a machine learning model that can accurately classify SMS messages as either spam or non-spam (ham). The project is hosted using Streamlit, allowing users to interact with the model through a user-friendly web interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Evaluation](#evaluation)
- [Contribution](#contribution)
- [License](#license)

## Installation

To run the SMS spam classifier locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/sms-spam-classifier.git
cd sms-spam-classifier
```

2. Install the required dependencies. It is recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

## Usage

Once you have installed the dependencies, you can run the SMS spam classifier using Streamlit:

```bash
streamlit run app.py
```

This command will launch a local server, and you can access the web application by visiting `http://localhost:8501` in your web browser.

## Dataset

The dataset used to train and evaluate the SMS spam classifier is the [SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection). It contains a collection of SMS messages labeled as spam and non-spam (ham).
The dataset is also available on Kaggle !

The dataset is preprocessed before training the model to convert text messages into numerical features suitable for machine learning algorithms.

## Model

The SMS spam classifier uses a machine learning model based on NLP techniques to classify messages as spam or ham. The model is trained on the preprocessed dataset using scikit-learn and other relevant libraries.

The current implementation uses [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to convert the text messages into numerical features and [Multinomial Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) as the classification algorithm.

## Evaluation

The performance of the SMS spam classifier is evaluated using metrics like accuracy, precision, recall, and F1-score on a separate test set. The model's hyperparameters are tuned to achieve the best possible results.

## Contribution

Contributions to the SMS spam classifier project are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request. Please ensure that your contributions align with the project's coding standards and follow the guidelines specified in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to use and modify this template for your SMS spam classifier project! If you have any questions or need assistance, please don't hesitate to contact me.

Happy coding! 🚀
