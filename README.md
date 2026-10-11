# SMPM Poulainville · Documentation

App web (PWA) qui affiche les manuels, guides, schémas et références de l'équipe.
Les PDF et images s'ouvrent **directement dans l'app** (visionneuse PDF.js intégrée) :
pas besoin de compte Google ni d'application externe. Les documents déjà ouverts
restent consultables **hors-ligne**.

## Ajouter / retirer un document
1. Déposer le fichier dans `docs/<Catégorie>/[<Sous-catégorie>/]`
   (ex. `docs/1_Manuels/17_Manuel_Nouveau.pdf`).
2. Régénérer l'index : `python3 generate_manifest.py`
3. `git add -A && git commit -m "Ajout doc" && git push` → Vercel redéploie tout seul.

Le préfixe `NN_` sert au tri et est masqué dans l'app ; les `_` deviennent des espaces.

## Tester en local
`python3 -m http.server 8765` puis ouvrir http://localhost:8765
