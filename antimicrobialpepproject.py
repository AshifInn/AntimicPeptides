"""
AntimicrobialPepProject.ipynb

<h1> "Protein Feature Calculation and Machine Learning Classification of Peptides" </h1>
<h2> Protein Feature Calculation and Machine Learning </h2>

This code installs the required packages and libraries, downloads peptide datasets, removes redundant sequences, calculates different protein features, and trains a machine learning model to classify the peptides as either positive or negative.

**Installation**
To install the necessary packages and libraries, run the following commands:

**Pfeature Installation**
This script also downloads and installs the Pfeature library, which provides various features for protein sequences. To install Pfeature, simply run the script provided. This will download the Pfeature ZIP file, unzip it, navigate to the Pfeature directory, and run the setup script. After running the script, Pfeature will be installed on your system and can be imported and used in your Python scripts.
"""

# Commented out IPython magic to ensure Python compatibility.
# Install miniconda
!wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh
!chmod +x Miniconda3-py37_4.8.2-Linux-x86_64.sh
!bash ./Miniconda3-py37_4.8.2-Linux-x86_64.sh -b -f -p /usr/local
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')

# Download and install Pfeature
!wget https://github.com/raghavagps/Pfeature/raw/master/PyLib/Pfeature.zip
!unzip Pfeature.zip
# %cd Pfeature
!python setup.py install

# Install CD-HIT
!conda install -c bioconda cd-hit -y

"""**Usage**
To download the peptide datasets and remove redundant sequences, run the following commands:
"""

# Download peptide datasets
!wget https://raw.githubusercontent.com/AshifInn/AntimicPeptides/main/train_po.fasta
!wget https://raw.githubusercontent.com/AshifInn/AntimicPeptides/main/train_ne.fasta
!cat train_ne.fasta 

# Remove redundant sequences using CD-HIT
!cd-hit -i train_po.fasta -o train_po_cdhit.txt -c 0.99
!cd-hit -i train_ne.fasta -o train_ne_cdhit.txt -c 0.99
!ls -l
!grep ">" train_po_cdhit.txt | wc -l
!grep ">" train_po.fasta | wc -l
!grep ">" train_ne.fasta | wc -l
!grep ">" train_ne_cdhit.txt | wc -l

"""To calculate protein features, use the following functions:"""

# Define functions for calculating different features
import pandas as pd

# Amino acid composition (AAC)
from Pfeature.pfeature import aac_wp

def calc_aac(input_file):
  # Create output file name
  output_file = input_file.rstrip('txt') + 'aac.csv'
  # Calculate AAC feature and save to output file
  aac_wp(input_file, output_file)
  # Load output file as pandas dataframe
  df = pd.read_csv(output_file)
  return df

# Dipeptide composition (DPC)
from Pfeature.pfeature import dpc_wp

def calc_dpc(input_file):
  # Create output file name
  output_file = input_file.rstrip('txt') + 'dpc.csv'
  # Calculate DPC feature and save to output file
  dpc_wp(input_file, output_file, 1)
  # Load output file as pandas dataframe
  df = pd.read_csv(output_file)
  return df

# Calculate feature for both positive and negative classes, combine the two classes, and merge with class labels
pos_file = 'train_po_cdhit.txt'
neg_file = 'train_ne_cdhit.txt'

"""**Feature Calculation and Data Preprocessing**
This script contains a function calc_features that calculates features for positive and negative classes and combines them with class labels to create a Pandas dataframe. The function takes in three arguments:

1. pos_file: file containing the positive class data
2. neg_file: file containing the negative class data
3. feature_calc_func: function used to calculate the features for each class

The function returns a Pandas dataframe with the combined features and class labels. The script also demonstrates how to use calc_features to calculate the AAC and DPC features for a given dataset. Finally, it performs some data preprocessing on the AAC feature dataframe and assigns the features to X and the labels to y. 
"""

def calc_features(pos_file, neg_file, feature_calc_func):
  # Calculate feature for positive and negative classes
  pos_feature = feature_calc_func(pos_file)
  neg_feature = feature_calc_func(neg_file)
  # Create class labels
  pos_class = pd.Series(['positive' for i in range(len(pos_feature))])
  neg_class = pd.Series(['negative' for i in range(len(neg_feature))])
  # Combine positive and negative classes
  po_ne_class = pd.concat([pos_class, neg_class], axis=0)
  po_ne_class.name = 'class'
  po_ne_feature = pd.concat([pos_feature, neg_feature], axis=0)
  # Combine feature and class
  df = pd.concat([po_ne_feature, po_ne_class], axis=1)
  return df

# Calculate AAC feature
aac_feature = calc_features(pos_file, neg_file, calc_aac)


# Calculate DPC feature
dpc_feature = calc_features(pos_file, neg_file, calc_dpc)

# Data pre-processing
aac_feature
# Assign X and y
X = aac_feature.iloc[:, :-1]
y = aac_feature.iloc[:, -1]

"""**Machine Learning**
To train a machine learning model, import the desired model from the sklearn library and call the fit function on the training data. In this example, we use a logistic regression model from the sklearn.linear_model module.
"""

# Split dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Standardize data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Train model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=1)
classifier.fit(X_train_std, y_train)

# Make predictions
y_pred = classifier.predict(X_test_std)

"""**To evaluate the model's performance,** import the desired evaluation metric(s) from the sklearn.metrics module and apply them to the true test labels and the predicted labels. In this example, we use the confusion_matrix and accuracy_score functions."""

# Evaluate model performance
from sklearn.metrics import confusion_matrix, accuracy_score
confusion_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(confusion_matrix)
print(accuracy)

confusion_matrix

accuracy
