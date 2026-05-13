from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🎧 Y2K / 2000s RADIO STATIONS
RADIO = {

    # 💿 2000s POP
    "2000s_pop": [
        "https://listen.181fm.com/181-2000s_128k.mp3"
    ],

    # 🎸 POP PUNK / ALT
    "pop_punk": [
        "https://listen.181fm.com/181-buzz_128k.mp3"
    ],

    # 🪩 PARTY
    "party": [
        "https://listen.181fm.com/181-party_128k.mp3"
    ],

    # 🌌 NIGHT DRIVE
    "night_drive": [
        "https://ice1.somafm.com/groovesalad-128-mp3"
    ],

    # 💃 DISCO / ABBA STYLE
    "disco": [
        "https://ice1.somafm.com/beatblender-128-mp3"
    ],

    # 🎤 HIP-HOP
    "hiphop": [
        "https://stream.revma.ihrhls.com/zc142"
    ],

    # 🌙 SOFT HITS
    "soft_hits": [
        "https://stream.revma.ihrhls.com/zc150"
    ],

    # 🇬🇧 UK HITS
    "uk_hits": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one"
    ]
}


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>MTV RADIO 2003</title>

<style>

body {{
    margin: 0;
    overflow: hidden;

    font-family: Tahoma, Arial;

    background:
    linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.88)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=1600&q=80');

    background-size: cover;
    background-position: center;

    color: white;

    display: flex;
    justify-content: center;
    align-items: center;

    min-height: 100vh;
}}

.rain {{
    position: fixed;
    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    pointer-events: none;
    overflow: hidden;
}}

.drop {{
    position: absolute;

    width: 2px;
    height: 80px;

    background:
    linear-gradient(transparent, rgba(255,255,255,0.4));

    animation: rain linear infinite;
}}

@keyframes rain {{

    from {{
        transform: translateY(-100px);
    }}

    to {{
        transform: translateY(100vh);
    }}
}}

.player {{
    width: 440px;

    background:
    linear-gradient(to bottom, #132b6d, #09122f);

    border:
    3px solid #67c8ff;

    border-radius: 22px;

    padding: 18px;

    box-shadow:
    0 0 25px #0099ff,
    0 0 70px rgba(0,153,255,0.4);

    backdrop-filter: blur(8px);

    position: relative;
    z-index: 10;
}}

.logo {{
    font-size: 24px;
    font-weight: bold;

    color: #8ad8ff;

    text-shadow:
    0 0 10px #00aaff;
}}

.top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.online {{
    color: #00ff88;
    font-size: 12px;
}}

.screen {{
    margin-top: 15px;

    background: black;

    border:
    2px solid #5ac8ff;

    border-radius: 12px;

    padding: 14px;

    box-shadow:
    inset 0 0 20px rgba(0,255,255,0.25);
}}

.nowplaying {{
    color: #00ffcc;
    margin-bottom: 10px;
    font-size: 14px;
}}

.visualizer {{
    display: flex;
    align-items: flex-end;
    gap: 4px;

    height: 50px;
}}

.bar {{
    width: 10px;

    border-radius: 4px;

    background:
    linear-gradient(to top, #00aaff, #00ff88);

    animation: bounce 1s infinite ease-in-out;
}}

.bar:nth-child(2) {{ animation-delay: .1s; }}
.bar:nth-child(3) {{ animation-delay: .2s; }}
.bar:nth-child(4) {{ animation-delay: .3s; }}
.bar:nth-child(5) {{ animation-delay: .4s; }}
.bar:nth-child(6) {{ animation-delay: .5s; }}
.bar:nth-child(7) {{ animation-delay: .6s; }}

@keyframes bounce {{
    0% {{ height: 10px; }}
    50% {{ height: 50px; }}
    100% {{ height: 16px; }}
}}

.cd {{
    width: 95px;
    height: 95px;

    margin: 18px auto;

    border-radius: 50%;

    background:
    radial-gradient(circle, #222 15%, #bbb 20%, #666 60%, #111 100%);

    border: 3px solid #ccc;

    animation: spin 3s linear infinite;

    box-shadow:
    0 0 20px rgba(255,255,255,0.4);
}}

@keyframes spin {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
}}

.grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}}

.btn {{
    background:
    linear-gradient(to bottom, #3daeff, #0050aa);

    border:
    2px solid #8fd8ff;

    border-radius: 14px;

    padding: 14px;

    cursor: pointer;

    text-align: center;

    font-size: 14px;
    font-weight: bold;

    transition: 0.2s;

    box-shadow:
    inset 0 0 10px rgba(255,255,255,0.2),
    0 0 10px rgba(0,136,255,0.5);
}}

.btn:hover {{
    transform: scale(1.05);
}}

.btn:active {{
    transform: scale(0.95);
}}

.chat {{
    margin-top: 14px;

    background: rgba(0,0,0,0.45);

    border-radius: 12px;

    padding: 10px;

    font-size: 12px;

    height: 80px;

    overflow: hidden;
}}

.msg {{
    margin-bottom: 4px;
}}

audio {{
    width: 100%;
    margin-top: 15px;

    filter: hue-rotate(180deg);
}}

.footer {{
    margin-top: 10px;
    text-align: center;
    font-size: 10px;
    opacity: 0.5;
}}

.ticker {{
    position: fixed;
    bottom: 0;
    left: 0;

    width: 100%;

    background: #00aaff;

    color: white;

    font-weight: bold;

    padding: 6px 0;

    overflow: hidden;
    white-space: nowrap;
}}

.ticker span {{
    display: inline-block;

    padding-left: 100%;

    animation: ticker 45s linear infinite;
}}

@keyframes ticker {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

</style>
</head>

<body>

<div class="rain" id="rain"></div>

<div class="player">

<div class="top">

<div class="logo">
📺 MTV RADIO 2003
</div>

<div class="online">
● online
</div>

</div>

<div class="screen">

<div class="nowplaying" id="nowplaying">
NOW PLAYING: waiting...
</div>

<div class="visualizer">
<div class="bar"></div>
<div class="bar"></div>
<div class="bar"></div>
<div class="bar"></div>
<div class="bar"></div>
<div class="bar"></div>
<div class="bar"></div>
</div>

</div>

<div class="cd"></div>

<div class="grid">

<div class="btn" onclick="play('2000s_pop')">
💿 POP 2000s
</div>

<div class="btn" onclick="play('pop_punk')">
🎸 POP PUNK
</div>

<div class="btn" onclick="play('party')">
🪩 PARTY
</div>

<div class="btn" onclick="play('night_drive')">
🌌 NIGHT DRIVE
</div>

<div class="btn" onclick="play('disco')">
💃 DISCO / ABBA
</div>

<div class="btn" onclick="play('hiphop')">
🎤 HIP-HOP
</div>

<div class="btn" onclick="play('soft_hits')">
🌙 SOFT HITS
</div>

<div class="btn" onclick="play('uk_hits')">
🇬🇧 UK HITS
</div>

</div>

<div class="chat" id="chat">

<div class="msg">
Ashley: omg this feels like 2004 😭
</div>

<div class="msg">
Mike: downloading mp3s rn 💿
</div>

<div class="msg">
SYSTEM: connected from Brooklyn 🌧
</div>

</div>

<audio id="audio" controls autoplay></audio>

<div class="footer">
windows xp connection established 📺
</div>

</div>

<div class="ticker">
<span>

BREAKING: someone burned Avril Lavigne onto CD-R 💿 •
MTV accidentally played actual music 📺 •
MySpace top friends drama escalating ⚠️ •
Limewire virus detected again 🦠 •
Green Day dominating every teenager playlist 🎸 •
SYSTEM: windows xp running smoothly somehow 💻 •
Fall Out Boy spotted in Brooklyn 👀 •
emo levels dangerously high tonight 🖤 •
someone downloaded linkin_park_final_REAL.mp3 •
MSN Messenger status changed to "away" 💬 •
punk music heard from Queens subway 🚇 •
Britney Spears on every screen again ✨ •
scene kids gathering near Times Square 🌧 •
SYSTEM: too much 2004 energy detected ⚡ •
Paramore songs causing emotional damage 😭 •
late night Manhattan radio transmission active 📡 •
iPod battery critically low 🔋 •
Hot Topic sales increased dramatically 🛍 •
skateboarders seen near downtown NYC 🛹 •
CD player anti-skip protection failed 💀 •
MTV VMA chaos returning tonight 🪩 •
dashboard confessional detected in headphones 🎧 •
Avril Lavigne still refusing to dress normally 🧷 •
SYSTEM ERROR: nostalgia overload 💿

</span>
</div>

<script>

// 🌧 RAIN
for(let i = 0; i < 120; i++) {{

    let drop = document.createElement("div");

    drop.className = "drop";

    drop.style.left =
    Math.random() * window.innerWidth + "px";

    drop.style.animationDuration =
    (0.4 + Math.random()) + "s";

    drop.style.opacity = Math.random();

    document.getElementById("rain").appendChild(drop);
}}

// 💬 CHAT
const messages = [

    "Ashley: this song ruined my life 😭",
    "SYSTEM: someone online from Queens",
    "Mike: hot topic vibes 🎸",
    "Jenny: this belongs on MTV",
    "Kevin: burn this to cd NOW 💿",
    "SYSTEM: signal boosted from Manhattan",
    "emo kid detected near Brooklyn 🖤",
    "someone still uses iTunes 👀",
    "MSN status changed to invisible 💬"

];

setInterval(() => {{

    let div = document.createElement("div");

    div.className = "msg";

    div.innerText =
    messages[Math.floor(Math.random()*messages.length)];

    let chat = document.getElementById("chat");

    chat.appendChild(div);

    if(chat.children.length > 5) {{
        chat.removeChild(chat.children[0]);
    }}

}}, 4000);


// 🎧 PLAYER
function play(station) {{

    const streams = {RADIO};

    document.getElementById("nowplaying").innerText =
    "NOW PLAYING: " + station.toUpperCase();

    let audio = document.getElementById("audio");

    let list = streams[station];

    let i = 0;

    function next() {{

        if(i >= list.length) return;

        audio.src = list[i];

        audio.play().catch(() => {{
            i++;
            next();
        }});

        let t = setTimeout(() => {{

            if(audio.readyState < 2) {{
                i++;
                next();
            }}

        }}, 4000);

        audio.onplaying = () => clearTimeout(t);
    }}

    next();
}}

</script>

</body>
</html>
"""


@app.route("/alice", methods=["POST"])
def alice():
    return jsonify({
        "response": {
            "text": "MTV Radio 2003 работает",
            "end_session": False
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)