import pickle
import pandas as pd
import json
import numpy as np
import math

def default_converter(o):
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.int_, np.intc, np.intp, np.int8,
                      np.int16, np.int32, np.int64, np.uint8,
                      np.uint16, np.uint32, np.uint64)):
        return int(o)
    if isinstance(o, (np.float_, np.float16, np.float32, np.float64)):
        if np.isnan(o) or math.isnan(o):
            return None
        return float(o)
    if isinstance(o, (np.complex_, np.complex64, np.complex128)):
        return {'real': o.real, 'imag': o.imag}
    if isinstance(o, (np.bool_)):
        return bool(o)
    if isinstance(o, np.void): 
        return None
    if pd.isna(o):
        return None
    
    # fallback
    return str(o)

def clean_dict(d):
    cleaned = {}
    for k, v in d.items():
        if pd.isna(v):
            cleaned[k] = None
        else:
            cleaned[k] = v
    return cleaned

def main():
    input_file = './data/CommunityFitNet_updated.pickle'
    output_file = './data/CommunityFitNet_updated.json'
    
    print(f"Loading {input_file} ...")
    with open(input_file, 'rb') as infile:
        df = pickle.load(infile)
        
    print("Converting DataFrame to list of dicts...")
    # Replace pd.NA and np.nan in the DataFrame before conversion to avoid serialization issues where possible
    df = df.where(pd.notnull(df), None)
    
    records = df.to_dict(orient='records')
    
    # We apply our custom encoding step
    print(f"Saving to {output_file} ...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(records, f, default=default_converter, indent=2, ensure_ascii=False)
        
    print("Done! Data successfully converted to JSON format.")

if __name__ == "__main__":
    main()
