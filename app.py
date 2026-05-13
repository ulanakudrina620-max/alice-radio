from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🎧 ULTRA-STABLE RADIO (fallback chains)
RADIO = {
    "2001": [
        "https://ice1.somafm.com/indiepop-128-mp3",
        "https://ice2.somafm.com/indiepop-128-mp3"
    ],
    "2005": [
        "https://ice1.somafm.com/poptron-128-mp3",
        "https://ice1.somafm.com/beatblender-128-mp3",
        "https://ice2.somafm.com/poptron-128-mp3"
    ],
    "2009": [
        "https://ice1.somafm.com/punkrockers-128-mp3",
        "https://ice1.somafm.com/groovesalad-128-mp3"
    ]
}


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>MTV ULTIMATE TIME MACHINE</title>

<style>

body {{
    margin: 0;
    font-family: Tahoma, Arial;
    background:
    linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    background-position: center;
    height: 100vh;
    overflow: hidden;
}}

.window {{
    display: flex;
    flex-direction: column;
    height: 100vh;
}}

.topbar {{
    height: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    background: linear-gradient(to right, #0b2a6f, #1a5cff);
    color: white;
    font-weight: bold;
}}

.main {{
    flex: 1;
    display: flex;
    padding: 20px;
    gap: 20px;
}}

.sidebar {{
    width: 260px;
    background: rgba(0,0,0,0.6);
    border-radius: 12px;
    padding: 15px;
}}

.btn {{
    background: linear-gradient(to bottom, #3daeff, #0050aa);
    border: 1px solid #7fd4ff;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    color: white;
}}

.btn:hover {{
    transform: scale(1.03);
}}

.player {{
    flex: 1;
    background: rgba(0,0,0,0.7);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
}}

.screen {{
    background: black;
    border: 1px solid #5ac8ff;
    border-radius: 10px;
    padding: 15px;
    height: 130px;
    color: #00ffcc;
}}

.nowplaying {{
    font-size: 14px;
}}

.status {{
    font-size: 12px;
    opacity: 0.7;
    margin-top: 5px;
}}

audio {{
    width: 100%;
    margin-top: 10px;
}}

/* 💬 CHAT */
.chat {{
    margin-top: 15px;
    background: rgba(10,10,25,0.95);
    border-radius: 12px;
    padding: 10px;
    height: 180px;
    overflow: hidden;
    font-size: 12px;
    color: white;
}}

.msg {{
    margin: 5px 0;
    padding: 5px 8px;
    background: rgba(255,255,255,0.06);
    border-radius: 6px;
}}

/* 🟡 BREAKING NEWS */
.ticker {{
    position: fixed;
    bottom: 0;
    width: 100%;
    background: yellow;
    color: black;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
}}

.ticker span {{
    display: inline-block;
    padding-left: 100%;
    animation: ticker 20s linear infinite;
}}

@keyframes ticker {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

</style>
</head>

<body>

<div class="window">

<div class="topbar">
<div>📺 MTV ULTIMATE TIME MACHINE</div>
<div>● STABLE MODE</div>
</div>

<div class="main">

<div class="sidebar">

<div class="btn" onclick="play('2001')">⏪ 2001 ERA</div>
<div class="btn" onclick="play('2005')">💿 2005 ERA</div>
<div class="btn" onclick="play('2009')">🚀 2009 ERA</div>

</div>

<div class="player">

<div class="screen">
<div class="nowplaying" id="nowplaying">SELECT ERA</div>
<div class="status" id="status">READY</div>
</div>

<audio id="audio" controls autoplay></audio>

<div class="chat" id="chat">
<div class="msg">SYSTEM: ULTIMATE MODE ONLINE 🧠</div>
<div class="msg">DJ: all streams stabilized ✔</div>
</div>

</div>

</div>

<div class="ticker">
<span>
BREAKING: MTV system stabilized • 2000s revival confirmed • NYC radio active • Winamp era restored • Pop punk resurgence • Time machine fully operational • No signal loss detected •
</span>
</div>

</div>

<script>

const streams = {RADIO};

function setStatus(text) {{
    document.getElementById("status").innerText = text;
}}

function play(year) {{

    let audio = document.getElementById("audio");
    let list = streams[year];
    let i = 0;

    document.getElementById("nowplaying").innerText =
    "NOW PLAYING: " + year.toUpperCase();

    function tryStream() {{

        if(i >= list.length) {{
            setStatus("❌ ALL STREAMS FAILED");
            return;
        }}

        setStatus("🔄 CONNECTING STREAM " + (i+1));

        audio.src = list[i];

        audio.play().then(() => {{
            setStatus("✅ PLAYING");
        }}).catch(() => {{
            i++;
            setStatus("⚠ SWITCHING STREAM...");
            tryStream();
        }});

        let timeout = setTimeout(() => {{
            if(audio.readyState < 2) {{
                i++;
                setStatus("⏳ BUFFER FAILED → SWITCHING");
                tryStream();
            }}
        }}, 4000);

        audio.onplaying = () => clearTimeout(timeout);
    }}

    tryStream();
}}

// 💬 STABLE CHAT
const messages = [
    "SYSTEM: connection stable 🗽",
    "Ashley: this is pure nostalgia 😭",
    "Mike: burning CD vibes 💿",
    "DJ: welcome to MTV TIME MACHINE",
    "NYC: signal locked 📡"
];

setInterval(() => {

    let chat = document.getElementById("chat");

    let div = document.createElement("div");
    div.className = "msg";

    div.innerText =
        messages[Math.floor(Math.random() * messages.length)];

    chat.appendChild(div);

    if(chat.children.length > 10) {{
        chat.removeChild(chat.children[0]);
    }}

}, 2000);

</script>

</body>
</html>
"""


@app.route("/alice", methods=["POST"])
def alice():
    return jsonify({
        "response": {
            "text": "ULTIMATE MTV Time Machine online",
            "end_session": False
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)