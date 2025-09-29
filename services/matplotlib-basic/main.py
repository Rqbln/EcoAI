from io import BytesIO
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import matplotlib
matplotlib.use('Agg') # headless
import matplotlib.pyplot as plt
import numpy as np
import os


SERVICE_NAME = os.getenv("SERVICE_NAME", "matplotlib-basic")


app = FastAPI(title=SERVICE_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/info")
async def info():
    return {"name": SERVICE_NAME, "version": "1.0.0"}


@app.get("/plot")
async def plot(kind: str = Query("sine", enum=[
    "sine", "hist", "scatter",
    "roc", "confusion", "fairness", "robustness",
    "energy", "monitoring"
])):
    buf = BytesIO()

    if kind == "sine":
        x = np.linspace(0, 2*np.pi, 500)
        y = np.sin(2*x) * np.cos(0.5*x)
        plt.figure(figsize=(6,4), dpi=160)
        plt.plot(x, y, linewidth=2, color='#16a34a')
        plt.title("Sine × Cosine", fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

    elif kind == "hist":
        data = np.random.normal(loc=0, scale=1, size=2000)
        plt.figure(figsize=(6,4), dpi=160)
        plt.hist(data, bins=40, color='#22c55e', alpha=0.7, edgecolor='black')
        plt.title("Random Normal Histogram", fontsize=14, fontweight='bold')
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

    elif kind == "scatter":
        x = np.random.rand(200)
        y = np.random.rand(200)
        plt.figure(figsize=(6,4), dpi=160)
        plt.scatter(x, y, alpha=0.6, c='#f59e0b', s=30)
        plt.title("Random Scatter", fontsize=14, fontweight='bold')
        plt.xlabel("X values")
        plt.ylabel("Y values")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

    elif kind == "roc":
        # ROC Curve simulation
        fpr = np.array([0, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0])
        tpr = np.array([0, 0.3, 0.6, 0.8, 0.9, 0.95, 0.98, 1.0])

        plt.figure(figsize=(6,4.5), dpi=120)
        plt.plot(fpr, tpr, linewidth=3, color='#16a34a', label='ROC Curve (AUC = 0.92)')
        plt.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Random Classifier')
        plt.fill_between(fpr, tpr, alpha=0.2, color='#16a34a')

        plt.xlabel('False Positive Rate', fontsize=10)
        plt.ylabel('True Positive Rate', fontsize=10)
        plt.title('ROC Curve - Model Performance', fontsize=12, fontweight='bold')
        plt.legend(fontsize=9)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

    elif kind == "confusion":
        # Matrice de confusion simulée
        from matplotlib.colors import LinearSegmentedColormap

        confusion_matrix = np.array([[850, 45], [38, 867]])
        labels = ['Predicted 0', 'Predicted 1']

        plt.figure(figsize=(4.5,4), dpi=120)
        cmap = LinearSegmentedColormap.from_list('custom', ['white', '#16a34a'])
        plt.imshow(confusion_matrix, cmap=cmap, aspect='equal')

        # Ajouter les valeurs dans les cellules
        for i in range(2):
            for j in range(2):
                plt.text(j, i, str(confusion_matrix[i, j]),
                        ha='center', va='center', fontsize=16,
                        color='white' if confusion_matrix[i, j] > 500 else 'black')

        plt.xticks([0, 1], labels, fontsize=11)
        plt.yticks([0, 1], ['Actual 0', 'Actual 1'], fontsize=11)
        plt.title('Confusion Matrix', fontsize=14, fontweight='bold')

        # Ajouter une barre de couleur
        plt.colorbar(shrink=0.8)
        plt.tight_layout()

    elif kind == "fairness":
        # Graphique de disparités par groupe
        groups = ['Genre\nHomme', 'Genre\nFemme', 'Age\nJeune', 'Age\nSénior', 'Origine\nGroupe A', 'Origine\nGroupe B']
        scores = [0.85, 0.81, 0.83, 0.79, 0.84, 0.80]
        colors = ['#22c55e' if s >= 0.82 else '#f59e0b' if s >= 0.78 else '#ef4444' for s in scores]

        plt.figure(figsize=(7,4.5), dpi=120)
        bars = plt.bar(groups, scores, color=colors, alpha=0.8, edgecolor='black')

        # Ajouter les valeurs sur les barres
        for bar, score in zip(bars, scores):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                    f'{score:.2f}', ha='center', va='bottom', fontweight='bold')

        plt.axhline(y=0.82, color='green', linestyle='--', alpha=0.7, label='Seuil acceptable')
        plt.ylabel('Score de Performance', fontsize=12)
        plt.title('Disparités de Performance par Groupe Protégé', fontsize=14, fontweight='bold')
        plt.ylim(0.75, 0.90)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

    elif kind == "robustness":
        # Performance vs perturbation
        epsilons = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
        fgsm_scores = [0.91, 0.89, 0.86, 0.82, 0.79, 0.75, 0.71]
        pgd_scores = [0.91, 0.87, 0.84, 0.80, 0.77, 0.73, 0.69]

        plt.figure(figsize=(6,4.5), dpi=120)
        plt.plot(epsilons, fgsm_scores, 'o-', linewidth=3, markersize=8,
                color='#16a34a', label='FGSM Attack')
        plt.plot(epsilons, pgd_scores, 's-', linewidth=3, markersize=8,
                color='#f59e0b', label='PGD Attack')

        plt.axhline(y=0.80, color='red', linestyle='--', alpha=0.7, label='Seuil critique')
        plt.fill_between(epsilons, 0.80, 1.0, alpha=0.1, color='green', label='Zone robuste')

        plt.xlabel('Magnitude de Perturbation (ε)', fontsize=12)
        plt.ylabel('Précision du Modèle', fontsize=12)
        plt.title('Robustesse aux Attaques Adversariales', fontsize=14, fontweight='bold')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.ylim(0.65, 0.95)
        plt.tight_layout()

    elif kind == "energy":
        # Consommation énergétique
        phases = ['Entraînement', 'Inférence\n(1k requêtes)', 'Stockage\n(mensuel)']
        kwh_values = [12.5, 0.3, 0.8]
        co2_values = [6.2, 0.15, 0.4]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8,4), dpi=120)

        # Graphique kWh
        bars1 = ax1.bar(phases, kwh_values, color=['#f59e0b', '#22c55e', '#16a34a'],
                       alpha=0.8, edgecolor='black')
        ax1.set_ylabel('Consommation (kWh)', fontsize=11)
        ax1.set_title('Consommation Énergétique', fontsize=13, fontweight='bold')

        for bar, value in zip(bars1, kwh_values):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                    f'{value}', ha='center', va='bottom', fontweight='bold')

        # Graphique CO2
        bars2 = ax2.bar(phases, co2_values, color=['#f59e0b', '#22c55e', '#16a34a'],
                       alpha=0.8, edgecolor='black')
        ax2.set_ylabel('Émissions CO₂ (kg)', fontsize=11)
        ax2.set_title('Impact Carbone', fontsize=13, fontweight='bold')

        for bar, value in zip(bars2, co2_values):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{value}', ha='center', va='bottom', fontweight='bold')

        plt.tight_layout()

    elif kind == "monitoring":
        # Évolution des KPI sur 7 jours
        dates = ['01/12', '02/12', '03/12', '04/12', '05/12', '06/12', '07/12']
        accuracy = [0.91, 0.90, 0.91, 0.89, 0.90, 0.91, 0.91]
        fairness = [0.78, 0.77, 0.79, 0.78, 0.78, 0.79, 0.78]
        sustainability = [0.90, 0.89, 0.90, 0.91, 0.90, 0.90, 0.90]

        plt.figure(figsize=(7,4.5), dpi=120)
        plt.plot(dates, accuracy, 'o-', linewidth=3, markersize=8,
                color='#16a34a', label='Accuracy')
        plt.plot(dates, fairness, 's-', linewidth=3, markersize=8,
                color='#f59e0b', label='Fairness')
        plt.plot(dates, sustainability, '^-', linewidth=3, markersize=8,
                color='#22c55e', label='Sustainability')

        # Zone de seuil acceptable
        plt.axhspan(0.75, 1.0, alpha=0.1, color='green', label='Zone acceptable')
        plt.axhspan(0.70, 0.75, alpha=0.1, color='orange', label='Zone attention')

        plt.ylabel('Score KPI', fontsize=12)
        plt.xlabel('Date', fontsize=12)
        plt.title('Évolution des KPI - Monitoring 7 jours', fontsize=14, fontweight='bold')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.ylim(0.70, 0.95)
        plt.xticks(rotation=45)
        plt.tight_layout()

    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
    plt.close('all')
    buf.seek(0)
    return StreamingResponse(buf, media_type='image/png')


@app.get("/")
async def root():
    return JSONResponse({"ok": True})