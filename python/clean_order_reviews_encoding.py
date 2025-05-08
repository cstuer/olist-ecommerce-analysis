import pandas as pd
import re

# 1. Load your messy CSV
df = pd.read_csv(r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_order_reviews_dataset.csv", encoding='utf-8', on_bad_lines='skip')

# 2. Optional: fix broken encoding (only if needed)
def safe_fix(text):
    try:
        if isinstance(text, str):
            return text.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text
    return text

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(safe_fix)

# 3. Optional: remove hidden non-printable characters
def remove_hidden(text):
    if isinstance(text, str):
        return re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    return text

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(remove_hidden)

# 4. Remove duplicates based on primary key (review_id)
df = df.drop_duplicates(subset='review_id', keep='first')

# 5. Save the clean file
df.to_csv(r"C:\Users\Stuer\OneDrive\Professional\SQL\Brazilian-ecommerce-project\olist_order_reviews_clean_final.csv", index=False, encoding='utf-8')

print(" Complete. File cleaned, duplicates removed, and saved as 'olist_order_reviews_clean_final.csv'.")
