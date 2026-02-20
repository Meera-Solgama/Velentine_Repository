import base64
import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Meera ❤ Zeel — Love Flight", layout="wide")

ASSETS = Path(__file__).parent / "assets"

def to_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    ext = path.suffix.lower().replace(".", "")
    mime = "png" if ext == "png" else "jpeg"
    return f"data:image/{mime};base64," + base64.b64encode(path.read_bytes()).decode("utf-8")

# -----------------------
# STAGES (Removed 26 Dec 2023 as you said it is NOT an event)
# -----------------------
stages = [
    {"id":"req","date":"(No date)","title":"Instagram Request 💌",
     "desc":"Zeel sent request… Meera accepted ✅",
     "ai":"ai_00_request.png"},

    {"id":"d17","date":"17 Dec 2023","title":"First Meet ✨",
     "desc":"Commerce Six Road Metro Station",
     "ai":"ai_01_17dec.png"},

    # ❌ Removed: 26 Dec 2023 (not an event)

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

payload = [{**s, "img": to_data_uri(ASSETS / s["ai"])} for s in stages]
payload_json = json.dumps(payload)

st.markdown("## ✈️ Meera ❤ Zeel — Love Flight (Game Journey)")

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  :root{
    --text: rgba(255,255,255,.96);
    --muted: rgba(255,255,255,.80);
    --glass: rgba(255,255,255,.14);
    --stroke: rgba(255,255,255,.22);
    --shadow: 0 22px 90px rgba(0,0,0,.45);
  }
  html, body { height:100%; }
  *{ box-sizing:border-box; }
  body{
    margin:0;
    overflow:hidden;
    font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial;
    color: var(--text);
    /* Lovely pink + red theme */
    background:
      radial-gradient(1200px 700px at 20% 10%, rgba(255,255,255,.12), transparent 60%),
      radial-gradient(1100px 650px at 85% 30%, rgba(255,255,255,.10), transparent 62%),
      linear-gradient(135deg, #ff4fa7, #ff2d5f, #ff86b3, #ff3b7a);
  }

  /* Soft floating glow */
  .glow{
    position:fixed; inset:-120px;
    background:
      radial-gradient(900px 540px at 12% 20%, rgba(255,255,255,.16), transparent 60%),
      radial-gradient(900px 540px at 85% 20%, rgba(255,255,255,.12), transparent 60%),
      radial-gradient(1200px 800px at 50% 95%, rgba(0,0,0,.18), transparent 65%);
    filter: blur(10px);
    z-index:-4;
    pointer-events:none;
  }

  /* Animated hearts in background */
  .heart{
    position:fixed;
    bottom:-30px;
    font-size: 18px;
    opacity: 0;
    animation: floatUp linear infinite;
    z-index:-3;
    filter: drop-shadow(0 12px 22px rgba(0,0,0,.22));
    pointer-events:none;
  }
  @keyframes floatUp{
    0%   { transform: translateY(0) translateX(0) scale(.7) rotate(0deg); opacity: 0; }
    10%  { opacity: .78; }
    100% { transform: translateY(-120vh) translateX(var(--dx)) scale(1.35) rotate(18deg); opacity: 0; }
  }

  /* HUD */
  .hud{
    position:fixed; left:14px; right:14px; top:12px;
    display:flex; justify-content:space-between; align-items:center; gap:12px;
    z-index:30;
  }
  .pill{
    background: var(--glass);
    border: 1px solid var(--stroke);
    border-radius: 999px;
    padding: 10px 14px;
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 40px rgba(0,0,0,.20);
    display:flex; gap:10px; align-items:center;
    min-height: 44px;
    white-space: nowrap;
  }
  .title{ font-weight: 950; letter-spacing:.2px; }
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

  /* Map */
  .wrap{
    position:fixed; inset:0;
    padding: 74px 14px 14px;
    display:flex; flex-direction:column; gap:12px;
  }
  .map{
    flex:1;
    position:relative;
    border-radius: 26px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.16);
    backdrop-filter: blur(12px);
    overflow:hidden;
    box-shadow: 0 26px 90px rgba(0,0,0,.30);
  }

  .route{
    position:absolute;
    left:6%; right:6%;
    top:52%;
    border-top: 3px dashed rgba(255,255,255,.55);
    filter: drop-shadow(0 10px 18px rgba(0,0,0,.22));
  }

  .stops{
    position:absolute;
    left:6%; right:6%;
    top: calc(52% - 32px);
    display:flex; justify-content:space-between; align-items:center;
    gap:10px;
  }

  .stop{
    width: 44px; height: 44px;
    border-radius: 999px;
    background: rgba(255,255,255,.16);
    border: 1px solid rgba(255,255,255,.30);
    backdrop-filter: blur(10px);
    display:grid; place-items:center;
    cursor:pointer;
    box-shadow: 0 12px 35px rgba(0,0,0,.22);
    transition: transform .15s ease, background .15s ease, outline .15s ease;
    outline: 0 solid rgba(255,255,255,0);
    position:relative;
  }
  .stop:hover{ transform: translateY(-2px) scale(1.04); background: rgba(255,255,255,.22); }
  .stop.active{
    background: rgba(255,255,255,.30);
    outline: 3px solid rgba(255,255,255,.20);
    transform: translateY(-3px) scale(1.07);
  }
  .stop.opened{
    background: rgba(255,255,255,.26);
    border-color: rgba(255,255,255,.42);
  }
  .stop .n{ font-weight: 900; font-size: 12px; user-select:none; }
  .stop .hint{
    position:absolute;
    top:-36px; left:50%;
    transform: translateX(-50%);
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(0,0,0,.34);
    border: 1px solid rgba(255,255,255,.22);
    font-size: 12px;
    white-space: nowrap;
    opacity: 0;
    transition: opacity .15s ease;
    pointer-events:none;
    backdrop-filter: blur(8px);
  }
  .stop:hover .hint{ opacity: 1; }

  /* Plane + trail */
  .plane{
    position:absolute;
    top: calc(52% - 74px);
    left: 6%;
    font-size: 34px;
    transform: translateX(-50%);
    filter: drop-shadow(0 18px 26px rgba(0,0,0,.30));
    z-index:10;
    will-change:left;
  }
  .trail{
    position:absolute;
    top: calc(52% - 52px);
    left: 6%;
    height: 6px;
    width: 0%;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(255,255,255,.0), rgba(255,255,255,.65), rgba(255,255,255,.0));
    opacity: .7;
    z-index:9;
    transition: width .25s ease;
  }

  /* Bottom info */
  .bar{
    background: var(--glass);
    border: 1px solid var(--stroke);
    border-radius: 18px;
    padding: 10px 12px;
    backdrop-filter: blur(12px);
    display:flex; justify-content:space-between; align-items:center; gap:10px;
  }
  .nowBox{ display:flex; flex-direction:column; gap:2px; }
  .nowTitle{
    width: fit-content;
    font-weight: 950;
    font-size: 14px;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,.18);
    border: 1px solid rgba(255,255,255,.18);
    box-shadow: 0 14px 36px rgba(0,0,0,.14);
  }
  .nowSub{ font-size: 12px; color: var(--muted); }

  /* Overlay */
  .overlay{
    position:fixed; inset:0;
    display:none;
    align-items:center; justify-content:center;
    background: rgba(0,0,0,.45);
    backdrop-filter: blur(10px);
    z-index:80;
    padding: 18px;
  }
  .card{
    width: min(900px, 96vw);
    border-radius: 26px;
    background: rgba(255,255,255,.14);
    border: 1px solid rgba(255,255,255,.22);
    box-shadow: var(--shadow);
    overflow:hidden;
    transform: scale(.98);
    animation: pop .16s ease forwards;
  }
  @keyframes pop{ to{ transform: scale(1); } }

  .cardTop{
    display:flex; justify-content:space-between; align-items:center; gap:12px;
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
    grid-template-columns: 1.1fr 1fr;
    gap: 14px;
    padding: 14px;
  }

  /* 3D photo wrapper */
  .photo3d{
    position:relative;
    border-radius: 22px;
    transform-style: preserve-3d;
    perspective: 900px;
  }
  .shine{
    position:absolute;
    inset:0;
    border-radius: 22px;
    background: radial-gradient(600px 220px at var(--mx,50%) var(--my,30%), rgba(255,255,255,.28), transparent 60%);
    mix-blend-mode: screen;
    pointer-events:none;
    opacity:.65;
  }

  /* Medium image (clear not too big) */
  .midImg{
    width: 100%;
    height: clamp(280px, 45vh, 420px);
    object-fit: cover;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.18);
    background: rgba(255,255,255,.08);
    transform: translateZ(18px);
    box-shadow: 0 18px 55px rgba(0,0,0,.25);
    display:block;
  }

  .info{
    display:flex; flex-direction:column; gap: 10px;
  }
  .date{
    width:fit-content;
    padding: 7px 10px;
    border-radius: 999px;
    background: rgba(255,255,255,.16);
    border: 1px solid rgba(255,255,255,.18);
    font-size: 12px;
    color: rgba(255,255,255,.92);
  }
  .head{ font-size: 24px; font-weight: 950; line-height: 1.08; }
  .desc{ font-size: 14px; line-height: 1.6; color: rgba(255,255,255,.90); }

  @media (max-width: 860px){
    .cardBody{ grid-template-columns: 1fr; }
    .midImg{ height: clamp(260px, 38vh, 360px); }
  }
</style>
</head>

<body>
  <div class="glow"></div>

  <div class="hud">
    <div class="pill">
      <div class="title">💖 Love Flight — click a stop</div>
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
      <div class="trail" id="trail"></div>
      <div class="plane" id="plane">✈️</div>
      <div class="stops" id="stops"></div>
    </div>

    <div class="bar">
      <div class="nowBox">
        <div class="nowTitle" id="nowTitle">Current: —</div>
        <div class="nowSub" id="nowSub">Click a stop</div>
      </div>
      <span class="tiny">Active stop highlighted • 3D photo animation</span>
    </div>
  </div>

  <div class="overlay" id="overlay">
    <div class="card" id="card">
      <div class="cardTop">
        <div style="display:flex; gap:10px; align-items:center;">
          <div class="date" id="cDate"></div>
          <div style="font-weight:900; color:rgba(255,255,255,.92);" id="cSmall"></div>
        </div>
        <button class="x" id="close">✕</button>
      </div>

      <div class="cardBody">
        <div class="photo3d" id="photo3d">
          <img class="midImg" id="cImg" src="" alt="memory"/>
          <div class="shine" id="shine"></div>
        </div>

        <div class="info">
          <div class="head" id="cHead"></div>
          <div class="desc" id="cDesc"></div>
          <div class="tiny" style="margin-top:auto;">
            Tip: Click outside to close • Use Next/Prev to fly
          </div>
        </div>
      </div>
    </div>
  </div>

<script>
  // ---- Animated hearts background ----
  const heartIcons = ["❤","💗","💖","💕","💞"];
  for(let i=0;i<34;i++){
    const h = document.createElement("div");
    h.className = "heart";
    h.style.left = (Math.random()*100) + "vw";
    h.style.animationDuration = (6 + Math.random()*8) + "s";
    h.style.fontSize = (14 + Math.random()*18) + "px";
    h.style.setProperty("--dx", ((Math.random()*140)-70) + "px");
    h.innerHTML = heartIcons[Math.floor(Math.random()*heartIcons.length)];
    document.body.appendChild(h);
  }

  const STAGES = __PAYLOAD__;

  const KEY = "mz_love_flight_v4";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));

  const stopsEl = document.getElementById("stops");
  const plane = document.getElementById("plane");
  const trail = document.getElementById("trail");
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

  const photo3d = document.getElementById("photo3d");
  const shine = document.getElementById("shine");

  let idx = 0;
  let anim = null;

  function save(){
    localStorage.setItem(KEY, JSON.stringify(Array.from(opened)));
    updateCounter();
  }

  function updateCounter(){
    counter.textContent = `${opened.size} / ${STAGES.length} opened`;
  }

  function pctFor(i){
    if(STAGES.length <= 1) return 6;
    return (6 + (88 * (i/(STAGES.length-1))));
  }

  function setActiveStop(i){
    [...stopsEl.children].forEach((b, j)=>{
      b.classList.toggle("active", j === i);
    });
  }

  function flyTo(i){
    i = Math.max(0, Math.min(STAGES.length-1, i));
    const from = parseFloat(plane.dataset.pct || pctFor(idx));
    const to = pctFor(i);

    if(anim) cancelAnimationFrame(anim);

    const start = performance.now();
    const dur = 650;
    const ease = (t) => 1 - Math.pow(1 - t, 3);

    idx = i;
    setActiveStop(idx);

    const s = STAGES[idx];
    nowTitle.textContent = `Current: Stop ${idx+1} — ${s.title}`;
    nowSub.textContent = `${s.date}`;
    trail.style.width = (to - 6) + "%";

    function step(now){
      const t = Math.min(1, (now - start) / dur);
      const cur = from + (to - from) * ease(t);

      plane.style.left = cur + "%";
      plane.dataset.pct = cur;

      if(t < 1){
        anim = requestAnimationFrame(step);
      }else{
        plane.dataset.pct = to;
        plane.style.left = to + "%";
      }
    }
    anim = requestAnimationFrame(step);
  }

  function openStage(i){
    flyTo(i);

    const s = STAGES[idx];
    opened.add(s.id);
    save();

    const btn = stopsEl.children[idx];
    if(btn) btn.classList.add("opened");

    cImg.src = s.img || "";
    cDate.textContent = s.date;
    cSmall.textContent = `Stage ${idx+1} / ${STAGES.length}`;
    cHead.textContent = s.title;
    cDesc.textContent = s.desc;

    overlay.style.display = "flex";
  }

  function closeStage(){ overlay.style.display = "none"; }

  closeBtn.addEventListener("click", closeStage);
  overlay.addEventListener("click", (e)=>{ if(e.target === overlay) closeStage(); });

  document.getElementById("next").addEventListener("click", ()=> flyTo(idx+1));
  document.getElementById("prev").addEventListener("click", ()=> flyTo(idx-1));
  document.getElementById("reset").addEventListener("click", ()=>{
    localStorage.removeItem(KEY);
    opened = new Set();
    buildStops();
    flyTo(0);
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
    setActiveStop(0);
  }

  // 3D tilt effect for photo
  function resetTilt(){
    photo3d.style.transform = "rotateX(0deg) rotateY(0deg)";
    shine.style.setProperty("--mx", "50%");
    shine.style.setProperty("--my", "30%");
  }
  photo3d.addEventListener("mousemove", (e)=>{
    const r = photo3d.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width;  // 0..1
    const y = (e.clientY - r.top) / r.height;  // 0..1
    const rotY = (x - 0.5) * 14;   // left/right
    const rotX = (0.5 - y) * 10;   // up/down
    photo3d.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg)`;
    shine.style.setProperty("--mx", (x*100).toFixed(1) + "%");
    shine.style.setProperty("--my", (y*100).toFixed(1) + "%");
  });
  photo3d.addEventListener("mouseleave", resetTilt);

  buildStops();
  plane.dataset.pct = pctFor(0);
  plane.style.left = pctFor(0) + "%";
  trail.style.width = "0%";
  flyTo(0);
  resetTilt();
</script>
</body>
</html>
"""

html = html.replace("__PAYLOAD__", payload_json)
st.components.v1.html(html, height=820, scrolling=False)

st.caption("✅ 26 Dec removed. ✅ Pink hearts animated background. ✅ Plane flies. ✅ Medium 3D photo opens. ✅ Active event highlighted.")
