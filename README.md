README FILE

<b> Identifying Antimicrobial Peptides using Protein Features and Logistic Regression </b> 

This code installs the necessary packages and libraries, downloads peptide datasets, removes redundant sequences, calculates amino acid composition (AAC) and dipeptide composition (DPC) protein features, and combines the resulting data frames into a single CSV file. The code also trains a logistic regression model to classify the peptides as either positive or negative based on their protein features, and evaluates the model's performance using the confusion matrix and accuracy score.

To use the code, run the installation commands to install miniconda, Pfeature, and CD-HIT. Then, run the commands to download and process the peptide datasets. 
To calculate protein features, use the calc_aac and calc_dpc functions and pass in the file path for the FASTA file. 
To combine the protein feature data frames and save the resulting data frame to a CSV file, use the calc_features function and pass in the file paths for the positive and negative class FASTA files and the feature calculation function. 
Finally, to train and evaluate the machine learning model, run the code to split the data into training and testing sets, standardize the data, fit the model to the training data, make predictions on the test data, and evaluate the model's performance. 


NB: If you are considering publishing a paper based on this type of project, it is important to acknowledge the original paper that served as inspiration. Be sure to include a citation for the original paper in your own work:

https://www.cell.com/molecular-therapy-family/nucleic-acids/fulltext/S2162-2531(20)30132-3?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS2162253120301323%3Fshowall%3Dtrue

This revised version provides credit to the original paper and clearly indicates that the new work is drawing inspiration from it, rather than simply copying it. It is always important to properly cite and give credit to the sources that have influenced your own research or writing.  
