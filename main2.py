import pandas as pd
import numpy as np

exam_data = {
    'name': ['Olivia', 'Liam', 'Sophia', 'Noah', 'Isabella', 'Mason', 'Ava', 'Elijah', 'Mia', 'Lucas'],
    'score': [12.4, np.nan, 20, 15, 12, 15.5, 19, np.nan, 10, 9],
    'attempts': [1, 3, 4, 2, 1, 5, 2, 3, 6, 7],
    'qualify': ['yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print (df)