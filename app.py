from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "MTV POP 2003": "https://ice1.somafm.com/poptron-128-mp3",
    "MYSPACE INDIE": "https://ice1.somafm.com/indiepop-128-mp3",
    "POP PUNK ERA": "https://ice1.somafm.com/punkrockers-128-mp3",
    "DANCE 2005": "https://ice1.somafm.com/beatblender-128-mp3",
    "CHILL NIGHT": "https://ice1.somafm.com/groovesalad-128-mp3"
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
<title>XP NEXT OS LEVEL</title>

<style>

/* 🧠 CRT / OLD MONITOR EFFECT */
body {{
    margin: 0;
    font-family: Tahoma;
    background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');
    overflow: hidden;
}}

.crt {{
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background: repeating-linear-gradient(
        0deg,
        rgba(255,255,255,0.03),
        rgba(255,255,255,0.03) 1px,
        transparent 2px,
        transparent 4px
    );
    animation: flicker 0.15s infinite;
}}

@keyframes flicker {{
    0% {{ opacity: 0.9; }}
    50% {{ opacity: 1; }}
    100% {{ opacity: 0.95; }}
}}

/* 🪟 DESKTOP */
.desktop {{
    width: 100%;
    height: 100vh;
    position: relative;
}}

/* 🪟 WINDOW SYSTEM */
.window {{
    position: absolute;
    width: 320px;
    background: rgba(0,0,0,0.88);
    border: 2px solid #3aa0ff;
    box-shadow: 0 0 20px rgba(0,150,255,0.4);
    color: white;
}}

.titlebar {{
    background: linear-gradient(to right, #0b2a6f, #1e6bff);
    padding: 5px;
    cursor: move;
    display: flex;
    justify-content: space-between;
    font-size: 12px;
}}

.controls span {{
    margin-left: 8px;
    cursor: pointer;
}}

.content {{
    padding: 10px;
}}

.btn {{
    background: #1e6bff;
    padding: 6px;
    margin: 4px 0;
    border-radius: 6px;
    cursor: pointer;
}}

/* 📻 RADIO */
#radio {{ top: 70px; left: 60px; }}
/* 💬 CHAT */
#chat {{ top: 120px; left: 420px; }}

/* 🧠 START MENU */
.startMenu {{
    position: fixed;
    bottom: 40px;
    left: 0;
    width: 200px;
    background: rgba(0,0,0,0.95);
    border: 2px solid #1e6bff;
    display: none;
    padding: 10px;
}}

.startItem {{
    padding: 6px;
    cursor: pointer;
}}

.startItem:hover {{
    background: #1e6bff;
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
    color: white;
}}

.startBtn {{
    background: #00aa00;
    padding: 6px 12px;
    margin-left: 10px;
    cursor: pointer;
}}

.task {{
    margin-left: 10px;
    background: rgba(255,255,255,0.2);
    padding: 3px 8px;
    border-radius: 4px;
    cursor: pointer;
}}

/* 💬 CHAT */
.msg {{
    font-size: 11px;
    margin: 3px 0;
    background: rgba(255,255,255,0.05);
    padding: 4px;
}}

/* ✨ GLITCH EFFECT */
.glitch {{
    position: fixed;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(255,0,255,0.08), transparent);
    pointer-events: none;
}}

</style>
</head>

<body>

<div class="crt"></div>
<div class="glitch"></div>

<!-- 🪟 RADIO -->
<div class="window" id="radio">
<div class="titlebar">
<span>📻 RADIO</span>
<div class="controls">
<span onclick="minimize('radio')">_</span>
<span onclick="closeWin('radio')">X</span>
</div>
</div>
<div class="content">
{stations}
<audio id="audio" controls></audio>
</div>
</div>

<!-- 💬 CHAT -->
<div class="window" id="chat">
<div class="titlebar">
<span>💬 MSN CHAT</span>
<div class="controls">
<span onclick="minimize('chat')">_</span>
<span onclick="closeWin('chat')">X</span>
</div>
</div>
<div class="content" id="chatBox">
<div class="msg">SYSTEM: XP OS ONLINE</div>
<div class="msg">Ashley: 2003 vibes 😭</div>
</div>
</div>

<!-- 🟢 START MENU -->
<div class="startMenu" id="startMenu">
<div class="startItem" onclick="openWin('radio')">📻 Radio</div>
<div class="startItem" onclick="openWin('chat')">💬 Chat</div>
<div class="startItem" onclick="alert('My Computer opened')">💻 My Computer</div>
</div>

<!-- 🟦 TASKBAR -->
<div class="taskbar">
<div class="startBtn" onclick="toggleStart()">START</div>
<div class="task" onclick="openWin('radio')">Radio</div>
<div class="task" onclick="openWin('chat')">Chat</div>
</div>

<script>

const streams = {RADIO};

/* 🎧 RADIO */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
}}

/* 🪟 WINDOW CONTROL */
function openWin(id) {{
    document.getElementById(id).style.display = "block";
}}

function closeWin(id) {{
    document.getElementById(id).style.display = "none";
}}

function minimize(id) {{
    document.getElementById(id).style.display = "none";
}}

/* 🧠 START MENU */
function toggleStart() {{
    const menu = document.getElementById("startMenu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}}

/* 🖱️ DRAG */
function drag(win) {{
    let isDown = false, ox, oy;

    win.querySelector(".titlebar").addEventListener("mousedown", (e)=>{{
        isDown = true;
        ox = e.clientX - win.offsetLeft;
        oy = e.clientY - win.offsetTop;
        win.style.zIndex = 999;
    }});

    document.addEventListener("mousemove", (e)=>{{
        if(!isDown) return;
        win.style.left = (e.clientX - ox) + "px";
        win.style.top = (e.clientY - oy) + "px";
    }});

    document.addEventListener("mouseup", ()=> isDown=false);
}}

document.querySelectorAll(".window").forEach(drag);

/* 💬 LIVE CHAT */
const msgs = [
    "Mike: XP forever 💿",
    "Ashley: MSN is back 💬",
    "DJ: MTV vibes ON",
    "NYC: signal stable 🗽",
    "Emma: Winamp skin era 🎧",
    "SYSTEM: dial-up noise simulated"
];

setInterval(()=> {{
    const box = document.getElementById("chatBox");

    const div = document.createElement("div");
    div.className = "msg";
    div.innerText = msgs[Math.floor(Math.random()*msgs.length)];

    box.appendChild(div);

    if(box.children.length > 10) box.removeChild(box.children[0]);
}}, 1300);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "NEXT OS LEVEL ACTIVE", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)