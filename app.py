import base64
import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Meera ❤ Zeel — Love River Flight", layout="wide")

ASSETS = Path(__file__).parent / "assets"

def to_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    ext = path.suffix.lower().replace(".", "")
    mime = "png" if ext == "png" else "jpeg"
    return f"data:image/{mime};base64," + base64.b64encode(path.read_bytes()).decode("utf-8")

# -----------------------
# STAGES (26 Dec REMOVED)
# -----------------------
stages = [
    {"id":"req","date":"(No date)","title":"Instagram Request 💌",
     "desc":"Zeel sent request… Meera accepted ✅",
     "ai":"ai_00_request.png"},

    {"id":"d17","date":"17 Dec 2023","title":"First Meet ✨",
     "desc":"Commerce Six Road Metro Station",
     "ai":"ai_01_17dec.png"},

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
     "desc":"Best friends → future life partners",
     "ai":"ai_13_promise.png"},
]

payload = [{**s, "img": to_data_uri(ASSETS / s["ai"])} for s in stages]
payload_json = json.dumps(payload)

# (No boring captions here)
st.markdown("## 💖 Meera ❤ Zeel — Love River Flight")

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  :root{
    --ink: rgba(20, 30, 60, .92);
    --muted: rgba(40, 60, 90, .68);
    --glass: rgba(255,255,255,.52);
    --stroke: rgba(255,255,255,.70);
    --shadow: 0 18px 70px rgba(30, 70, 140, .16);
  }
  html, body { height:100%; }
  *{ box-sizing:border-box; }
  body{
    margin:0;
    overflow:hidden;
    font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial;
    color: var(--ink);

    /* LIGHT BLUE FULL BACKGROUND */
    background:
      radial-gradient(1200px 700px at 18% 15%, rgba(255,255,255,.70), transparent 60%),
      radial-gradient(900px 650px at 85% 25%, rgba(255,255,255,.55), transparent 62%),
      linear-gradient(135deg, #eaf6ff, #d7f0ff, #e9f3ff, #f3fbff);
  }

  /* Red glitter hearts across full background */
  .heart{
    position:fixed;
    bottom:-40px;
    opacity: 0;
    z-index:-4;
    pointer-events:none;
    animation: floatUp linear infinite;
    filter: drop-shadow(0 10px 14px rgba(0,0,0,.12));
  }
  .heart::after{
    content:"❤";
    display:block;
    background: linear-gradient(180deg, #ff0a54, #ff3d7f, #ff0a54);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow:
      0 0 6px rgba(255,0,80,.45),
      0 0 12px rgba(255,0,80,.22);
  }
  @keyframes floatUp{
    0%   { transform: translateY(0) translateX(0) scale(.75) rotate(0deg); opacity: 0; }
    12%  { opacity: .85; }
    100% { transform: translateY(-125vh) translateX(var(--dx)) scale(1.35) rotate(18deg); opacity: 0; }
  }

  /* Glitter sparkles */
  .spark{
    position:fixed;
    width: 5px; height: 5px;
    border-radius: 999px;
    background: rgba(255, 40, 120, .85);
    box-shadow:
      0 0 10px rgba(255,0,90,.35),
      0 0 18px rgba(255,0,90,.18);
    opacity: 0;
    z-index:-3;
    pointer-events:none;
    animation: twinkle ease-in-out infinite;
  }
  @keyframes twinkle{
    0%,100% { transform: scale(.7); opacity: 0; }
    45%     { opacity: .85; }
    60%     { transform: scale(1.35); opacity: .95; }
  }

  /* Simple HUD - only counter (no boring lines) */
  .hud{
    position:fixed; left: 14px; right:14px; top:12px;
    z-index:30;
    display:flex; justify-content:space-between; align-items:center; gap:12px;
  }
  .pill{
    background: rgba(255,255,255,.55);
    border: 1px solid rgba(255,255,255,.80);
    border-radius: 999px;
    padding: 10px 14px;
    backdrop-filter: blur(10px);
    box-shadow: 0 14px 50px rgba(30, 70, 140, .10);
    display:flex; gap:10px; align-items:center;
    min-height: 44px;
    white-space: nowrap;
  }
  .title{ font-weight: 950; letter-spacing:.2px; color: rgba(20,40,70,.92); }
  .tiny{ font-size: 12px; color: var(--muted); }

  .wrap{
    position:fixed; inset:0;
    padding: 70px 12px 14px;
    display:flex;
    flex-direction:column;
    gap: 12px;
  }

  /* Map area - soft glass (not dark / not gray) */
  .map{
    flex:1;
    position:relative;
    border-radius: 28px;
    background: rgba(255,255,255,.20);
    border: 1px solid rgba(255,255,255,.55);
    overflow:hidden;
    box-shadow: var(--shadow);
  }
  .riverSvg{
    position:absolute; inset:0;
    width:100%; height:100%;
    opacity: .95;
  }

  /* Stops */
  .stop{
    position:absolute;
    width: 44px; height:44px;
    border-radius: 999px;
    transform: translate(-50%, -50%);
    display:grid;
    place-items:center;
    cursor:pointer;
    user-select:none;
    background: rgba(255,255,255,.70);
    border: 1px solid rgba(255,255,255,.88);
    box-shadow: 0 16px 40px rgba(30, 70, 140, .12);
    transition: transform .15s ease, background .15s ease, outline .15s ease;
  }
  .stop:hover{ transform: translate(-50%, -50%) scale(1.06); background: rgba(255,255,255,.84); }
  .stop .n{ font-weight: 950; font-size: 12px; color: rgba(30, 60, 95, .92); }
  .stop.active{ outline: 4px solid rgba(255, 0, 90, .14); background: rgba(255,255,255,.92); }
  .stop.opened{ border-color: rgba(255,0,90,.20); background: rgba(255,245,252,.95); }

  .hint{
    position:absolute;
    left: 50%;
    top: -36px;
    transform: translateX(-50%);
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(255,255,255,.92);
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 12px;
    color: rgba(30, 60, 95, .82);
    opacity: 0;
    white-space: nowrap;
    transition: opacity .15s ease;
    box-shadow: 0 12px 30px rgba(30, 70, 140, .10);
    pointer-events:none;
  }
  .stop:hover .hint{ opacity: 1; }

  /* Plane */
  .plane{
    position:absolute;
    font-size: 34px;
    transform: translate(-50%, -50%);
    z-index: 20;
    filter: drop-shadow(0 18px 25px rgba(30, 70, 140, .14));
    will-change: left, top;
  }

  /* Bottom info (no boring captions, only current event) */
  .bar{
    background: rgba(255,255,255,.55);
    border: 1px solid rgba(255,255,255,.80);
    border-radius: 18px;
    padding: 10px 12px;
    backdrop-filter: blur(10px);
    box-shadow: 0 14px 50px rgba(30, 70, 140, .10);
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap: 12px;
  }
  .nowTitle{
    font-weight: 950;
    font-size: 14px;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,.80);
    border: 1px solid rgba(255,255,255,.92);
    width: fit-content;
    color: rgba(20,40,70,.92);
  }
  .nowSub{ font-size: 12px; color: var(--muted); }

  /* --- Gift Boxes (rain + scattered) --- */
  .gift{
    position:absolute;
    width: 42px; height: 42px;
    border-radius: 14px;
    background: rgba(255,255,255,.85);
    border: 1px solid rgba(255,255,255,.92);
    box-shadow: 0 16px 40px rgba(30, 70, 140, .12);
    display:grid;
    place-items:center;
    cursor:pointer;
    user-select:none;
    transform: translate(-50%, -50%);
    transition: transform .12s ease;
    z-index: 25;
  }
  .gift:hover{ transform: translate(-50%, -50%) scale(1.05) rotate(-1deg); }
  .gift .emoji{ font-size: 22px; }

  /* Falling gifts */
  .giftFall{
    position:fixed;
    top:-60px;
    width: 46px; height: 46px;
    border-radius: 16px;
    background: rgba(255,255,255,.85);
    border: 1px solid rgba(255,255,255,.92);
    box-shadow: 0 16px 40px rgba(30, 70, 140, .10);
    display:grid;
    place-items:center;
    z-index: 12;
    cursor:pointer;
    user-select:none;
    animation: fall linear forwards;
    transform: translateX(-50%);
  }
  @keyframes fall{
    from{ transform: translateX(-50%) translateY(0) rotate(0deg); }
    to  { transform: translateX(-50%) translateY(120vh) rotate(12deg); }
  }

  /* Gift blast */
  .burst{
    position:fixed;
    width: 10px; height: 10px;
    border-radius: 999px;
    background: rgba(255,0,90,.85);
    box-shadow: 0 0 10px rgba(255,0,90,.35);
    pointer-events:none;
    z-index: 200;
    animation: burst .85s ease forwards;
  }
  @keyframes burst{
    from{ transform: translate(-50%,-50%) scale(.7); opacity: .95; }
    to  { transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0.2); opacity: 0; }
  }

  /* Memory overlay (light blue, not gray) */
  .overlay{
    position:fixed; inset:0;
    display:none;
    align-items:center; justify-content:center;
    background: rgba(200, 235, 255, .40);
    backdrop-filter: blur(10px);
    z-index: 80;
    padding: 18px;
  }
  .card{
    width: min(880px, 96vw);
    border-radius: 26px;
    background: rgba(255,255,255,.78);
    border: 1px solid rgba(255,255,255,.92);
    box-shadow: 0 22px 90px rgba(30, 70, 140, .16);
    overflow:hidden;
    transform: scale(.98);
    animation: pop .16s ease forwards;
  }
  @keyframes pop{ to{ transform: scale(1); } }

  .cardTop{
    display:flex; justify-content:space-between; align-items:center; gap:12px;
    padding: 12px 14px;
    background: rgba(255,255,255,.62);
    border-bottom: 1px solid rgba(255,255,255,.85);
  }
  .x{
    cursor:pointer;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,.92);
    background: rgba(255,255,255,.78);
    color: rgba(20,40,70,.92);
    padding: 8px 12px;
    font-weight: 950;
  }

  .cardBody{
    display:grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 14px;
    padding: 14px;
  }

  /* Medium photo + 3D tilt */
  .photo3d{
    position:relative;
    border-radius: 22px;
    transform-style: preserve-3d;
    perspective: 900px;
  }
  .midImg{
    width: 100%;
    height: clamp(270px, 42vh, 410px);
    object-fit: cover;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.92);
    background: rgba(255,255,255,.65);
    transform: translateZ(16px);
    box-shadow: 0 18px 55px rgba(30, 70, 140, .14);
    display:block;
  }
  .shine{
    position:absolute;
    inset:0;
    border-radius: 22px;
    background: radial-gradient(600px 220px at var(--mx,50%) var(--my,30%), rgba(255,0,90,.16), transparent 60%);
    mix-blend-mode: multiply;
    pointer-events:none;
    opacity:.75;
  }

  .info{ display:flex; flex-direction:column; gap:10px; }
  .date{
    width:fit-content;
    padding: 7px 10px;
    border-radius: 999px;
    background: rgba(255,255,255,.85);
    border: 1px solid rgba(255,255,255,.92);
    font-size: 12px;
    color: rgba(20,40,70,.78);
  }
  .head{ font-size: 24px; font-weight: 950; line-height: 1.08; color: rgba(20,40,70,.95); }
  .desc{ font-size: 14px; line-height: 1.6; color: rgba(30,60,90,.84); }

  @media (max-width: 860px){
    .cardBody{ grid-template-columns: 1fr; }
    .midImg{ height: clamp(250px, 36vh, 350px); }
  }

  /* --- Envelope Wish Modal --- */
  .wishBack{
    position:fixed; inset:0;
    display:none;
    align-items:center; justify-content:center;
    background: rgba(200,235,255,.38);
    backdrop-filter: blur(10px);
    z-index: 120;
    padding: 18px;
  }
  .envelope{
    width: min(560px, 94vw);
    border-radius: 26px;
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(255,255,255,.92);
    box-shadow: 0 24px 90px rgba(30,70,140,.18);
    overflow:hidden;
    transform: translateY(10px) scale(.98);
    animation: envPop .18s ease forwards;
  }
  @keyframes envPop{ to{ transform: translateY(0) scale(1); } }

  .envTop{
    padding: 12px 14px;
    display:flex; align-items:center; justify-content:space-between;
    background: rgba(255,255,255,.60);
    border-bottom: 1px solid rgba(255,255,255,.85);
  }
  .envTitle{
    font-weight: 950;
    color: rgba(20,40,70,.92);
    display:flex; gap:8px; align-items:center;
  }
  .envBody{
    padding: 16px 16px 18px;
  }
  .wishCard{
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(255,220,235,.60), rgba(255,255,255,.75));
    border: 1px solid rgba(255,255,255,.85);
    padding: 14px 14px;
    color: rgba(20,40,70,.90);
    box-shadow: 0 14px 40px rgba(30,70,140,.10);
  }
  .wishLine1{ font-weight: 950; font-size: 16px; }
  .wishLine2{ margin-top: 8px; font-size: 14px; line-height: 1.6; color: rgba(30,60,90,.84); }
</style>
</head>

<body>
<script>
  // Background hearts + sparkles
  const heartCount = 52;
  for(let i=0;i<heartCount;i++){
    const h = document.createElement("div");
    h.className = "heart";
    h.style.left = (Math.random()*100) + "vw";
    h.style.animationDuration = (6 + Math.random()*8) + "s";
    h.style.fontSize = (14 + Math.random()*20) + "px";
    h.style.setProperty("--dx", ((Math.random()*180)-90) + "px");
    h.style.animationDelay = (Math.random()*6) + "s";
    document.body.appendChild(h);
  }
  const sparkCount = 36;
  for(let i=0;i<sparkCount;i++){
    const s = document.createElement("div");
    s.className = "spark";
    s.style.left = (Math.random()*100) + "vw";
    s.style.top  = (Math.random()*100) + "vh";
    s.style.animationDuration = (2.0 + Math.random()*3.0) + "s";
    s.style.animationDelay = (Math.random()*2.5) + "s";
    document.body.appendChild(s);
  }
</script>

  <div class="hud">
    <div class="pill">
      <div class="title">💖 Meera ❤ Zeel</div>
      <div class="tiny" id="counter">0 opened</div>
    </div>
    <div class="pill">
      <div class="tiny" id="currentTiny">✈️ Love River Journey</div>
    </div>
  </div>

  <div class="wrap">
    <div class="map" id="map">
      <!-- River path -->
      <svg class="riverSvg" viewBox="0 0 100 100" preserveAspectRatio="none">
        <!-- under glow -->
        <path d="M50,5
                 C30,12 72,18 50,25
                 C28,32 74,40 52,48
                 C30,56 70,63 50,72
                 C30,80 72,88 50,95"
              fill="none" stroke="rgba(255,255,255,.65)" stroke-width="12" stroke-linecap="round"/>
        <!-- main river -->
        <path d="M50,5
                 C30,12 72,18 50,25
                 C28,32 74,40 52,48
                 C30,56 70,63 50,72
                 C30,80 72,88 50,95"
              fill="none" stroke="rgba(120, 190, 255, .58)" stroke-width="8" stroke-linecap="round"/>
        <!-- sparkle line -->
        <path d="M50,5
                 C30,12 72,18 50,25
                 C28,32 74,40 52,48
                 C30,56 70,63 50,72
                 C30,80 72,88 50,95"
              fill="none" stroke="rgba(255,255,255,.65)" stroke-width="1.3" stroke-dasharray="3 4" stroke-linecap="round"/>
      </svg>

      <div class="plane" id="plane">✈️</div>
      <div id="stopsLayer"></div>
      <div id="giftLayer"></div>
    </div>

    <div class="bar">
      <div>
        <div class="nowTitle" id="nowTitle">Current: —</div>
        <div class="nowSub" id="nowSub">Tap any stop or gifts 🎁</div>
      </div>
      <div class="tiny" id="miniNote">💌 Gifts give surprise wishes</div>
    </div>
  </div>

  <!-- Memory overlay -->
  <div class="overlay" id="overlay">
    <div class="card" id="card">
      <div class="cardTop">
        <div style="display:flex; gap:10px; align-items:center;">
          <div class="date" id="cDate"></div>
          <div style="font-weight:950; color:rgba(20,40,70,.90);" id="cSmall"></div>
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
          <div class="tiny" style="margin-top:auto;">(tap outside to close)</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Wish envelope modal -->
  <div class="wishBack" id="wishBack">
    <div class="envelope">
      <div class="envTop">
        <div class="envTitle">💌 Valentine Wish</div>
        <button class="x" id="wishClose">✕</button>
      </div>
      <div class="envBody">
        <div class="wishCard">
          <div class="wishLine1" id="wishL1">To Meera ❤ Zeel</div>
          <div class="wishLine2" id="wishL2">...</div>
        </div>
      </div>
    </div>
  </div>

<script>
  const STAGES = __PAYLOAD__;

  // Wishes for gifts
  const WISHES = [
    "Happy Valentine’s Day! 💖 You two are the cutest love story — keep choosing each other every day.",
    "Your bond feels like home 🏡💞. May your love stay soft, silly, and strong forever.",
    "To Meera ❤ Zeel: May your smiles stay in sync and your hearts stay in one team 💘",
    "Love is not perfect — it’s beautiful because you both try 💗 Happy Valentine’s Day!",
    "You both are the kind of couple that makes love look easy 😄💖 Stay happy always!",
    "A little drama, a lot of laughter, and infinite love 💞 That’s you two! Happy Valentine!",
    "From first meet to forever vibes ✨💘 Keep flying together!",
    "May your love be sweet like chocolate 🍫 and warm like hugs 🤗💗"
  ];

  // Save opened stops
  const KEY = "mz_love_river_v2";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));

  const counter = document.getElementById("counter");
  const nowTitle = document.getElementById("nowTitle");
  const nowSub = document.getElementById("nowSub");

  const stopsLayer = document.getElementById("stopsLayer");
  const giftLayer = document.getElementById("giftLayer");
  const plane = document.getElementById("plane");

  const overlay = document.getElementById("overlay");
  const closeBtn = document.getElementById("close");
  const cImg = document.getElementById("cImg");
  const cDate = document.getElementById("cDate");
  const cSmall = document.getElementById("cSmall");
  const cHead = document.getElementById("cHead");
  const cDesc = document.getElementById("cDesc");

  const photo3d = document.getElementById("photo3d");
  const shine = document.getElementById("shine");

  const wishBack = document.getElementById("wishBack");
  const wishClose = document.getElementById("wishClose");
  const wishL1 = document.getElementById("wishL1");
  const wishL2 = document.getElementById("wishL2");

  // Stop positions (vertical river)
  const POS = [
    {x:50, y:8},
    {x:40, y:15},
    {x:58, y:22},
    {x:44, y:30},
    {x:62, y:38},
    {x:48, y:46},
    {x:64, y:54},
    {x:46, y:62},
    {x:60, y:70},
    {x:45, y:78},
    {x:62, y:86},
    {x:50, y:93},
    {x:55, y:97},
  ].slice(0, STAGES.length);

  let idx = 0;
  let anim = null;

  function updateCounter(){
    counter.textContent = `${opened.size} / ${STAGES.length} opened`;
  }
  function save(){
    localStorage.setItem(KEY, JSON.stringify(Array.from(opened)));
    updateCounter();
  }
  function setActiveStop(i){
    [...stopsLayer.querySelectorAll(".stop")].forEach((b, j)=>{
      b.classList.toggle("active", j === i);
    });
  }

  function closeMemory(){ overlay.style.display = "none"; }
  function openMemory(){
    const s = STAGES[idx];

    opened.add(s.id);
    save();

    const btn = stopsLayer.querySelectorAll(".stop")[idx];
    if(btn) btn.classList.add("opened");

    cImg.src = s.img || "";
    cDate.textContent = s.date;
    cSmall.textContent = `Stage ${idx+1} / ${STAGES.length}`;
    cHead.textContent = s.title;
    cDesc.textContent = s.desc;

    overlay.style.display = "flex";
  }

  closeBtn.addEventListener("click", closeMemory);
  overlay.addEventListener("click", (e)=>{ if(e.target === overlay) closeMemory(); });

  // Plane fly + delay open
  function flyTo(targetIdx, openAfter=false){
    targetIdx = Math.max(0, Math.min(STAGES.length-1, targetIdx));
    const from = POS[idx];
    const to = POS[targetIdx];

    if(anim) cancelAnimationFrame(anim);

    // Update current immediately
    idx = targetIdx;
    setActiveStop(idx);
    const s = STAGES[idx];
    nowTitle.textContent = `Current: Stop ${idx+1} — ${s.title}`;
    nowSub.textContent = s.date;

    // duration based on distance
    const dx = (to.x - from.x), dy = (to.y - from.y);
    const dist = Math.sqrt(dx*dx + dy*dy);
    const dur = Math.min(1200, Math.max(650, dist * 26));
    const start = performance.now();
    const ease = (t) => 1 - Math.pow(1 - t, 3);
    const arc = Math.max(1.8, Math.min(6, dist/5));

    function step(now){
      const t = Math.min(1, (now - start) / dur);
      const e = ease(t);
      const x = from.x + (to.x - from.x) * e;
      const y = from.y + (to.y - from.y) * e - Math.sin(Math.PI * e) * arc;

      plane.style.left = x + "%";
      plane.style.top  = y + "%";

      if(t < 1){
        anim = requestAnimationFrame(step);
      }else{
        plane.style.left = to.x + "%";
        plane.style.top  = to.y + "%";
        if(openAfter){
          setTimeout(()=> openMemory(), 260);
        }
      }
    }
    anim = requestAnimationFrame(step);
  }

  // Build stops
  function buildStops(){
    stopsLayer.innerHTML = "";
    STAGES.forEach((s, i)=>{
      const p = POS[i];
      const b = document.createElement("div");
      b.className = "stop" + (opened.has(s.id) ? " opened" : "");
      b.style.left = p.x + "%";
      b.style.top  = p.y + "%";
      b.innerHTML = `
        <div class="hint">${s.date} • ${s.title}</div>
        <div class="n">${i+1}</div>
      `;
      b.addEventListener("click", ()=>{
        closeMemory();
        flyTo(i, true);
      });
      stopsLayer.appendChild(b);
    });
    updateCounter();
    setActiveStop(0);
  }

  // --- 3D tilt photo ---
  function resetTilt(){
    photo3d.style.transform = "rotateX(0deg) rotateY(0deg)";
    shine.style.setProperty("--mx", "50%");
    shine.style.setProperty("--my", "30%");
  }
  photo3d.addEventListener("mousemove", (e)=>{
    const r = photo3d.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width;
    const y = (e.clientY - r.top) / r.height;
    const rotY = (x - 0.5) * 14;
    const rotX = (0.5 - y) * 10;
    photo3d.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg)`;
    shine.style.setProperty("--mx", (x*100).toFixed(1) + "%");
    shine.style.setProperty("--my", (y*100).toFixed(1) + "%");
  });
  photo3d.addEventListener("mouseleave", resetTilt);

  // --- Gift wishes (envelope) ---
  function closeWish(){ wishBack.style.display = "none"; }
  function openWish(){
    const msg = WISHES[Math.floor(Math.random()*WISHES.length)];
    wishL1.textContent = "To Meera ❤ Zeel";
    wishL2.textContent = msg;
    wishBack.style.display = "flex";
  }
  wishClose.addEventListener("click", closeWish);
  wishBack.addEventListener("click", (e)=>{ if(e.target === wishBack) closeWish(); });

  function blastAt(clientX, clientY){
    // burst particles
    for(let i=0;i<18;i++){
      const p = document.createElement("div");
      p.className = "burst";
      p.style.left = clientX + "px";
      p.style.top  = clientY + "px";
      p.style.setProperty("--dx", ((Math.random()*260)-130) + "px");
      p.style.setProperty("--dy", ((Math.random()*220)-110) + "px");
      document.body.appendChild(p);
      setTimeout(()=> p.remove(), 900);
    }
  }

  // scattered gifts on map
  function buildStaticGifts(){
    giftLayer.innerHTML = "";
    const points = [
      {x:14, y:16}, {x:84, y:22}, {x:18, y:62}, {x:84, y:70}, {x:12, y:86}
    ];
    points.forEach((p)=>{
      const g = document.createElement("div");
      g.className = "gift";
      g.style.left = p.x + "%";
      g.style.top  = p.y + "%";
      g.innerHTML = `<div class="emoji">🎁</div>`;
      g.addEventListener("click", (e)=>{
        e.stopPropagation();
        blastAt(e.clientX, e.clientY);
        openWish();
      });
      giftLayer.appendChild(g);
    });
  }

  // falling gifts rain
  function spawnFallingGift(){
    const g = document.createElement("div");
    g.className = "giftFall";
    g.style.left = (Math.random()*100) + "vw";
    g.style.animationDuration = (4.6 + Math.random()*3.4) + "s";
    g.innerHTML = `<div style="font-size:22px;">🎁</div>`;
    g.addEventListener("click", (e)=>{
      e.stopPropagation();
      blastAt(e.clientX, e.clientY);
      openWish();
      g.remove();
    });
    document.body.appendChild(g);
    setTimeout(()=> g.remove(), 9000);
  }
  setInterval(spawnFallingGift, 1100);

  // Init
  buildStops();
  buildStaticGifts();

  // start plane at first stop
  plane.style.left = POS[0].x + "%";
  plane.style.top  = POS[0].y + "%";
  nowTitle.textContent = `Current: Stop 1 — ${STAGES[0].title}`;
  nowSub.textContent = STAGES[0].date;

  resetTilt();
  updateCounter();
</script>
</body>
</html>
"""

html = html.replace("__PAYLOAD__", payload_json)
st.components.v1.html(html, height=860, scrolling=False)
