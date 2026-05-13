from flask import Flask
import os

app = Flask(__name__)

# 🎧 FINAL STABLE RADIO SET
RADIO = {
    "POP 2000s": "https://ice1.somafm.com/poptron-128-mp3",
    "INDIE XP": "https://ice1.somafm.com/indiepop-128-mp3",
    "PUNK XP": "https://ice1.somafm.com/punkrockers-128-mp3",
    "DANCE XP": "https://ice1.somafm.com/beatblender-128-mp3",
    "CHILL XP": "https://ice1.somafm.com/groovesalad-128-mp3",
    "RNB XP": "https://ice1.somafm.com/smoothjazz-128-mp3"
}


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>FINAL LEVEL MTV XP RADIO</title>

<style>

body {{
    margin: 0;
    font-family: Tahoma, Arial;
    background:
    linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    height: 100vh;
    overflow: hidden;
}}

/* 🪟 DESKTOP */
.window {{
    display: flex;
    flex-direction: column;
    height: 100vh;
}}

.topbar {{
    height: 50px;
    background: linear-gradient(to right, #0b2a6f, #1a5cff);
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    font-weight: bold;
}}

.main {{
    flex: 1;
    display: flex;
    padding: 20px;
    gap: 20px;
}}

/* 📁 SIDEBAR */
.sidebar {{
    width: 260px;
    background: rgba(0,0,0,0.6);
    border-radius: 12px;
    padding: 15px;
}}

.btn {{
    background: linear-gradient(to bottom, #4fb3ff, #0050aa);
    border: 1px solid #8bd1ff;
    padding: 10px;
    margin-bottom: 8px;
    border-radius: 10px;
    cursor: pointer;
    color: white;
    font-weight: bold;
    text-align: center;
}}

.btn:hover {{
    transform: scale(1.04);
}}

/* 📺 PLAYER */
.player {{
    flex: 1;
    background: rgba(0,0,0,0.78);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
}}

.screen {{
    background: black;
    border: 1px solid #66d9ff;
    border-radius: 10px;
    padding: 15px;
    color: #00ffcc;
}}

.now {{
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

/* 🎚 EQ */
.eq {{
    display: flex;
    gap: 3px;
    margin-top: 10px;
    height: 25px;
}}

.bar {{
    width: 4px;
    background: lime;
    animation: eq 0.5s infinite ease-in-out;
}}

.bar:nth-child(2) {{ animation-delay: 0.1s; }}
.bar:nth-child(3) {{ animation-delay: 0.2s; }}
.bar:nth-child(4) {{ animation-delay: 0.3s; }}

@keyframes eq {{
    0% {{ height: 5px; }}
    50% {{ height: 25px; }}
    100% {{ height: 8px; }}
}}

/* 💬 CHAT */
.chat {{
    margin-top: 15px;
    background: rgba(10,10,25,0.9);
    border-radius: 10px;
    padding: 10px;
    height: 160px;
    overflow: hidden;
    color: white;
    font-size: 12px;
}}

.msg {{
    margin: 5px 0;
    padding: 4px 6px;
    background: rgba(255,255,255,0.05);
    border-radius: 6px;
}}

/* 🟡 TICKER */
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
    animation: move 18s linear infinite;
}}

@keyframes move {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

</style>
</head>

<body>

<div class="window">

<div class="topbar">
<div>📺 FINAL LEVEL MTV XP RADIO</div>
<div>● STABLE SYSTEM</div>
</div>

<div class="main">

<div class="sidebar">

<div class="btn" onclick="play('POP 2000s')">POP 2000s</div>
<div class="btn" onclick="play('INDIE XP')">INDIE XP</div>
<div class="btn" onclick="play('PUNK XP')">PUNK XP</div>
<div class="btn" onclick="play('DANCE XP')">DANCE XP</div>
<div class="btn" onclick="play('CHILL XP')">CHILL XP</div>
<div class="btn" onclick="play('RNB XP')">RNB XP</div>

</div>

<div class="player">

<div class="screen">
<div class="now" id="now">SELECT STATION</div>
<div class="status" id="status">READY</div>

<div class="eq">
<div class="bar"></div>
<div class="bar"></div>
<div class="bar"></div>
<div class="bar"></div>
</div>

</div>

<audio id="audio" controls></audio>

<div class="chat" id="chat">
<div class="msg">SYSTEM: FINAL LEVEL ONLINE ✔</div>
<div class="msg">DJ: welcome to MTV XP radio</div>
</div>

</div>

</div>

<div class="ticker">
<span>
FINAL LEVEL ACTIVE • WINAMP ERA SIMULATION • NYC RADIO SIGNAL STABLE • 2000s CULTURE RESTORED • MTV DESKTOP RUNNING •
</span>
</div>

</div>

<script>

const streams = {RADIO};

function play(station) {{

    let audio = document.getElementById("audio");

    document.getElementById("now").innerText =
    "NOW PLAYING: " + station;

    document.getElementById("status").innerText = "CONNECTING...";

    audio.src = streams[station];
    audio.load();

    audio.play()
    .then(() => {{
        document.getElementById("status").innerText = "PLAYING ✔";
    }})
    .catch(() => {{
        document.getElementById("status").innerText = "CLICK PLAY ▶";
    }});
}}

const msgs = [
    "DJ: MTV XP is alive",
    "Ashley: nostalgia overload 😭",
    "Mike: Winamp forever 💿",
    "SYSTEM: stable connection",
    "NYC: signal locked 📡"
];

setInterval(() => {{

    let chat = document.getElementById("chat");

    let div = document.createElement("div");
    div.className = "msg";

    div.innerText = msgs[Math.floor(Math.random()*msgs.length)];

    chat.appendChild(div);

    if(chat.children.length > 10) {{
        chat.removeChild(chat.children[0]);
    }}

}}, 2300);

</script>

</body>
</html>
"""


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "FINAL LEVEL UI ACTIVE", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)