# AI-Trust EvalDash - Responsible AI Dashboard

Un tableau de bord complet pour l'évaluation de l'IA responsable, basé sur les recommandations du AI Act et du cadre Confiance.ai.

## 🎯 Objectif

EvalDash agrège les indicateurs de performance, d'équité, de robustesse et d'impact carbone pour fournir une évaluation transparente et complète des modèles d'IA.

## 🏗️ Architecture

### Stack Technique
- **Frontend**: React + TypeScript + Vite
- **Backend**: FastAPI (Python)
- **Visualisations**: Matplotlib + NumPy
- **Conteneurisation**: Docker + Docker Compose
- **Proxy**: Nginx

### Services
1. **Frontend** (Port 8080): Interface utilisateur React avec navigation et sections interactives
2. **Gateway** (Port 8000): API gateway qui route les requêtes et fournit les métriques
3. **Matplotlib Service**: Service de génération de graphiques spécialisés

## 📊 Sections du Dashboard

### 1. Vue d'ensemble
- **Score global**: 0.84 (pondéré : 40% perf + 30% fairness + 20% robustesse + 10% durabilité)
- **Actions rapides**: Run demo, Download PDF

### 2. Performance
- ROC Curve (AUC = 0.92)
- Matrice de confusion
- Métriques: Accuracy, Precision, Recall, F1-Score

### 3. Fairness & Biais
- Analyse des disparités par groupes protégés
- Métriques: Demographic Parity, Equalized Odds
- **Conformité AI Act**: ✅ OK

### 4. Robustesse
- Tests d'adversarialité (FGSM, PGD)
- Performance vs magnitude de perturbation
- **Score de robustesse**: 0.82

### 5. Durabilité
- Consommation énergétique (kWh)
- Impact carbone (CO₂)
- **Eco-label**: 🟠 Medium

### 6. Explicabilité
- Méthodes API-only pour LLM
- Couverture des explications: 92%

### 7. Conformité
- Checklist AI Act intégrée
- **Niveau de risque**: Low

### 8. Monitoring
- Évolution des KPI sur 7 jours
- Détection de drift automatisée

## 🚀 Démarrage Rapide

### Prérequis
- Docker et Docker Compose
- Ports 8000 et 8080 disponibles

### Installation
```bash
# Cloner le projet
cd Responsible-AI

# Construire et lancer les services
docker compose up --build

# Accéder au dashboard
open http://localhost:8080
```

### URLs d'accès
- **Dashboard**: http://localhost:8080
- **API Gateway**: http://localhost:8000
- **Documentation API**: http://localhost:8000/docs

## 📈 API Endpoints

### Métriques
- `GET /metrics/global` - Score global et composants
- `GET /metrics/performance` - Métriques de performance
- `GET /metrics/fairness` - Métriques d'équité
- `GET /metrics/robustness` - Métriques de robustesse
- `GET /metrics/sustainability` - Métriques de durabilité
- `GET /metrics/monitoring` - Données de monitoring

### Graphiques
- `GET /plot/{service_id}?kind={type}` - Génération de graphiques

Types de graphiques disponibles:
- `roc` - ROC Curve
- `confusion` - Matrice de confusion
- `fairness` - Disparités par groupe
- `robustness` - Performance vs perturbation
- `energy` - Consommation énergétique
- `monitoring` - Évolution KPI

## 🎨 Design System

### Palette de couleurs
- **Primaire**: #00467F (Bleu BNP Paribas)
- **Succès**: #009E60 (Vert)
- **Attention**: #FF7A00 (Orange)
- **Texte**: #555 (Gris)

### Typographie
- **Titres**: Roboto Bold (20-32pt)
- **Corps**: Roboto Regular (16pt)
- **Code**: Cousine (monospace)

### Responsive
- Sidebar collapsible sur mobile (< 900px)
- Grids adaptatifs pour graphiques
- Navigation touch-friendly

## 🔧 Configuration

### Variables d'environnement
```bash
SERVICE_NAME=matplotlib-basic
MATPLOTLIB_BASIC_URL=http://matplotlib-basic:8000
```

### Personnalisation
Les métriques et seuils peuvent être ajustés dans:
- `gateway/main.py` - Endpoints et données
- `frontend/src/App.tsx` - Valeurs affichées
- `frontend/src/index.css` - Styles et couleurs

## 📋 Conformité AI Act

Le dashboard intègre automatiquement:
- ✅ Transparence des décisions
- ✅ Non-discrimination
- ✅ Sécurité des données
- ⚠️ Monitoring continu (en cours)

## 🌱 Durabilité

Métriques intégrées:
- Consommation énergétique par phase
- Émissions CO₂ calculées
- Score de durabilité (10% du score global)

## 🔍 Monitoring

Surveillance automatisée:
- KPI quotidiens (accuracy, fairness, sustainability)
- Alertes si dérive > 5%
- Dashboard temps réel

## 👥 Team Data-Fortress

- 👨‍💻 **Dev Lead**: Architecture et développement
- 👩‍🔬 **Data Scientist**: Métriques et modèles
- 🔒 **Security Expert**: Conformité et sécurité
- 🌱 **Sustainability Officer**: Impact environnemental

---

**Join us to build trustworthy AI for finance.**

Pour plus d'informations, consulter la documentation API à http://localhost:8000/docs