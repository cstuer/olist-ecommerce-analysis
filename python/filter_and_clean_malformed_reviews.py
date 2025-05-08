import pandas as pd
import re

# Step 1: Load your messy CSV
with open(r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_order_reviews_clean_final.csv", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Step 2: Drop lines that have wrong number of commas (should be exactly 6 commas for 7 columns)
good_lines = [line for line in lines if line.count(',') == 6]

# Step 3: Save temporarily cleaned file
temp_file_path = r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_temp_clean.csv"
with open(temp_file_path, 'w', encoding='utf-8') as file:
    file.writelines(good_lines)

# Step 4: Now load into pandas
df = pd.read_csv(temp_file_path, encoding='utf-8')

# Step 5: Fix broken encoding (if any)
def safe_fix(text):
    try:
        if isinstance(text, str):
            return text.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text
    return text

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(safe_fix)

# Step 6: Remove hidden non-printable characters
def remove_hidden(text):
    if isinstance(text, str):
        return re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    return text

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(remove_hidden)

# Step 7: Drop duplicate review_ids
df = df.drop_duplicates(subset='review_id', keep='first')

# Step 8: Save final clean file
final_path = r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_order_reviews_ready.csv"
df.to_csv(final_path, index=False, encoding='utf-8')

print("Cleaning done. Final clean file saved as 'olist_order_reviews_ready.csv'. Ready for PostgreSQL import.")
