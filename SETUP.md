# Setup (one-time)

## 1. Maths-lab environment (conda)
```bash
conda env create -f environment.yml   # creates the 'scholar' env from the pinned list
conda activate scholar
nbstripout --install                  # run inside this repo: keeps notebook diffs clean
```
If you change packages later:
```bash
conda env export --from-history > environment.yml
```

## 2. First-use test
Open the repo in VS Code (`code .`), install the **Python** + **Jupyter** extensions,
open `maths-lab/lab.ipynb`, pick the **scholar** kernel, run the first cell.
You should see x**2 - 1 factor to (x - 1)(x + 1).

## 3. Obsidian
Open Obsidian → "Open folder as vault" → select this repo's `notes/` folder.

## 4. Accounts (register the first four before Module 1)
- Project Euler  — projecteuler.net   (public solutions only for #1–100; rest go in private/)
- Khan Academy   — khanacademy.org    (gives the ≥80% mastery checkpoints)
- Dr Frost Maths — drfrostmaths.com
- iNaturalist    — inaturalist.org     (+ app; biodiversity baseline starts in Module 1)
- Anki           — apps.ankiweb.net    (+ AnkiWeb account + AnkiDroid); one "Homestead Scholar" deck

## Commit rhythm
Friday: stage all → commit "Week N: ..." → push.
Module end: fill grade.md + update ledger/, then commit + push.
