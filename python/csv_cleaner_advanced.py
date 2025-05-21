import pandas as pd
import re

# Load messy CSV
with open(r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_order_reviews_clean_final.csv", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Drop lines that have wrong number of commas
good_lines = [line for line in lines if line.count(',') == 6]

# Save temporarily cleaned file
temp_file_path = r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_temp_clean.csv"
with open(temp_file_path, 'w', encoding='utf-8') as file:
    file.writelines(good_lines)

# Load into pandas
df = pd.read_csv(temp_file_path, encoding='utf-8')

# Fix any broken encoding
def safe_fix(text):
    try:
        if isinstance(text, str):
            return text.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text
    return text

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(safe_fix)

# Remove hidden non-printable characters
def remove_hidden(text):
    if isinstance(text, str):
        return re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    return text

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(remove_hidden)

# Drop duplicate review_ids
df = df.drop_duplicates(subset='review_id', keep='first')

# Save final clean file
final_path = r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_order_reviews_ready.csv"
df.to_csv(final_path, index=False, encoding='utf-8')

print("Cleaning done. Final clean file saved as 'olist_order_reviews_ready.csv'. Ready for PostgreSQL import.")
