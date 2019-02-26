The folder consists of the following files:
There are 3 .py files
- Dataset used: attacks_normal.csv (obtained by selecting a total of 1000 attack and normal scenario samples from the dataset prepared by MIT Lincoln Lab. (https://www.ll.mit.edu/r-d/datasets/1998-darpa-intrusion-detection-evaluation-dataset)
- combine.py : used to generate dataset from the set of datasets obtained form MIT Lincoln Lab. Please do not run this program. Added for demonstration only.
- attacks_normal.csv: csv file generated using combine.py. Make sure this csv file is in the same folder as -classification.py and anomaly.py
- classification.py : misuse detection system. No additional parameters required to run
- anomaly.py : anomaly detection system. No additional parameters required to run
- mlp_anomaly.py - anomaly IDS using multi layer perceptron of sklearn
- mlp_classification.py - misuse IDS for all attack types/ normal using multi layer perceptron of sklearn
the below 5 are for detection of respective types of attacks: Back, BufferOverflow, FTP, GuessPassword, IMap
