from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "MTV POP 2003": "https://ice1.somafm.com/poptron-128-mp3",
    "MYSPACE INDIE": "https://ice1.somafm.com/indiepop-128-mp3",
    "PUNK CD BURN": "https://ice1.somafm.com/punkrockers-128-mp3",
    "WINAMP DANCE": "https://ice1.somafm.com/beatblender-128-mp3",
    "LATE NIGHT CHILL": "https://ice1.somafm.com/groovesalad-128-mp3"
}


@app.route("/")
def home():

    buttons = ""
    for k in RADIO:
        buttons += f"<div class='btn' onclick=\"play('{k}')\">{k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>2003 INTERNET SIMULATOR</title>

<style>

/* 🌐 OLD INTERNET CRT FEEL */
body {{
    margin: 0;
    font-family: Tahoma, Verdana;
    background:
    radial-gradient(circle at top, #1a1a2e, #000),
    url('https://images.unsplash.com/photo-1526481280695-3c687fd5432c?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    overflow: hidden;
    color: white;
}}

/* 💻 DESKTOP LAYER */
.desktop {{
    display: flex;
    height: 100vh;
}}

/* 📁 LEFT PANEL (MYSPACE FEEL) */
.sidebar {{
    width: 260px;
    background: rgba(0,0,0,0.7);
    padding: 10px;
    border-right: 2px solid #00ffff;
}}

.btn {{
    background: linear-gradient(to bottom, #00aaff, #003366);
    padding: 8px;
    margin: 5px 0;
    cursor: pointer;
    text-align: center;
    border: 1px solid #66ccff;
}}

.btn:hover {{
    transform: scale(1.05);
}}

/* 📺 MAIN WINDOW */
.main {{
    flex: 1;
    padding: 15px;
    position: relative;
}}

/* 🎧 PLAYER BOX */
.player {{
    background: rgba(0,0,0,0.75);
    border: 2px solid #00ffff;
    padding: 15px;
    border-radius: 8px;
    width: 520px;
}}

audio {{
    width: 100%;
}}

/* 💬 MSN CHAT */
.chat {{
    margin-top: 10px;
    height: 180px;
    overflow: hidden;
    background: rgba(0,0,0,0.8);
    padding: 10px;
    border: 1px solid #ff00ff;
    font-size: 12px;
}}

.msg {{
    margin: 3px 0;
    padding: 3px;
}}

/* 🟡 BREAKING NEWS (VERY 2000s) */
.news {{
    position: fixed;
    top: 0;
    width: 100%;
    background: yellow;
    color: black;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
    border-bottom: 2px solid black;
}}

.news span {{
    display: inline-block;
    padding-left: 100%;
    animation: move 18s linear infinite;
}}

@keyframes move {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

/* 🟣 FLOATING ADS (MYSPACE ERA) */
.ad {{
    position: absolute;
    right: 20px;
    top: 120px;
    width: 200px;
    background: rgba(255,0,255,0.2);
    border: 1px dashed magenta;
    padding: 10px;
    font-size: 11px;
}}

.online {{
    color: lime;
    animation: blink 1s infinite;
}}

@keyframes blink {{
    0% {{ opacity: 1; }}
    50% {{ opacity: 0.3; }}
    100% {{ opacity: 1; }}
}}

</style>
</head>

<body>

<!-- 🟡 BREAKING NEWS BAR -->
<div class="news">
<span>
BREAKING: MySpace TOP 8 returns • MTV 2003 countdown leaked • Winamp skins trending again • Limewire revival detected • CD burning hits peak • MSN Messenger servers simulated online • Avril Lavigne dominates charts • Nokia ringtone culture returns • Napster nostalgia wave • Windows XP theme viral again •
</span>
</div>

<div class="desktop">

<!-- 📁 SIDEBAR -->
<div class="sidebar">
<h3>📀 RADIO STATIONS</h3>
{buttons}

<div style="margin-top:10px" class="online">
● MSN STATUS: ONLINE
</div>
</div>

<!-- 🎧 MAIN -->
<div class="main">

<div class="player">

<h2 id="now">SELECT STATION</h2>

<audio id="audio" controls></audio>

<div class="chat" id="chat">
<div class="msg">SYSTEM: MSN Messenger connected 💬</div>
<div class="msg">Ashley: burning CDs again 💿</div>
<div class="msg">Mike: Winamp skin hunting 🎧</div>
</div>

</div>

</div>

<!-- 🟣 FAKE AD -->
<div class="ad">
<b>HOT ON MYSPACE 🔥</b><br><br>
Avril Lavigne - Sk8er Boi<br>
Blink-182 - I Miss You<br>
Green Day - American Idiot<br><br>
<span style="color:lime">DOWNLOAD VIA LIMEWIRE</span>
</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 PLAY */
function play(station) {{
    const audio = document.getElementById("audio");
    document.getElementById("now").innerText = "NOW PLAYING: " + station;

    audio.src = streams[station];
    audio.play().catch(()=>{{}});
}}

/* 💬 CHAOTIC 2003 CHAT */
const chatLines = [
    "Ashley: omg this is so MySpace era 😭",
    "Mike: I just burned 12 CDs today 💿",
    "DJ: MTV countdown vibes 🔥",
    "SYSTEM: user logged in via dial-up",
    "Emma: MSN status = BRB listening to punk",
    "Jake: Limewire downloading is life 💀",
    "Tom: Nokia ringtone nostalgia",
    "Lisa: Avril Lavigne takeover",
    "NYC: signal stable 🗽"
];

setInterval(() => {{
    const chat = document.getElementById("chat");

    const div = document.createElement("div");
    div.className = "msg";

    div.innerText = chatLines[Math.floor(Math.random()*chatLines.length)];

    chat.appendChild(div);

    if(chat.children.length > 10) {{
        chat.removeChild(chat.children[0]);
    }}

}}, 1700);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "2003 INTERNET SIMULATOR ACTIVE", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)