# 🛣️ Roadmap – BioStation 🐦🎙️

![Roadmap](https://DataPit-fr.github.io/BioStation/roadmap.svg)

## 🎯 Objectif
Créer une station autonome capable d'enregistrer des sons, de reconnaître les chants d'oiseaux en temps réel à l'aide de machine learning, et de collecter des données environnementales via du C embarqué.

---

## ✅ Phases principales

### 📌 Phase 1 — Spécifications & Setup
- [x] Définir les espèces ciblées (oiseaux locaux)
- [ ] Lister les besoins (autonomie, stockage, détection, communication)
- [ ] Choisir le matériel (Raspberry Pi, microcontrôleur, micro, batterie)

### 📌 Phase 2 — Acquisition audio (Raspberry Pi)
- [ ] Configurer la Raspberry Pi (Raspbian, SSH, Python, etc.)
- [ ] Installer et tester un micro (USB ou I2S)
- [ ] Capturer des sons et les sauvegarder au format WAV
- [ ] Ajouter un prétraitement de signal (librosa)

### 📌 Phase 3 — Module C embarqué (STM32 / Arduino)
- [ ] Lire les capteurs (T°, humidité, lumière…)
- [ ] Implémenter communication série avec la Raspberry (UART/I2C)
- [ ] Déclencher l'enregistrement audio selon capteurs ou bruit détecté
- [ ] Optimiser la consommation du microcontrôleur

### 📌 Phase 4 — Modèle de reconnaissance des chants
- [ ] Collecter un dataset (Xeno-Canto, BirdCLEF)
- [ ] Nettoyer/segmenter les enregistrements
- [ ] Générer des spectrogrammes
- [ ] Entraîner un modèle CNN (Keras/TensorFlow)
- [ ] Exporter en TFLite pour exécution sur Raspberry Pi

### 📌 Phase 5 — Intégration du système
- [ ] Fusionner audio, ML et C embarqué
- [ ] Lancer la détection temps réel sur Pi
- [ ] Sauvegarder les résultats localement ou sur le cloud
- [ ] Logger les données environnementales + espèces détectées

### 📌 Phase 6 — Test terrain & amélioration
- [ ] Tester en extérieur (parc, forêt…)
- [ ] Analyser la précision de détection
- [ ] Optimiser seuils, bruit, conso énergie
- [ ] Ajouter une interface (mini dashboard local ou envoi d’alerte)

---

## 🛠️ Technologies prévues

| Composant             | Stack                          |
|----------------------|--------------------------------|
| Audio & ML           | Python, librosa, PyTorch/TensorFlow |
| Microcontrôleur       | C, UART, STM32Cube / Arduino IDE |
| Détection chant       | CNN / YAMNet / MobileNet       |
| Interface             | Streamlit, Flask (optionnel)   |
| Communication Pi ↔ MCU | UART / I2C                     |

---

## 📦 À venir
- [ ] Détection de plusieurs espèces simultanées
- [ ] Ajout d’une batterie solaire
- [ ] Géolocalisation (via GPS ou IP)
- [ ] Upload automatique vers un serveur/cloud
- [ ] Statistiques journalières ou hebdomadaires
