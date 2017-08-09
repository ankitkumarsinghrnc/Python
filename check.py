import pandas as pd
import os


test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'C:\\Users\\Ankit Kumar\\Desktop\\training.tsv'), header=0, delimiter="\t", \
                   quoting=3 )
print(test)