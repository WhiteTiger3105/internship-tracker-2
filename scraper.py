# Internship Tracker — Avocatura BUC & Iasi

Site static care se actualizeaza **automat, zilnic**, cu anunturi de
internship/stagiu de practica la firme de avocatura din Bucuresti si Iasi.
Prioritizeaza Corporate/M&A, Civil, Imobiliare. Verifica fiecare anunt pentru
cuvinte-cheie de calificare si le compara cu profilul tau (`data/profile.json`).

## Cum functioneaza

1. `scraper.py` parcurge lista de site-uri din `data/sources.json` (firme de
   avocatura + job boards) si cauta paragrafe/linkuri care contin cuvinte
   precum "stagiu", "internship", "practica" etc. Salveaza rezultatele in
   `data/results.json`.
2. `generate_site.py` transforma `results.json` intr-o pagina HTML
   (`docs/index.html`) — cu filtrare pe Bucuresti / Iasi / general si
   marcaj vizual pentru anunturile prioritare (M&A/Corporate/Civil/Imobiliare).
3. `.github/workflows/daily-update.yml` ruleaza automat aceasta secventa
   **o data pe zi** (6:00 UTC), face commit la rezultate si publica pagina
   pe GitHub Pages.

## Setup (o singura data, ~5 minute)

1. **Creeaza un repo nou pe GitHub** (ex: `internship-tracker`), public.
2. **Incarca toate fisierele din acest folder** in repo (pastreaza structura
   exact cum e: `.github/workflows/`, `data/`, `scraper.py`, etc.)
   - Cel mai simplu: `git init`, `git add .`, `git commit -m "init"`,
     `git remote add origin <url-ul repo-ului tau>`, `git push -u origin main`.
3. **Activeaza GitHub Pages cu sursa "GitHub Actions":**
   - In repo → Settings → Pages → Build and deployment → Source → selecteaza
     **"GitHub Actions"**.
4. **Verifica permisiunile Actions:**
   - Settings → Actions → General → Workflow permissions → selecteaza
     **"Read and write permissions"**.
5. **Ruleaza prima data manual** ca sa testezi:
   - Tab **Actions** → selecteaza workflow-ul "Daily Internship Update" →
     **Run workflow**.
6. Dupa ~1-2 minute, pagina ta va fi live la:
   `https://<username-ul-tau>.github.io/internship-tracker/`

De aici incolo, workflow-ul ruleaza **singur, zilnic**, fara nicio interventie
din partea ta.

## Personalizare

- **Adauga/scoate firme:** editeaza `data/sources.json`.
- **Schimba orele de rulare:** modifica linia `cron:` din
  `.github/workflows/daily-update.yml` (formatul e UTC).
- **Actualizeaza profilul tau:** editeaza `data/profile.json` — de aici se
  trag notele de tip "Ai engleza B2 — cerinta indeplinita" de pe pagina.

## Limitari onestre

- Multe site-uri de firme folosesc JavaScript greu sau platforme de cariere
  (Workday, etc.) care nu sunt usor de "citit" prin scraping simplu (HTML
  static). Pentru acelea, scriptul poate rata anunturi — verifica manual
  periodic firmele cu cele mai mari sanse pentru tine (NNDKP, Wolf Theiss,
  Schoenherr, PNSA, RTPR — Corporate/M&A).
- LinkedIn blocheaza activ scraping-ul automat; linkul din `sources.json`
  e mai mult orientativ — s-ar putea sa nu returneze rezultate utile.
- Acesta e un instrument de **alertare**, nu un inlocuitor pentru verificarea
  directa pe site-urile firmelor inainte de a aplica.
