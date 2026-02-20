import base64
import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Meera ❤ Zeel — Journey Game", layout="wide")

ASSETS = Path(__file__).parent / "assets"

def to_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    ext = path.suffix.lower().replace(".", "")
    mime = "png" if ext == "png" else "jpeg"
    return f"data:image/{mime};base64," + base64.b64encode(path.read_bytes()).decode("utf-8")

# -----------------------
# STAGES
# -----------------------
stages = [
    {"id":"req","date":"(No date)","title":"Instagram Request 💌",
     "desc":"Zeel sent request… Meera accepted ✅",
     "ai":"ai_00_request.png"},

    {"id":"d17","date":"17 Dec 2023","title":"First Meet ✨",
     "desc":"Commerce Six Road Metro Station",
     "ai":"ai_01_17dec.png"},

    {"id":"d26","date":"26 Dec 2023","title":"Second Date 😍",
     "desc":"Second meet — more comfort, more smiles",
     "ai":"ai_02_26dec.png"},

    {"id":"jan6","date":"06 Jan 2024","title":"Ajay’s Cafe ☕",
     "desc":"Coffee + talks + vibes",
     "ai":"ai_03_06jan.png"},

    {"id":"feb14","date":"14 Feb 2024","title":"Ahmedabad Gufa 💗",
     "desc":"Meera met Zeel with her friend Hiral at Ahmedabad Gufa",
     "ai":"ai_04_14feb.png"},

    {"id":"mar6","date":"06 Mar 2024","title":"Parimal Garden 🌿",
     "desc":"First time exploring Parimal together",
     "ai":"ai_05_06mar.png"},

    {"id":"mar8","date":"08 Mar 2024","title":"First Kiss 😘",
     "desc":"First kiss moment in Parimal garden",
     "ai":"ai_06_08mar.png"},

    {"id":"mar28","date":"28 Mar 2024","title":"Cheek Bite 😂",
     "desc":"Funny cute moment — bite on cheek (not ear 😄)",
     "ai":"ai_07_28mar.png"},

    {"id":"mar29","date":"29 Mar 2024","title":"Bounce Up 🎉",
     "desc":"Meera + Zeel + Hiral + Ujjaval at adventure jump park",
     "ai":"ai_08_29mar.png"},

    {"id":"mar30","date":"30 Mar 2024","title":"Parimal (Group) 🌳",
     "desc":"All four spending quality time together at Parimal",
     "ai":"ai_09_30mar.png"},

    {"id":"mar31","date":"31 Mar 2024","title":"Bye + Movie Date 🎬",
     "desc":"Meera & Zeel together saying bye to Hiral (bus) + sleeping sofa movie date",
     "ai":"ai_10_31mar.png"},

    {"id":"apr5","date":"05 Apr 2024","title":"Parimal Again 💞",
     "desc":"Best friend bond + date vibes (quality time)",
     "ai":"ai_11_05apr.png"},

    {"id":"apr6","date":"06 Apr 2024","title":"Unlimited + Real Paprika 🍕",
     "desc":"Real Paprika date — love story started ❤️",
     "ai":"ai_12_06apr.png"},

    {"id":"promise","date":"After that ❤️","title":"Promise Bond 🤝💖",
     "desc":"Best friends → future life partners (no marriage yet)",
     "ai":"ai_13_promise.png"},
]

payload = []
for s in stages:
    payload.append({**s, "img": to_data_uri(ASSETS / s["ai"])})

payload_json = json.dumps(payload)

st.markdown("## ✈️ Meera ❤ Zeel — Journey Game (Click Stops to Unlock Memories)")

html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  :root{
    --text: rgba(255,255,255,.96);
    --muted: rgba(255,255,255,.78);
    --glass: rgba(255,255,255,.14);
    --stroke: rgba(255,255,255,.22);
    --shadow: 0 22px 90px rgba(0,0,0,.45);
    --r: 22px;
  }
  *{box-sizing:border-box}
  body{
    margin:0;
    overflow:hidden;
    font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial;
    color: var(--text);
    background: radial-gradient(1200px 700px at 20% 10%, rgba(255,255,255,.14), transparent 60%),
                radial-gradient(1200px 700px at 85% 30%, rgba(255,255,255,.10), transparent 62%),
                linear-gradient(135deg, #6a5cff, #ff4fb2, #ff7a59);
  }

  /* cute sky overlays */
  .cloud{
    position:fixed;
    top: 8vh;
    width: 220px;
    height: 70px;
    background: rgba(255,255,255,.28);
    border: 1px solid rgba(255,255,255,.18);
    border-radius: 999px;
    filter: blur(.2px);
    box-shadow: 0 18px 45px rgba(0,0,0,.18);
    opacity: .75;
    z-index:-2;
    animation: drift linear infinite;
  }
  .cloud:before,.cloud:after{
    content:"";
    position:absolute;
    background: rgba(255,255,255,.28);
    border: 1px solid rgba(255,255,255,.18);
    border-radius: 999px;
  }
  .cloud:before{ width: 90px; height: 90px; left: 22px; top: -35px; }
  .cloud:after{ width: 120px; height: 120px; left: 95px; top: -55px; }
  @keyframes drift{
    from{ transform: translateX(-30vw); }
    to{ transform: translateX(130vw); }
  }

  .stars{
    position:fixed; inset:0;
    background-image:
      radial-gradient(2px 2px at 15% 20%, rgba(255,255,255,.9), transparent 60%),
      radial-gradient(2px 2px at 70% 18%, rgba(255,255,255,.8), transparent 60%),
      radial-gradient(1.6px 1.6px at 35% 35%, rgba(255,255,255,.7), transparent 60%),
      radial-gradient(1.8px 1.8px at 90% 40%, rgba(255,255,255,.75), transparent 60%),
      radial-gradient(1.6px 1.6px at 55% 12%, rgba(255,255,255,.75), transparent 60%),
      radial-gradient(1.4px 1.4px at 22% 52%, rgba(255,255,255,.6), transparent 60%);
    opacity:.55;
    z-index:-3;
    pointer-events:none;
  }

  /* HUD */
  .hud{
    position:fixed;
    left: 14px; right:14px; top: 12px;
    display:flex; justify-content:space-between; align-items:center; gap:12px;
    z-index:30;
  }
  .pill{
    background: var(--glass);
    border: 1px solid var(--stroke);
    border-radius: 999px;
    padding: 10px 14px;
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 40px rgba(0,0,0,.22);
    display:flex; gap:10px; align-items:center;
    min-height: 44px;
    white-space: nowrap;
  }
  .title{ font-weight: 900; letter-spacing:.2px; }
  .tiny{ font-size: 12px; color: var(--muted); }
  .btn{
    cursor:pointer;
    border: 1px solid var(--stroke);
    background: rgba(255,255,255,.12);
    color: var(--text);
    padding: 9px 12px;
    border-radius: 999px;
    font-weight: 900;
    transition: transform .12s ease, background .12s ease;
  }
  .btn:hover{ background: rgba(255,255,255,.18); }
  .btn:active{ transform: scale(.98); }

  /* Map area */
  .wrap{
    position:fixed; inset:0;
    padding: 74px 14px 14px;
    display:flex;
    flex-direction:column;
    gap: 12px;
  }

  .map{
    flex: 1;
    position:relative;
    border-radius: 26px;
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.16);
    backdrop-filter: blur(10px);
    overflow:hidden;
    box-shadow: 0 26px 90px rgba(0,0,0,.35);
  }

  /* dotted route line */
  .route{
    position:absolute;
    left: 6%;
    right: 6%;
    top: 52%;
    height: 0;
    border-top: 3px dashed rgba(255,255,255,.45);
    filter: drop-shadow(0 10px 20px rgba(0,0,0,.28));
  }

  /* stops row */
  .stops{
    position:absolute;
    left: 6%;
    right: 6%;
    top: calc(52% - 32px);
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap: 10px;
    pointer-events:auto;
  }

  .stop{
    width: 44px;
    height: 44px;
    border-radius: 999px;
    background: rgba(255,255,255,.16);
    border: 1px solid rgba(255,255,255,.30);
    backdrop-filter: blur(10px);
    display:grid;
    place-items:center;
    cursor:pointer;
    position:relative;
    box-shadow: 0 12px 35px rgba(0,0,0,.25);
    transition: transform .15s ease, background .15s ease;
    flex: 0 0 auto;
  }
  .stop:hover{ transform: translateY(-2px) scale(1.03); background: rgba(255,255,255,.22); }
  .stop .n{
    font-weight: 900;
    font-size: 12px;
    color: rgba(255,255,255,.95);
    user-select:none;
  }
  .stop.opened{
    background: rgba(255,255,255,.28);
    border-color: rgba(255,255,255,.40);
  }
  .stop .hint{
    position:absolute;
    top: -36px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,.35);
    border: 1px solid rgba(255,255,255,.22);
    color: rgba(255,255,255,.92);
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 12px;
    white-space: nowrap;
    opacity: 0;
    pointer-events:none;
    transition: opacity .15s ease;
    backdrop-filter: blur(8px);
  }
  .stop:hover .hint{ opacity: 1; }

  /* plane */
  .plane{
    position:absolute;
    top: calc(52% - 72px);
    left: 6%;
    font-size: 34px;
    transform: translateX(-50%);
    transition: left .55s cubic-bezier(.2,.9,.2,1);
    filter: drop-shadow(0 18px 26px rgba(0,0,0,.35));
    z-index: 10;
  }

  /* bottom panel - stage list small */
  .bar{
    background: var(--glass);
    border: 1px solid var(--stroke);
    border-radius: 18px;
    padding: 10px 12px;
    backdrop-filter: blur(12px);
    display:flex;
    gap: 10px;
    align-items:center;
    justify-content:space-between;
  }
  .bar b{ font-size: 13px; }
  .bar span{ font-size: 12px; color: var(--muted); }

  /* Big open card (overlay) */
  .overlay{
    position:fixed;
    inset:0;
    display:none;
    align-items:center;
    justify-content:center;
    z-index: 80;
    background: rgba(0,0,0,.45);
    backdrop-filter: blur(9px);
    padding: 18px;
  }
  .card{
    width: min(980px, 96vw);
    border-radius: 26px;
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.22);
    box-shadow: var(--shadow);
    overflow:hidden;
    transform: scale(.98);
    animation: pop .16s ease forwards;
  }
  @keyframes pop{ to{ transform: scale(1); } }

  .cardTop{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:12px;
    padding: 12px 14px;
    background: rgba(255,255,255,.10);
    border-bottom: 1px solid rgba(255,255,255,.16);
  }
  .x{
    cursor:pointer;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,.22);
    background: rgba(255,255,255,.12);
    color: var(--text);
    padding: 8px 12px;
    font-weight: 900;
  }

  .cardBody{
    display:grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 14px;
    padding: 14px;
  }

  /* BIG IMAGE */
  .bigImg{
    width: 100%;
    height: min(62vh, 520px);
    object-fit: cover;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.18);
    background: rgba(255,255,255,.08);
  }

  .info{
    display:flex;
    flex-direction:column;
    gap: 10px;
    min-width:0;
  }
  .date{
    width:fit-content;
    padding: 7px 10px;
    border-radius: 999px;
    background: rgba(255,255,255,.14);
    border: 1px solid rgba(255,255,255,.18);
    font-size: 12px;
    color: rgba(255,255,255,.90);
  }
  .head{
    font-size: 26px;
    font-weight: 950;
    line-height: 1.05;
  }
  .desc{
    font-size: 14px;
    line-height: 1.6;
    color: rgba(255,255,255,.88);
  }

  @media (max-width: 860px){
    .cardBody{ grid-template-columns: 1fr; }
    .bigImg{ height: min(52vh, 420px); }
  }
</style>
</head>

<body>
  <div class="stars"></div>
  <div class="cloud" style="left:-30vw; top:9vh; animation-duration: 24s;"></div>
  <div class="cloud" style="left:-45vw; top:22vh; animation-duration: 30s; opacity:.6;"></div>
  <div class="cloud" style="left:-60vw; top:38vh; animation-duration: 34s; opacity:.5;"></div>

  <div class="hud">
    <div class="pill">
      <div class="title">✈️ Tap a stop to open memory</div>
      <div class="tiny" id="counter">0 opened</div>
    </div>
    <div class="pill">
      <button class="btn" id="prev">⬅️ Prev</button>
      <button class="btn" id="next">Next ➡️</button>
      <button class="btn" id="reset">Reset</button>
    </div>
  </div>

  <div class="wrap">
    <div class="map" id="map">
      <div class="route"></div>
      <div class="plane" id="plane">✈️</div>
      <div class="stops" id="stops"></div>
    </div>

    <div class="bar">
      <div>
        <b id="nowTitle">Ready ✨</b><br/>
        <span id="nowSub">Click any stop to begin</span>
      </div>
      <span>Game Style Journey • Big Photo Viewer</span>
    </div>
  </div>

  <div class="overlay" id="overlay">
    <div class="card" id="card">
      <div class="cardTop">
        <div style="display:flex; gap:10px; align-items:center; min-width:0;">
          <div class="date" id="cDate"></div>
          <div style="font-weight:900; color:rgba(255,255,255,.92); overflow:hidden; text-overflow:ellipsis; white-space:nowrap;" id="cSmall"></div>
        </div>
        <button class="x" id="close">✕</button>
      </div>

      <div class="cardBody">
        <img class="bigImg" id="cImg" src="" alt="memory"/>
        <div class="info">
          <div class="head" id="cHead"></div>
          <div class="desc" id="cDesc"></div>
          <div class="tiny" style="margin-top:auto;">
            Tip: Click outside to close • Use Next/Prev to move plane
          </div>
        </div>
      </div>
    </div>
  </div>

<script>
  const STAGES = __PAYLOAD__;

  // progress saved
  const KEY = "mz_game_opened_v2";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));

  const stopsEl = document.getElementById("stops");
  const plane = document.getElementById("plane");
  const counter = document.getElementById("counter");

  const nowTitle = document.getElementById("nowTitle");
  const nowSub = document.getElementById("nowSub");

  const overlay = document.getElementById("overlay");
  const closeBtn = document.getElementById("close");
  const cImg = document.getElementById("cImg");
  const cDate = document.getElementById("cDate");
  const cSmall = document.getElementById("cSmall");
  const cHead = document.getElementById("cHead");
  const cDesc = document.getElementById("cDesc");

  let idx = 0;

  function save(){
    localStorage.setItem(KEY, JSON.stringify(Array.from(opened)));
    updateCounter();
  }

  function updateCounter(){
    counter.textContent = `${opened.size} / ${STAGES.length} opened`;
  }

  function planeTo(i){
    idx = Math.max(0, Math.min(STAGES.length-1, i));
    const pct = STAGES.length === 1 ? 6 : (6 + (88 * (idx/(STAGES.length-1))));
    plane.style.left = pct + "%";

    const s = STAGES[idx];
    nowTitle.textContent = `Stop ${idx+1}: ${s.title}`;
    nowSub.textContent = s.date;

    // highlight current stop
    [...stopsEl.children].forEach((b, j)=>{
      b.style.transform = j === idx ? "translateY(-2px) scale(1.06)" : "";
    });
  }

  function openStage(i){
    planeTo(i);
    const s = STAGES[idx];

    opened.add(s.id);
    save();

    // stop badge opened
    const btn = stopsEl.children[idx];
    if(btn) btn.classList.add("opened");

    // big viewer
    cImg.src = s.img || "";
    cDate.textContent = s.date;
    cSmall.textContent = `Stage ${idx+1} / ${STAGES.length}`;
    cHead.textContent = s.title;
    cDesc.textContent = s.desc;

    overlay.style.display = "flex";
  }

  function closeStage(){
    overlay.style.display = "none";
  }

  closeBtn.addEventListener("click", closeStage);
  overlay.addEventListener("click", (e)=>{
    if(e.target === overlay) closeStage();
  });

  document.getElementById("next").addEventListener("click", ()=>{
    planeTo(idx+1);
  });
  document.getElementById("prev").addEventListener("click", ()=>{
    planeTo(idx-1);
  });
  document.getElementById("reset").addEventListener("click", ()=>{
    localStorage.removeItem(KEY);
    opened = new Set();
    buildStops();
    planeTo(0);
    closeStage();
  });

  function buildStops(){
    stopsEl.innerHTML = "";
    STAGES.forEach((s, i)=>{
      const b = document.createElement("div");
      b.className = "stop" + (opened.has(s.id) ? " opened" : "");
      b.innerHTML = `
        <div class="hint">${s.date} • ${s.title}</div>
        <div class="n">${i+1}</div>
      `;
      b.addEventListener("click", ()=> openStage(i));
      stopsEl.appendChild(b);
    });
    updateCounter();
  }

  buildStops();
  planeTo(0);
</script>
</body>
</html>
"""

html = html.replace("__PAYLOAD__", payload_json)

st.components.v1.html(html, height=820, scrolling=False)
st.caption("✅ Click a stop to open big photo. Click outside to close. Plane moves with Next/Prev.")
