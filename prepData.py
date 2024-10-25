#student responses need to placed inside of a list variable
# Assuming the Excel file contains your table in the first sheet

# Replace 'your_excel_file.xlsx' with the actual file path
file_path = 'your_excel_file.xlsx'

import pandas as pd
def load_excel(file_path): 
    df = pd.read_excel(file_path)
    return df
def table_to_list(df):
    qa_list = []
    for index, row in df.iterrows():
        n = row[0]
        question = row[1]
        answer = row[2]
        qa_string = f"n: {n}, Question: {question} Answer: {answer}"
        qa_list.append(qa_string)
    return qa_list
if __name__ == "__main__":
    df = load_excel(file_path)
    result_list = table_to_list(df)
    if result_list:
        print(result_list[0])
    else:
        print("No data found.")
