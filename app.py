from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "MTV POP 2003": "https://ice1.somafm.com/poptron-128-mp3",
    "MYSPACE INDIE": "https://ice1.somafm.com/indiepop-128-mp3",
    "POP PUNK ERA": "https://ice1.somafm.com/punkrockers-128-mp3",
    "DANCE 2005": "https://ice1.somafm.com/beatblender-128-mp3",
    "CHILL NIGHT": "https://ice1.somafm.com/groovesalad-128-mp3",
    "RNB SLOW JAM": "https://ice1.somafm.com/smoothjazz-128-mp3"
}


@app.route("/")
def home():

    stations = ""
    for k in RADIO:
        stations += f"<div class='btn' onclick=\"play('{k}')\">📻 {k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>XP INTERNET OS</title>

<style>

/* 🧠 XP DESKTOP */
body {{
    margin: 0;
    font-family: Tahoma;
    background:
    linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');
    overflow: hidden;
}}

.desktop {{
    width: 100%;
    height: 100vh;
    position: relative;
}}

/* 🪟 WINDOWS */
.window {{
    position: absolute;
    width: 320px;
    background: rgba(0,0,0,0.85);
    border: 2px solid #3aa0ff;
    border-radius: 8px;
    color: white;
}}

.titlebar {{
    background: linear-gradient(to right, #0b2a6f, #1e6bff);
    padding: 6px;
    cursor: move;
    font-size: 12px;
    font-weight: bold;
}}

.content {{
    padding: 10px;
}}

.btn {{
    background: #1e6bff;
    padding: 6px;
    margin: 4px 0;
    cursor: pointer;
    border-radius: 6px;
    text-align: center;
}}

.btn:hover {{
    background: #3399ff;
}}

/* 📻 RADIO WINDOW */
#radio {{
    top: 80px;
    left: 60px;
}}

/* 💬 CHAT WINDOW */
#chat {{
    top: 120px;
    left: 420px;
}}

/* 📁 MY COMPUTER */
#pc {{
    top: 300px;
    left: 200px;
}}

/* 🟦 TASKBAR */
.taskbar {{
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 40px;
    background: linear-gradient(to right, #0b2a6f, #1e6bff);
    display: flex;
    align-items: center;
    padding: 0 10px;
    color: white;
    font-weight: bold;
}}

.start {{
    background: #00aa00;
    padding: 6px 12px;
    cursor: pointer;
    border-radius: 4px;
    margin-right: 10px;
}}

.clock {{
    margin-left: auto;
}}

/* 💬 CHAT */
.msg {{
    font-size: 11px;
    margin: 3px 0;
    background: rgba(255,255,255,0.05);
    padding: 4px;
    border-radius: 4px;
}}

/* 🟡 NEWS */
.news {{
    position: fixed;
    top: 0;
    width: 100%;
    background: yellow;
    color: black;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
}}

.news span {{
    display: inline-block;
    padding-left: 100%;
    animation: move 14s linear infinite;
}}

@keyframes move {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

audio {{
    width: 100%;
}}

</style>
</head>

<body>

<!-- 🟡 BREAKING NEWS -->
<div class="news">
<span>
MTV XP OS ONLINE • MySpace revival detected • Winamp skins trending • MSN Messenger active • Limewire nostalgia spike • CD burning returns • Avril Lavigne charts • Windows XP simulation running •
</span>
</div>

<div class="desktop">

<!-- 📻 RADIO -->
<div class="window" id="radio">
<div class="titlebar">📻 RADIO PLAYER</div>
<div class="content">

{stations}

<audio id="audio" controls></audio>

</div>
</div>

<!-- 💬 CHAT -->
<div class="window" id="chat">
<div class="titlebar">💬 MSN CHAT</div>
<div class="content" id="chatBox">
<div class="msg">SYSTEM: XP OS ONLINE</div>
<div class="msg">Ashley: this feels like 2003 😭</div>
</div>
</div>

<!-- 💻 MY COMPUTER -->
<div class="window" id="pc">
<div class="titlebar">💻 MY COMPUTER</div>
<div class="content">
📁 Local Disk (C:)<br>
📁 My Music<br>
📁 My Videos<br>
📁 Downloads (Limewire)<br>
</div>
</div>

</div>

<!-- 🟦 TASKBAR -->
<div class="taskbar">
<div class="start" onclick="alert('START MENU (simulated XP)')">START</div>
MTV XP INTERNET OS
<div class="clock">ONLINE ●</div>
</div>

<script>

const streams = {RADIO};

/* 🎧 RADIO */
function play(station) {{
    const audio = document.getElementById("audio");
    audio.src = streams[station];
    audio.play().catch(()=>{{}});
}}

/* 🪟 DRAG SYSTEM */
function drag(win) {{
    let isDown = false;
    let offsetX, offsetY;

    win.querySelector(".titlebar").addEventListener("mousedown", (e) => {{
        isDown = true;
        offsetX = e.clientX - win.offsetLeft;
        offsetY = e.clientY - win.offsetTop;
    }});

    document.addEventListener("mousemove", (e) => {{
        if(!isDown) return;
        win.style.left = (e.clientX - offsetX) + "px";
        win.style.top = (e.clientY - offsetY) + "px";
    }});

    document.addEventListener("mouseup", () => {{
        isDown = false;
    }});
}}

document.querySelectorAll(".window").forEach(drag);

/* 💬 LIVE CHAT */
const msgs = [
    "Mike: MSN is alive again 💬",
    "Ashley: burning CDs 💿",
    "DJ: MTV mode active",
    "SYSTEM: dial-up simulation",
    "NYC: signal stable 🗽",
    "Emma: Winamp forever 🎧"
];

setInterval(() => {{
    const box = document.getElementById("chatBox");

    const div = document.createElement("div");
    div.className = "msg";
    div.innerText = msgs[Math.floor(Math.random()*msgs.length)];

    box.appendChild(div);

    if(box.children.length > 10) {{
        box.removeChild(box.children[0]);
    }}

}}, 1500);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "XP INTERNET OS ACTIVE", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)