import pandas as pd
import os

def format_author(name):
    """Format 'First Last' -> 'LAST, FIRST' and handle blanks."""
    if not isinstance(name, str) or not name.strip():
        return "UNKNOWN AUTHOR"
    
    parts = name.strip().split()
    if len(parts) == 1:
        return parts[0].upper()
    else:
        last = parts[-1].upper()
        first = " ".join(parts[:-1]).upper()
        return f"{last}, {first}"

def process_csv(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    try:

        df = pd.read_csv(file_path)
        
        if 'Author' not in df.columns:
            print("Error: 'Author' column not found in CSV.")
            return
        

        df['auth_cap'] = df['Author'].apply(format_author)
        

        df.to_csv(file_path, index=False)
        print(f"✅ Updated file saved: {file_path}")
    
    except Exception as e:
        print(f"Error processing file: {e}")

process_csv("files\merged_2.csv")
