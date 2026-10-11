#!/usr/bin/env python3
"""Scanne le dossier docs/ et génère docs.js (liste des documents de l'app).

A relancer après chaque ajout / suppression de fichier :
    python3 generate_manifest.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
EXTS = {".pdf": "pdf", ".png": "image", ".jpg": "image", ".jpeg": "image", ".webp": "image", ".gif": "image"}


def pretty(name):
    name = os.path.splitext(name)[0]
    name = re.sub(r"^\d+_", "", name)
    return name.replace("_", " ").strip()


items = []
for dirpath, dirnames, filenames in os.walk(DOCS):
    dirnames.sort()
    for f in sorted(filenames):
        ext = os.path.splitext(f)[1].lower()
        if ext not in EXTS:
            continue
        full = os.path.join(dirpath, f)
        rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
        parts = os.path.relpath(dirpath, DOCS).split(os.sep)
        parts = [] if parts == ["."] else parts
        items.append({
            "title": pretty(f),
            "path": rel,
            "type": EXTS[ext],
            "size": os.path.getsize(full),
            "category": pretty(parts[0]) if parts else "Divers",
            "sub": pretty(parts[1]) if len(parts) > 1 else "",
        })

with open(os.path.join(ROOT, "docs.js"), "w", encoding="utf-8") as out:
    out.write("// Fichier généré par generate_manifest.py - ne pas modifier à la main\n")
    out.write("window.DOCS = ")
    json.dump(items, out, ensure_ascii=False, indent=1)
    out.write(";\n")

print(f"{len(items)} documents indexés -> docs.js")
