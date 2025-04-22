# Sudoku Solver

[![Licence](https://img.shields.io/badge/license-none-lightgrey.svg)]  
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)]  
[![Build Status](https://img.shields.io/badge/build-passing-green.svg)]  
[![Dernière mise à jour](https://img.shields.io/badge/last%20update-2025--04--22-blue.svg)]  

## Description
**Sudoku Solver** est une application desktop en **Python 3** et **Tkinter** qui permet de :
- Saisir manuellement une grille de Sudoku (9×9).
- Naviguer de case en case avec les flèches du clavier.
- Résoudre la grille en un clic via un algorithme de backtracking.

## Objectifs
- Offrir une interface simple et réactive pour l’entrée et la navigation.  
- Résoudre n’importe quelle grille en quelques secondes.  
- Servir d’outil d’entraînement ou de validation personnelle.

## Installation
```bash
# 1. Cloner le dépôt
git clone https://github.com/MathieuBal/sudoku-solver.git
cd sudoku-solver

# 2. (Optionnel) Créer et activer un environnement virtuel
python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

# 3. Installer les dépendances
# tkinter est inclus dans la stdlib ; pas de pip supplémentaire requis
pip install -r requirements.txt
