from flask import Flask
import os

app = Flask(__name__)

# 🎧 BIG STABLE RADIO BANK (2000s / 2010 vibes)
RADIO = {
    "MTV POP 2003": "https://ice1.somafm.com/poptron-128-mp3",
    "MYSPACE INDIE": "https://ice1.somafm.com/indiepop-128-mp3",
    "POP PUNK ERA": "https://ice1.somafm.com/punkrockers-128-mp3",
    "DANCE 2005 CLUB": "https://ice1.somafm.com/beatblender-128-mp3",
    "CHILL NIGHT NYC": "https://ice1.somafm.com/groovesalad-128-mp3",
    "RNB SLOW JAMZ": "https://ice1.somafm.com/smoothjazz-128-mp3",
    "ELECTRO BLOG ERA": "https://ice1.somafm.com/dubstep-128-mp3",
    "UK CHART POP": "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one"
}


@app.route("/")
def home():

    buttons = ""
    for k in RADIO:
        buttons += f"<div class='btn' onclick=\"play('{k}')\">✨ {k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>MYSPACE XP MTV SIMULATOR</title>

<style>

/* 🌌 FULL 2000s GLAM BACKGROUND */
body {{
    margin: 0;
    font-family: Tahoma, Arial;
    background:
    radial-gradient(circle at top, #ff4fd8, #000),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    overflow: hidden;
    color: white;
}}

/* 🪟 DESKTOP LAYER */
.desktop {{
    display: flex;
    height: 100vh;
}}

/* 💖 MYSPACE SIDEBAR */
.sidebar {{
    width: 280px;
    background: rgba(0,0,0,0.65);
    border-right: 2px solid #ff4fd8;
    padding: 10px;
    backdrop-filter: blur(8px);
}}

.btn {{
    background: linear-gradient(45deg, #ff4fd8, #7a5cff);
    padding: 10px;
    margin: 6px 0;
    cursor: pointer;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    box-shadow: 0 0 10px #ff4fd8;
}}

.btn:hover {{
    transform: scale(1.06);
    box-shadow: 0 0 20px #ff4fd8;
}}

/* 🎧 MAIN PLAYER */
.main {{
    flex: 1;
    padding: 20px;
    position: relative;
}}

.player {{
    width: 560px;
    background: rgba(0,0,0,0.8);
    border: 2px solid #ff4fd8;
    padding: 15px;
    border-radius: 18px;
    box-shadow: 0 0 25px #ff4fd8;
}}

audio {{
    width: 100%;
    margin-top: 10px;
}}

/* 💬 MSN / AIM CHAT */
.chat {{
    margin-top: 10px;
    height: 200px;
    overflow: hidden;
    background: rgba(0,0,0,0.85);
    padding: 10px;
    border: 1px solid #7a5cff;
    font-size: 12px;
}}

.msg {{
    margin: 4px 0;
    padding: 4px;
    color: #fff;
    background: rgba(255,255,255,0.05);
    border-radius: 6px;
}}

/* 🟡 MTV BREAKING NEWS */
.news {{
    position: fixed;
    top: 0;
    width: 100%;
    background: linear-gradient(90deg, #ff4fd8, #7a5cff);
    color: white;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
}}

.news span {{
    display: inline-block;
    padding-left: 100%;
    animation: move 16s linear infinite;
}}

@keyframes move {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

/* ✨ GLITTER OVERLAY */
.glitter {{
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: radial-gradient(white 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0.12;
}}

/* 💿 FLOATING "MYSPACE CARD" */
.card {{
    position: absolute;
    right: 30px;
    top: 120px;
    width: 220px;
    background: rgba(255,0,255,0.15);
    border: 1px dashed #ff4fd8;
    padding: 10px;
    font-size: 11px;
}}

.online {{
    color: lime;
    animation: blink 1s infinite;
}}

@keyframes blink {{
    0% {{ opacity: 1; }}
    50% {{ opacity: 0.4; }}
    100% {{ opacity: 1; }}
}}

</style>
</head>

<body>

<div class="glitter"></div>

<!-- 🟡 MTV NEWS -->
<div class="news">
<span>
BREAKING: Britney Spears dominates Y2K charts • MySpace TOP FRIENDS return • MTV 2003 countdown restored • Winamp skins trending globally • Limewire nostalgia spike • CD burning culture revived • Nokia ringtone fashion back • Paris Hilton era resurfacing • Avril Lavigne takeover continues • MSN Messenger servers simulated online •
</span>
</div>

<div class="desktop">

<!-- 💖 SIDEBAR -->
<div class="sidebar">
<h3>💿 RADIO STATIONS</h3>
{buttons}

<div style="margin-top:10px" class="online">
● MSN STATUS: ONLINE
</div>
</div>

<!-- 🎧 MAIN -->
<div class="main">

<div class="player">

<h2 id="now">SELECT A STATION</h2>

<audio id="audio" controls></audio>

<div class="chat" id="chat">
<div class="msg">SYSTEM: MYSPACE XP ONLINE 💖</div>
<div class="msg">DJ: welcome to glam internet era ✨</div>
<div class="msg">Ashley: this is literally 2005 😭</div>
</div>

</div>

</div>

<!-- 💿 MYSPACE CARD -->
<div class="card">
<b>💖 TOP FRIENDS</b><br><br>
Paris Hilton<br>
Britney Spears<br>
Avril Lavigne<br>
Blink-182<br><br>
<span style="color:lime">STATUS: ONLINE</span>
</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 PLAY */
function play(station) {{
    const audio = document.getElementById("audio");
    document.getElementById("now").innerText = "💖 NOW PLAYING: " + station;

    audio.src = streams[station];
    audio.play().catch(()=>{{}});
}}

/* 💬 ULTRA 2000s CHAT SYSTEM */
const chatLines = [
    "Ashley: OMG Britney era is BACK 💖",
    "Mike: burning CDs with glitter covers ✨",
    "DJ: MTV countdown vibes live 🔥",
    "SYSTEM: MSN Messenger connected",
    "Emma: MySpace profile editing rn",
    "Jake: Limewire downloading chaos 💀",
    "Tom: Nokia ringtone culture",
    "Lisa: Avril Lavigne domination",
    "NYC: signal stable 🗽",
    "Paris: it's all about glam ✨"
];

setInterval(() => {{
    const chat = document.getElementById("chat");

    const div = document.createElement("div");
    div.className = "msg";

    div.innerText = chatLines[Math.floor(Math.random()*chatLines.length)];

    chat.appendChild(div);

    if(chat.children.length > 11) {{
        chat.removeChild(chat.children[0]);
    }}

}}, 1400);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "FULL MYSPACE XP MTV SIMULATOR ACTIVE", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)