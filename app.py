from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🎧 STATIONS
RADIO = {

    # NEWS
    "news": [
        "https://playerservices.streamtheworld.com/api/livestream-redirect/WINSAM.mp3"
    ],

    "bloomberg": [
        "https://playerservices.streamtheworld.com/api/livestream-redirect/WBBRAMAAC.aac"
    ],

    "wnyc": [
        "https://fm939.wnyc.org/wnycfm"
    ],

    # NYC MUSIC
    "z100": [
        "https://stream.revma.ihrhls.com/zc153"
    ],

    "hot97": [
        "https://stream.revma.ihrhls.com/zc142"
    ],

    "litefm": [
        "https://stream.revma.ihrhls.com/zc150"
    ],

    # 2000s
    "2000s_hits": [
        "https://listen.181fm.com/181-2000s_128k.mp3"
    ],

    "2000s_party": [
        "https://listen.181fm.com/181-party_128k.mp3"
    ],

    # CLASSIC
    "beatles": [
        "https://listen.181fm.com/181-beatles_128k.mp3"
    ],

    "disco": [
        "https://ice1.somafm.com/beatblender-128-mp3"
    ],

    # MODERN
    "bbc1": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one"
    ],

    "soma": [
        "https://ice1.somafm.com/groovesalad-128-mp3"
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
    overflow-x: hidden;

    font-family: Tahoma, Arial;

    background:
    linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.85)),
    url('https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&w=1600&q=80');

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
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image:
    linear-gradient(transparent, rgba(255,255,255,0.15));
    animation: rain 0.3s linear infinite;
}}

@keyframes rain {{
    from {{ background-position: 0 0; }}
    to {{ background-position: -20px 100px; }}
}}

.player {{
    width: 440px;

    background:
    linear-gradient(to bottom, #12296b, #07122d);

    border:
    3px solid #70c8ff;

    border-radius: 22px;

    padding: 18px;

    box-shadow:
    0 0 20px #0099ff,
    0 0 50px rgba(0,153,255,0.4);

    backdrop-filter: blur(8px);

    position: relative;
    z-index: 2;
}}

.topbar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.logo {{
    font-size: 24px;
    font-weight: bold;
    color: #7fd4ff;
    text-shadow: 0 0 10px #00aeff;
}}

.online {{
    color: #00ff88;
    font-size: 12px;
}}

.screen {{
    margin-top: 14px;

    background: black;

    border:
    2px solid #5ac8ff;

    border-radius: 12px;

    padding: 14px;

    box-shadow:
    inset 0 0 15px rgba(0,255,255,0.3);
}}

.nowplaying {{
    color: #00ffcc;
    font-size: 14px;
    margin-bottom: 10px;
}}

.visualizer {{
    display: flex;
    gap: 4px;
    align-items: flex-end;
    height: 50px;
}}

.bar {{
    width: 10px;
    border-radius: 4px;

    background:
    linear-gradient(to top, #00aaff, #00ff88);

    animation: move 1s infinite ease-in-out;
}}

.bar:nth-child(2) {{ animation-delay: .1s; }}
.bar:nth-child(3) {{ animation-delay: .2s; }}
.bar:nth-child(4) {{ animation-delay: .3s; }}
.bar:nth-child(5) {{ animation-delay: .4s; }}
.bar:nth-child(6) {{ animation-delay: .5s; }}
.bar:nth-child(7) {{ animation-delay: .6s; }}

@keyframes move {{
    0% {{ height: 12px; }}
    50% {{ height: 50px; }}
    100% {{ height: 18px; }}
}}

.cd {{
    width: 90px;
    height: 90px;

    margin: 16px auto;

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
    linear-gradient(to bottom, #39a7ff, #0050aa);

    border:
    2px solid #8fd8ff;

    border-radius: 14px;

    padding: 14px;

    text-align: center;

    cursor: pointer;

    transition: 0.2s;

    font-size: 14px;
    font-weight: bold;

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

    background: rgba(0,0,0,0.5);

    border-radius: 12px;

    padding: 10px;

    font-size: 12px;

    height: 80px;

    overflow: hidden;
}}

.msg {{
    margin-bottom: 4px;
}}

.ticker {{
    position: fixed;
    bottom: 0;
    width: 100%;
    background: #ffcc00;
    color: black;
    font-weight: bold;
    padding: 6px 0;
    overflow: hidden;
    white-space: nowrap;
}}

.ticker span {{
    display: inline-block;
    padding-left: 100%;
    animation: ticker 18s linear infinite;
}}

@keyframes ticker {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

audio {{
    width: 100%;
    margin-top: 14px;
}}

.footer {{
    margin-top: 12px;
    text-align: center;
    font-size: 10px;
    opacity: 0.5;
}}

</style>
</head>

<body>

<div class="rain"></div>

<div class="player">

<div class="topbar">
<div class="logo">📺 MTV RADIO 2003</div>
<div class="online">● online</div>
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

<div class="btn" onclick="play('news')">🗞 NEWS</div>
<div class="btn" onclick="play('bloomberg')">💰 MONEY</div>

<div class="btn" onclick="play('z100')">🔥 Z100</div>
<div class="btn" onclick="play('hot97')">🎤 HOT97</div>

<div class="btn" onclick="play('2000s_hits')">💿 2000s</div>
<div class="btn" onclick="play('2000s_party')">🪩 PARTY</div>

<div class="btn" onclick="play('beatles')">🎸 BEATLES</div>
<div class="btn" onclick="play('disco')">💃 ABBA</div>

<div class="btn" onclick="play('bbc1')">🇬🇧 BBC1</div>
<div class="btn" onclick="play('soma')">🌌 CHILL</div>

</div>

<div class="chat" id="chat">
<div class="msg">Ashley: omg this song 😭</div>
<div class="msg">Mike: hot97 still legendary</div>
<div class="msg">SYSTEM: connected from Brooklyn 🗽</div>
</div>

<audio id="audio" controls autoplay></audio>

<div class="footer">
WINAMP ENGINE READY • NYC WEATHER: rainy & dramatic 🌧
</div>

</div>

<div class="ticker">
<span>
BREAKING: someone downloaded linkin_park_final_REAL.mp3 • MTV actually plays music again • NYC subway running late as usual • Avril Lavigne spotted in 2003 • windows xp detected ⚠️
</span>
</div>

<script>

const jokes = [
    "finding signal in manhattan... 🗽",
    "DJ downloading mp3s from limewire 💿",
    "windows xp connection established 📺",
    "mtv still alive somehow 🎵",
    "late night brooklyn vibes 🌧",
    "loading 2003 internet energy ✨"
];

const chatMessages = [
    "Ashley: this track changed my life 😭",
    "Mike: hot97 goes hard",
    "SYSTEM: user connected from Queens",
    "Jenny: omg abba remix 💃",
    "Kevin: someone burn this to cd 💿",
    "SYSTEM: signal boosted from Manhattan"
];

function random(arr) {{
    return arr[Math.floor(Math.random() * arr.length)];
}}

setInterval(() => {{

    const chat = document.getElementById("chat");

    let div = document.createElement("div");

    div.className = "msg";

    div.innerText = random(chatMessages);

    chat.appendChild(div);

    if (chat.children.length > 5) {{
        chat.removeChild(chat.children[0]);
    }}

}}, 4000);


function play(station) {{

    const streams = {RADIO};

    document.getElementById("nowplaying").innerText =
    "NOW PLAYING: " + station.toUpperCase();

    let audio = document.getElementById("audio");

    let list = streams[station];

    let i = 0;

    function next() {{

        if (i >= list.length) return;

        audio.src = list[i];

        audio.play().catch(() => {{
            i++;
            next();
        }});

        let t = setTimeout(() => {{
            if (audio.readyState < 2) {{
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