import pandas as pd
train=pd.read_csv('sentiment.csv', sep='\t')
train.head()
train=train.drop_duplicates(subset=['SentenceId'], keep='first')
train[train['SentenceId']==1]['Phrase'][0]
sol=pd.read_csv('sentiment.csv', sep='\t')
sol=sol.drop_duplicates(subset=['SentenceId'], keep='first')
train=train.drop(['SentenceId'],axis=1)
train.columns=['ID','text','class']
train.head()
sol=sol.drop(['SentenceId'],axis=1)
sol.columns=['ID','text']
sol.head()
def clean_text(text):
    if isinstance(text, str):
        cleaned_text = text.lower()  # Convert to lowercase
        cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # Remove punctuation
        return cleaned_text
    else:
        return str(text)

def create_files(df, folder_path):
    """
    Create files from a dataframe where each row is saved as a text file named after the ID column.
    The text file contains the cleaned value in the text column.
    
    Args:
        df (pandas.DataFrame): A dataframe with columns 'ID', 'text', and 'target'
        folder_path (str): A string indicating the path to the folder where the files will be stored.
        
    Returns:
        None
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    for index, row in df.iterrows():
        ID_value = row['ID']
        text_value = row['text']
        
        cleaned_text = clean_text(text_value)
        
        file_name = os.path.join(folder_path, f"{ID_value}.txt")
        
        with open(file_name, 'w') as f:
            f.write(str(cleaned_text))
            
train['class'].value_counts()
round(train['class'].value_counts()*100/len(train),2)
train['filename']='./data/'+train['ID'].astype('str')+'.txt'
train=train.drop(['ID','text'],axis=1)
train.columns=['label','filename']
train=train.sample(n=len(train))
train.reset_index(inplace=True,drop=True)
train.head()
train.shape,test.shape
import os
newpath = r'./train' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
import shutil, os
#creating subfolders
for c in class_names:
    dest =  r'./test/'+str(c)
    os.makedirs(dest)
    for i in list(test[test['label']==c]['filename']): # Image Id
        move_image_to_cat = shutil.copy(i, dest)
import shutil
shutil.rmtree('./data')
