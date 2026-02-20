import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Meera ❤ Zeel — Valentine Journey", layout="wide")

ASSETS = Path(__file__).parent / "assets"

def to_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    ext = path.suffix.lower().replace(".", "")
    mime = "png" if ext == "png" else "jpeg"
    return f"data:image/{mime};base64," + base64.b64encode(path.read_bytes()).decode()

# -----------------------
# STAGES (EDIT ONLY THIS IF NEEDED)
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

st.markdown("## 💖 Meera ❤ Zeel — Valentine Journey (Decorative Pink Theme)")

# -----------------------
# FULL FRONTEND (HTML/CSS/JS)
# -----------------------
html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  :root {{
    --glass: rgba(255,255,255,.18);
    --stroke: rgba(255,255,255,.25);
    --text: rgba(255,255,255,.95);
    --muted: rgba(255,255,255,.78);
    --shadow: 0 18px 60px rgba(0,0,0,.35);
    --radius: 22px;
  }}
  *{{ box-sizing:border-box; }}
  body {{
    margin:0;
    overflow:hidden;
    font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial;
    color: var(--text);
    background: linear-gradient(135deg, #ffb3d9, #ff5fa2, #ff2d87);
  }}

  /* Decorative glow */
  .glow {{
    position: fixed; inset: -120px;
    background:
      radial-gradient(900px 500px at 15% 15%, rgba(255,255,255,.20), transparent 60%),
      radial-gradient(900px 500px at 85% 25%, rgba(255,255,255,.14), transparent 60%),
      radial-gradient(1200px 700px at 50% 90%, rgba(0,0,0,.20), transparent 65%);
    z-index:-2;
    pointer-events:none;
    filter: blur(10px);
  }}

  /* Floating hearts */
  .heart {{
    position: fixed;
    bottom: -20px;
    font-size: 18px;
    opacity: .0;
    animation: floatUp linear infinite;
    z-index: -1;
    filter: drop-shadow(0 10px 18px rgba(0,0,0,.25));
  }}
  @keyframes floatUp {{
    0%   {{ transform: translateY(0) scale(.6) rotate(0deg); opacity: 0; }}
    10%  {{ opacity: .85; }}
    100% {{ transform: translateY(-120vh) scale(1.25) rotate(20deg); opacity: 0; }}
  }}

  /* Sparkles */
  .spark {{
    position: fixed;
    width: 6px; height: 6px;
    border-radius: 999px;
    background: rgba(255,255,255,.9);
    opacity: .0;
    animation: twinkle ease-in-out infinite;
    z-index:-1;
  }}
  @keyframes twinkle {{
    0%,100% {{ transform: scale(.6); opacity: .0; }}
    40%     {{ opacity: .85; }}
    60%     {{ transform: scale(1.25); opacity: .95; }}
  }}

  /* HUD */
  .hud {{
    position: fixed; left: 14px; right: 14px; top: 10px;
    z-index: 20;
    display:flex; justify-content:space-between; gap: 10px; align-items:center;
  }}
  .pill {{
    backdrop-filter: blur(12px);
    background: rgba(255,255,255,.18);
    border: 1px solid rgba(255,255,255,.26);
    border-radius: 999px;
    padding: 10px 14px;
    box-shadow: 0 10px 30px rgba(0,0,0,.22);
    display:flex; gap:10px; align-items:center;
    min-height: 42px;
    white-space: nowrap;
  }}
  .title {{ font-weight: 900; letter-spacing: .2px; }}
  .tiny  {{ font-size: 12px; color: var(--muted); }}

  .btn {{
    cursor:pointer; user-select:none;
    border: 1px solid rgba(255,255,255,.28);
    background: rgba(255,255,255,.14);
    color: var(--text);
    padding: 9px 12px;
    border-radius: 999px;
    font-weight: 800;
    transition: transform .12s ease, background .12s ease;
  }}
  .btn:hover {{ background: rgba(255,255,255,.22); }}
  .btn:active {{ transform: scale(.98); }}

  /* Wrap */
  .wrap {{
    position: fixed; inset: 0;
    padding-top: 72px;
    padding-bottom: 14px;
    display:flex; flex-direction:column;
  }}

  /* Progress track */
  .track {{
    margin: 0 14px;
    height: 10px;
    border-radius: 999px;
    background: rgba(255,255,255,.22);
    border: 1px solid rgba(255,255,255,.28);
    position: relative;
    overflow: hidden;
  }}
  .progress {{
    height: 100%;
    width: 0%;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(255,255,255,.75), rgba(255,255,255,.40));
    transition: width .55s ease;
  }}
  .plane {{
    position:absolute;
    top: 50%;
    left: 0%;
    transform: translate(-10px,-50%);
    transition: left .55s ease;
    font-size: 18px;
    filter: drop-shadow(0 6px 14px rgba(0,0,0,.35));
  }}

  /* Horizontal journey */
  .journey {{
    flex: 1;
    margin-top: 12px;
    overflow-x: auto;
    overflow-y: hidden;
    scroll-snap-type: x mandatory;
    display:flex;
    gap: 16px;
    padding: 10px 14px 18px;
    -webkit-overflow-scrolling: touch;
  }}
  .journey::-webkit-scrollbar {{ height: 10px; }}
  .journey::-webkit-scrollbar-thumb {{
    background: rgba(255,255,255,.35);
    border-radius: 999px;
  }}

  .stage {{
    scroll-snap-align: start;
    min-width: min(86vw, 420px);
    max-width: 420px;
    height: 100%;
    border-radius: var(--radius);
    backdrop-filter: blur(14px);
    background: rgba(255,255,255,.16);
    border: 1px solid rgba(255,255,255,.28);
    box-shadow: var(--shadow);
    position: relative;
    overflow: hidden;
    padding: 16px;
    display:flex;
    flex-direction: column;
    gap: 10px;
  }}

  .row {{
    display:flex;
    align-items:flex-start;
    justify-content: space-between;
    gap: 12px;
  }}

  .badge {{
    font-size: 12px;
    background: rgba(255,255,255,.18);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 999px;
    padding: 6px 10px;
    color: rgba(255,255,255,.92);
    width: fit-content;
  }}

  .stage h2 {{
    margin: 6px 0 0;
    font-size: 20px;
    line-height: 1.15;
    letter-spacing: .2px;
  }}
  .stage p {{
    margin: 0;
    color: rgba(255,255,255,.82);
    font-size: 13px;
    line-height: 1.5;
  }}

  /* Gift + effects */
  .giftArea {{
    margin-top: 6px;
    display:flex;
    align-items:center;
    justify-content:center;
    position: relative;
    min-height: 230px;
  }}

  .giftBtn {{
    position: relative;
    width: 168px;
    height: 168px;
    border: 0;
    background: transparent;
    cursor: pointer;
    filter: drop-shadow(0 18px 28px rgba(0,0,0,.35));
  }}

  .gift {{
    width: 100%;
    height: 100%;
    position: relative;
    transform-origin: center;
  }}

  .boxBase {{
    position:absolute;
    left: 20px; right: 20px;
    bottom: 18px;
    height: 92px;
    border-radius: 16px;
    background: rgba(255,255,255,.22);
    border: 1px solid rgba(255,255,255,.30);
  }}
  .boxLid {{
    position:absolute;
    left: 14px; right: 14px;
    bottom: 88px;
    height: 54px;
    border-radius: 16px;
    background: rgba(255,255,255,.26);
    border: 1px solid rgba(255,255,255,.30);
    transform-origin: left bottom;
    transition: transform .6s cubic-bezier(.2,.9,.2,1);
  }}
  .ribbonV {{
    position:absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: 18px;
    width: 20px;
    height: 124px;
    border-radius: 999px;
    background: rgba(255,255,255,.85);
    opacity: .92;
  }}
  .ribbonH {{
    position:absolute;
    left: 20px; right: 20px;
    bottom: 58px;
    height: 20px;
    border-radius: 999px;
    background: rgba(255,255,255,.85);
    opacity: .92;
  }}
  .bow {{
    position:absolute;
    left: 50%;
    bottom: 124px;
    transform: translateX(-50%);
    width: 58px;
    height: 32px;
    display:flex; gap: 6px;
    align-items:center;
    justify-content:center;
  }}
  .bow span {{
    width: 26px; height: 22px;
    border-radius: 999px 999px 999px 6px;
    background: rgba(255,255,255,.90);
    transform: rotate(12deg);
    border: 1px solid rgba(255,255,255,.22);
  }}
  .bow span:last-child {{
    border-radius: 999px 999px 6px 999px;
    transform: rotate(-12deg);
  }}

  .opened .boxLid {{ transform: rotate(-52deg) translate(-6px,-8px); }}

  .burstLayer {{
    position:absolute; inset:0;
    pointer-events:none;
    overflow:hidden;
  }}
  .balloon {{
    position:absolute;
    bottom: -40px;
    width: 24px; height: 30px;
    border-radius: 999px;
    background: rgba(255,255,255,.95);
    filter: drop-shadow(0 10px 18px rgba(0,0,0,.25));
    animation: floatB 1.5s ease forwards;
    opacity:.95;
  }}
  .balloon::after {{
    content:"";
    position:absolute;
    left: 50%;
    bottom: -18px;
    width: 1px;
    height: 22px;
    background: rgba(255,255,255,.75);
    transform: translateX(-50%);
    opacity:.75;
  }}
  @keyframes floatB {{
    from{{ transform: translateY(0) translateX(0); opacity: .95; }}
    to{{ transform: translateY(-260px) translateX(var(--dx)); opacity: 0; }}
  }}

  .conf {{
    position:absolute;
    width: 8px; height: 12px;
    background: rgba(255,255,255,.95);
    top: 45%;
    left: 50%;
    transform: translate(-50%,-50%);
    animation: confetti 1.1s ease forwards;
    opacity:.95;
  }}
  @keyframes confetti {{
    from{{ transform: translate(-50%,-50%) rotate(0deg); }}
    to{{ transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) rotate(540deg); opacity: 0; }}
  }}

  /* Modal */
  .modalBack {{
    position:fixed; inset:0;
    display:none;
    z-index: 60;
    background: rgba(0,0,0,.48);
    backdrop-filter: blur(7px);
    align-items:center;
    justify-content:center;
    padding: 18px;
  }}
  .modal {{
    width: min(560px, 96vw);
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.25);
    background: rgba(255,255,255,.14);
    box-shadow: 0 30px 90px rgba(0,0,0,.55);
    overflow:hidden;
  }}
  .modalTop {{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    padding: 12px 14px;
    background: rgba(255,255,255,.14);
    border-bottom: 1px solid rgba(255,255,255,.18);
  }}
  .closeBtn {{
    border:1px solid rgba(255,255,255,.25);
    background: rgba(255,255,255,.16);
    color: var(--text);
    padding: 8px 10px;
    border-radius: 999px;
    cursor:pointer;
    font-weight: 900;
  }}
  .modalBody {{
    padding: 14px;
    display:flex;
    gap: 12px;
    align-items:flex-start;
  }}
  .modalImg {{
    width: 150px;
    height: 150px;
    border-radius: 20px;
    object-fit: cover;
    border: 1px solid rgba(255,255,255,.22);
    background: rgba(255,255,255,.10);
  }}
  .modalText {{
    display:flex;
    flex-direction:column;
    gap: 6px;
    min-width: 0;
  }}
  .modalText .d {{ font-size: 12px; color: rgba(255,255,255,.80); }}
  .modalText .t {{ font-size: 18px; font-weight: 900; line-height: 1.1; }}
  .modalText .p {{ font-size: 13px; color: rgba(255,255,255,.90); line-height: 1.45; }}
</style>
</head>

<body>
  <div class="glow"></div>

  <div class="hud">
    <div class="pill">
      <div class="title">💝 Open gifts to unlock memories</div>
      <div class="tiny" id="counter">0 / {len(payload)} opened</div>
    </div>
    <div class="pill">
      <button class="btn" id="left">⬅️</button>
      <button class="btn" id="right">➡️</button>
      <button class="btn" id="reset">Reset</button>
    </div>
  </div>

  <div class="wrap">
    <div class="track">
      <div class="progress" id="progress"></div>
      <div class="plane" id="plane">🛫</div>
    </div>

    <div class="journey" id="journey"></div>
  </div>

  <div class="modalBack" id="modalBack">
    <div class="modal">
      <div class="modalTop">
        <b>Unlocked Memory 💖</b>
        <button class="closeBtn" id="close">✕</button>
      </div>
      <div class="modalBody">
        <img class="modalImg" id="mImg" src="" alt="memory"/>
        <div class="modalText">
          <div class="d" id="mDate"></div>
          <div class="t" id="mHead"></div>
          <div class="p" id="mDesc"></div>
        </div>
      </div>
    </div>
  </div>

<script>
  // --- Generate floating hearts + sparkles ---
  const heartIcons = ["❤","💗","💖","💞","💕"];
  for(let i=0;i<26;i++){
    const h = document.createElement("div");
    h.className = "heart";
    h.style.left = (Math.random()*100) + "vw";
    h.style.animationDuration = (6 + Math.random()*7) + "s";
    h.style.fontSize = (14 + Math.random()*16) + "px";
    h.style.opacity = (0.25 + Math.random()*0.65).toFixed(2);
    h.innerHTML = heartIcons[Math.floor(Math.random()*heartIcons.length)];
    document.body.appendChild(h);
  }
  for(let i=0;i<28;i++){
    const s = document.createElement("div");
    s.className = "spark";
    s.style.left = (Math.random()*100) + "vw";
    s.style.top = (Math.random()*100) + "vh";
    s.style.animationDuration = (2.2 + Math.random()*3.5) + "s";
    s.style.animationDelay = (Math.random()*2.5) + "s";
    document.body.appendChild(s);
  }

  // Data
  const STAGES = {payload};

  // Local progress
  const KEY = "mz_pink_valentine_opened_v1";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));

  const journey = document.getElementById("journey");
  const counter = document.getElementById("counter");
  const progress = document.getElementById("progress");
  const plane = document.getElementById("plane");

  function save(){
    localStorage.setItem(KEY, JSON.stringify(Array.from(opened)));
    updateHUD();
  }

  function updateHUD(){
    const total = STAGES.length;
    const n = opened.size;
    counter.textContent = `${n} / ${total} opened`;
    const pct = total === 0 ? 0 : Math.round((n/total)*100);
    progress.style.width = pct + "%";
    plane.style.left = pct + "%";
    plane.textContent = pct >= 100 ? "🛬" : (pct >= 60 ? "✈️" : "🛫");
  }

  function rand(min,max){ return Math.random()*(max-min)+min; }

  function celebrate(layer){
    layer.innerHTML = "";
    for(let i=0;i<10;i++){
      const b = document.createElement("div");
      b.className = "balloon";
      b.style.left = rand(8,92) + "%";
      b.style.setProperty("--dx", rand(-60,60) + "px");
      layer.appendChild(b);
    }
    for(let i=0;i<18;i++){
      const c = document.createElement("div");
      c.className = "conf";
      c.style.left = rand(35,65) + "%";
      c.style.top = rand(35,55) + "%";
      c.style.setProperty("--dx", rand(-180,180) + "px");
      c.style.setProperty("--dy", rand(-160,160) + "px");
      layer.appendChild(c);
    }
    setTimeout(()=> layer.innerHTML="", 1600);
  }

  // Modal
  const modalBack = document.getElementById("modalBack");
  const closeBtn = document.getElementById("close");
  const mImg = document.getElementById("mImg");
  const mDate = document.getElementById("mDate");
  const mHead = document.getElementById("mHead");
  const mDesc = document.getElementById("mDesc");

  function openModal(s){
    mImg.src = s.img || "";
    mDate.textContent = s.date;    // date shown here only
    mHead.textContent = s.title;
    mDesc.textContent = s.desc;
    modalBack.style.display = "flex";
  }
  function closeModal(){ modalBack.style.display="none"; }
  closeBtn.addEventListener("click", closeModal);
  modalBack.addEventListener("click", (e)=>{ if(e.target === modalBack) closeModal(); });

  function stageCard(s, idx){
    const card = document.createElement("div");
    card.className = "stage";
    card.innerHTML = `
      <div class="row">
        <div>
          <div class="badge">Stage ${idx+1} / ${STAGES.length}</div>
          <h2>${s.title}</h2>
          <p>${s.desc}</p>
        </div>
        <div class="badge">${s.date}</div>
      </div>

      <div class="giftArea">
        <button class="giftBtn" aria-label="Open gift">
          <div class="gift ${opened.has(s.id) ? "opened" : ""}">
            <div class="boxLid"></div>
            <div class="boxBase"></div>
            <div class="ribbonV"></div>
            <div class="ribbonH"></div>
            <div class="bow"><span></span><span></span></div>
          </div>
        </button>
        <div class="burstLayer"></div>
      </div>
    `;

    const btn = card.querySelector(".giftBtn");
    const gift = card.querySelector(".gift");
    const burst = card.querySelector(".burstLayer");

    btn.addEventListener("click", ()=>{
      celebrate(burst);

      if(!opened.has(s.id)){
        opened.add(s.id);
        gift.classList.add("opened");
        save();
      }
      openModal(s);

      setTimeout(()=> journey.scrollBy({left: 320, behavior:"smooth"}), 500);
    });

    return card;
  }

  function build(){
    journey.innerHTML = "";
    STAGES.forEach((s,i)=> journey.appendChild(stageCard(s,i)));
    updateHUD();
  }

  document.getElementById("left").addEventListener("click", ()=> journey.scrollBy({left:-360, behavior:"smooth"}));
  document.getElementById("right").addEventListener("click", ()=> journey.scrollBy({left:360, behavior:"smooth"}));
  document.getElementById("reset").addEventListener("click", ()=>{
    localStorage.removeItem(KEY);
    opened = new Set();
    build();
  });

  build();
</script>
</body>
</html>
"""

st.components.v1.html(html, height=800, scrolling=False)
st.caption("✅ Date is NOT written on photos. Date is shown only in the UI (badge + popup).")
