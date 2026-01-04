import pandas as pd
import requests
import os
MAPBOX_TOKEN = 'pk.eyJ1IjoidGFudTgyNSIsImEiOiJjbWp4eTJ0ODA1c2lwM2VzNTdzbGsxcjNpIn0.4V27lKGTJczNps3Fhbusvg'
IMAGE_DIR = './data/images/'
os.makedirs(IMAGE_DIR, exist_ok=True)
def fetch_image(df):
    print(f"start fetching images for {len(df)} entries ...")
    for idx , row in df.iterrows():
        img_id = row['id']
        lat , lon = row['lat'], row['long']
        img_path = os.path.join(IMAGE_DIR, f"{img_id}.jpg")
        if os.path.exists(img_path):
            continue
        url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{lon},{lat},18,0/600x600?access_token={MAPBOX_TOKEN}"
        try:
            res = requests.get(url , timeout=10)
            if res.status_code == 200:
                with open(img_path , 'wb') as f:
                    f.write(res.content)
            else:
                print(f"ERROR{res.status_code} for id {img_id}")
        except Exception as e:
            print(f"Failed ID {img_id}:{e}")
if __name__ == "__main__":
    try:
        train = pd.read_excel('./data/raw/Train.xlsx').dropna(subset=['lat','long'])
        test = pd.read_excel('./data/raw/Test 2.xlsx').dropna(subset=['lat','long'])
        train.to_csv('data/train_cleaned.csv', index=False)
        test.to_csv('data/test_cleaned.csv', index=False)
        print("CSVs generated successfully in the /data folder.")
        full_data = pd.concat([train, test])
        fetch_image(full_data)
        print("Image fetching completed.")
    except FileNotFoundError as e:
        print(f"Error: could find the file at {e.filename}. Please ensure the file exists in the specified path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
