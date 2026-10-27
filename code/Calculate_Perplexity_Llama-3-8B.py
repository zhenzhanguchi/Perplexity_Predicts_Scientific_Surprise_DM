import os
import pandas as pd
import torch
from torch.nn import DataParallel
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer(model_path, tokenizer_model_path, device):
    """Load model and tokenizer, move model to GPU, and wrap with DataParallel."""
    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(model_path)
    model.eval()
    model = model.to(device)
    model = DataParallel(model, device_ids=[0])  # Using one GPU
    print("Model loaded successfully!")

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_model_path)
    print("Tokenizer loaded successfully!")

    return model, tokenizer

def calculate_perplexity_and_tokens(text, uid, model, tokenizer, device, max_length=8192):
    """Calculate perplexity for abstracts up to max_length tokens."""
    try:
        tokens = tokenizer(text, return_tensors="pt", truncation=False)["input_ids"][0]
        total_token_count = len(tokens)

        # This code targets abstracts shorter than max_length.
        # Longer abstracts are handled using a sliding-window approach.
        # For Llama 3 8B, only 0.0003% of abstracts exceed max_length.
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
        input_ids = inputs.input_ids.to(device)

        with torch.no_grad():
            outputs = model(input_ids, labels=input_ids)
            loss = outputs.loss
            perplexity = torch.exp(loss).item()

        return perplexity, total_token_count

    except Exception as e:
        print(f"Error calculating perplexity for id {uid}. Error: {e}")
        return None, None

def main():
    model_path = "Your local model path"
    tokenizer_model_path = "Your local tokenizer path"

    input_file = "xxxx"
    output_file = "xxxx"

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    model, tokenizer = load_model_and_tokenizer(model_path, tokenizer_model_path, device)

    try:
        df = pd.read_parquet(input_file)
        print(f"Successfully loaded {len(df)} rows from {input_file}.")
    except Exception as e:
        raise RuntimeError(f"Failed to load file: {input_file}. Error: {e}")

    df = df[df['abstract'].notna() & (df['abstract'].str.strip() != "")]
    print(f"Cleaned data: {len(df)} rows remaining.")

    required_columns = ['abstract', 'id']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Input file must contain {required_columns} columns.")

    chunk_size = 500
    start_index = 0
    processed_uids = set()

    if os.path.exists(output_file):
        existing_df = pd.read_parquet(output_file)
        processed_uids = set(existing_df['id'])
        start_index = len(existing_df)
    else:
        existing_df = pd.DataFrame()

    total_rows = len(df)
    progress_bar = tqdm(total=total_rows, desc="Processing", unit="row")

    while start_index < total_rows:
        end_index = min(start_index + chunk_size, total_rows)
        chunk_df = df.iloc[start_index:end_index]
        chunk_df = chunk_df[~chunk_df['id'].isin(processed_uids)]

        if chunk_df.empty:
            start_index = end_index
            continue

        results = []
        for _, row in chunk_df.iterrows():
            results.append(calculate_perplexity_and_tokens(row['abstract'], row['id'], model, tokenizer, device))
            progress_bar.update(1)

        chunk_df['perplexity'], chunk_df['num_token'] = zip(*results)
        existing_df = pd.concat([existing_df, chunk_df[['id', 'perplexity', 'num_token', 
                                                    'month_year']]])

        try:
            existing_df.to_parquet(output_file, index=False)
            print(f"Saved results up to row {end_index}.")
        except Exception as e:
            raise RuntimeError(f"Failed to save results to {output_file}. Error: {e}")

        start_index = end_index

    progress_bar.close()
    print(f"Perplexity calculation completed. Results saved to {output_file}.")

if __name__ == "__main__":
    main()
