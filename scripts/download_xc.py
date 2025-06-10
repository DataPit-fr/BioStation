import os
import argparse
import requests
from tqdm import tqdm

def search_xeno_canto(species, max_results=50):
    query = species.replace(' ', '+')
    base_url = f"https://xeno-canto.org/api/2/recordings?query={query}"
    all_results = []
    page = 1

    print(f"🔍 Searching Xeno-Canto for: {species}")
    while len(all_results) < max_results:
        url = base_url + f"&page={page}"
        resp = requests.get(url)
        data = resp.json()
        if 'recordings' not in data:
            break

        all_results.extend(data['recordings'])
        if page >= int(data.get('numPages', 1)):
            break
        page += 1

    return all_results[:max_results]

def download_recordings(recordings, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for rec in tqdm(recordings, desc="⬇ Downloading"):
        url = url = rec["file"] if rec["file"].startswith("http") else "https:" + rec["file"]
        file_name = f"{rec['gen']}_{rec['sp']}_{rec['id']}.mp3"
        file_path = os.path.join(output_dir, file_name)

        if os.path.exists(file_path):
            continue

        try:
            r = requests.get(url, stream=True)
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        except Exception as e:
            print(f"❌ Failed to download {file_name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--species', type=str, required=True, help="Nom scientifique, ex: 'Parus major'")
    parser.add_argument('--max', type=int, default=50, help="Nombre max d'enregistrements")
    parser.add_argument('--output', type=str, default='data/raw', help="Répertoire de sortie")
    args = parser.parse_args()

    results = search_xeno_canto(args.species, args.max)
    download_recordings(results, args.output)