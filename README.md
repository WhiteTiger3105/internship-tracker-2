<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Internship/Stagiu Avocatura - Bucuresti & Iasi</title>
<style>
:root{
  --bg:#0f1115; --card:#171a21; --border:#262b35; --text:#e8e9ec;
  --muted:#9aa1ad; --accent:#d4af37; --priority:#2e7d4f;
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--text);}
header{padding:32px 24px 16px;border-bottom:1px solid var(--border);}
header h1{margin:0 0 6px;font-size:1.6rem;}
header p{margin:0;color:var(--muted);font-size:.92rem;}
.meta{margin-top:10px;font-size:.8rem;color:var(--muted);}
.controls{display:flex;gap:10px;flex-wrap:wrap;padding:18px 24px;border-bottom:1px solid var(--border);}
.controls button{background:var(--card);border:1px solid var(--border);color:var(--text);padding:7px 14px;border-radius:20px;font-size:.82rem;cursor:pointer;}
.controls button.active{background:var(--accent);color:#1a1a1a;border-color:var(--accent);}
main{padding:20px 24px 60px;max-width:980px;margin:0 auto;}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px 18px;margin-bottom:14px;}
.card.priority{border-left:4px solid var(--priority);}
.card h3{margin:0 0 4px;font-size:1.02rem;}
.tag{display:inline-block;font-size:.7rem;padding:2px 8px;border-radius:10px;background:#222633;color:var(--muted);margin-right:6px;}
.tag.priority{background:var(--priority);color:#fff;}
.region{font-size:.78rem;color:var(--accent);}
.snippet{margin:8px 0;font-size:.88rem;color:#cfd3da;line-height:1.45;}
.quals{margin-top:8px;font-size:.8rem;color:var(--muted);}
.quals b{color:var(--text);}
a.src{font-size:.8rem;color:var(--accent);text-decoration:none;}
footer{text-align:center;color:var(--muted);font-size:.78rem;padding:20px;}
.empty{color:var(--muted);text-align:center;padding:40px;}
</style>
</head>
<body>
<header>
  <h1>Internship / Stagiu de practica - Avocatura</h1>
  <p>Bucuresti & Iasi · Prioritizat: Corporate/M&A, Civil, Imobiliare</p>
  <div class="meta">Ultima actualizare: 2026-06-22T08:00:00 · 2 rezultate gasite</div>
</header>
<div class="controls">
  <button id="btn-all" class="active" onclick="filterCards('all')">Toate</button>
  <button id="btn-Bucuresti" onclick="filterCards('Bucuresti')">Bucuresti</button>
  <button id="btn-Iasi" onclick="filterCards('Iasi')">Iasi</button>
  <button id="btn-General" onclick="filterCards('General')">Job boards generale</button>
</div>
<main>

    <div class="card priority" data-region="Bucuresti">
      <span class="region">Bucuresti</span>
      <h3>NNDKP</h3>
      <span class="tag priority">M&A / Corporate / Civil / Imobiliare</span>
      <div class="snippet">Cautam studenti la drept pentru stagiu de practica in echipa de Corporate/M&A. Cerinte: an III-IV, engleza avansata, cunostinte Excel.</div>
      <div class="quals"><b>Match cu profilul tau:</b><br>Ai engleza B2 Cambridge — cerinta indeplinita.<br>Atentie: cerinta tipica An III/IV — tu esti An II, verifica daca accepta exceptii.<br>Cerinta detectata: excel</div>
      <div><a class="src" href="https://www.nndkp.ro/cariere/stagiu-corporate" target="_blank" rel="noopener">Vezi sursa &rarr;</a></div>
    </div>
    
    <div class="card priority" data-region="Bucuresti">
      <span class="region">Bucuresti</span>
      <h3>Wolf Theiss</h3>
      <span class="tag priority">M&A / Corporate / Civil / Imobiliare</span>
      <div class="snippet">Internship program for law students - Real Estate team. Requirements: fluent English, German is a plus.</div>
      <div class="quals"><b>Match cu profilul tau:</b><br>Ai engleza B2 Cambridge — cerinta indeplinita.<br>Ai germana functionala — diferentiator, mai ales pt. Wolf Theiss/Schoenherr.</div>
      <div><a class="src" href="https://www.wolftheiss.com/careers/internship" target="_blank" rel="noopener">Vezi sursa &rarr;</a></div>
    </div>
    
</main>
<footer>Generat automat zilnic via GitHub Actions. Nu inlocuieste verificarea directa pe site-urile firmelor.</footer>
<script>
function filterCards(region){
  document.querySelectorAll('.card').forEach(c=>{
    c.style.display = (region==='all' || c.dataset.region===region) ? '' : 'none';
  });
  document.querySelectorAll('.controls button').forEach(b=>b.classList.remove('active'));
  document.getElementById('btn-'+region).classList.add('active');
}
</script>
</body>
</html>
