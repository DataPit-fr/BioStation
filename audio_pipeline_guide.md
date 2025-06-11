# 🐦 Pipeline Audio : Téléchargement, Découpage et Spectrogrammes

Ce guide décrit comment récupérer des sons d’oiseaux, les découper et générer des spectrogrammes pour de l’analyse ou de l'entraînement machine learning.

---

## 📁 Structure des dossiers

```
project/
├── data/
│   ├── raw/           # Fichiers audio téléchargés
│   ├── processed/     # Fichiers audio découpés (chunks)
│   └── spectrograms/  # Images des spectrogrammes
├── scripts/
│   ├── download_xc.py           # Script de téléchargement depuis xeno-canto
│   ├── segment_audio.py         # Script de découpe audio (optionnel si non encore fourni)
│   └── generate_spectrograms.py # Script de génération de spectrogrammes
```

---

## 🔽 Étape 1 : Télécharger des enregistrements audio

Utilise le script `download_xc.py` pour récupérer jusqu’à 30 enregistrements d’une espèce depuis [xeno-canto](https://www.xeno-canto.org/).

```bash
python scripts/download_xc.py --species "Columba livia" --max 30 --output data/raw
```

- `--species` : Nom latin de l’espèce
- `--max` : Nombre d’enregistrements à télécharger
- `--output` : Dossier où stocker les fichiers `.mp3` téléchargés

---

## ✂️ Étape 2 : Découper les fichiers audio (si applicable)

Ce script n’est pas fourni ici, mais l’idée est de transformer les `.mp3` ou `.wav` longs en petits segments `.wav` (e.g., 5 sec).

```bash
python scripts/segment_audio.py --input_dir data/raw --output_dir data/processed --chunk_duration 5
```

*(Remplace cette commande selon ton script réel de découpe)*

---

## 📊 Étape 3 : Générer les spectrogrammes

Convertis les segments `.wav` en images `.png` représentant les spectrogrammes de Mel (format prêt pour les CNN).

```bash
python scripts/generate_spectrograms.py --input_dir data/processed --output_dir data/spectrograms
```

Chaque image générée sera de dimension **224x224 pixels**, et stockée avec la même structure que les fichiers d’entrée.

---

## ✅ Pré-requis Python

Assure-toi d’avoir les bibliothèques suivantes installées :

```bash
conda install -c conda-forge librosa matplotlib pysoundfile
```

ou avec pip :

```bash
pip install librosa matplotlib soundfile
```

---

## 📌 Remarques

- Si une erreur `libsndfile.dll` apparaît : passer à `librosa` et `pysoundfile` évite ce problème sur Windows.
- Le spectrogramme est en échelle log et utilise la colormap `magma` pour une meilleure lisibilité visuelle.
- Tu peux adapter la résolution, le nombre de filtres `Mel`, etc. dans le script `generate_spectrograms.py`.

---

🧠 Idée bonus : ajoute `tqdm` pour une barre de progression et surveille facilement les gros batchs de sons.
