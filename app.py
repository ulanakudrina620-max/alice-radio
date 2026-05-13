from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "late night indie": "https://ice1.somafm.com/indiepop-128-mp3",
    "emo memories": "https://ice1.somafm.com/punkrockers-128-mp3",
    "soft pop 2000s": "https://ice1.somafm.com/poptron-128-mp3",
    "dream beats": "https://ice1.somafm.com/beatblender-128-mp3",
    "sleepy ambient": "https://ice1.somafm.com/groovesalad-128-mp3"
}


@app.route("/")
def home():

    stations = ""
    for k in RADIO:
        stations += f"<div class='btn' onclick=\"play('{k}')\">{k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>tumblr core 2012</title>

<style>

body {{
    margin: 0;
    font-family: Helvetica, Arial;
    background:
    linear-gradient(rgba(0,0,0,0.88), rgba(0,0,0,0.98)),
    url('https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    color: #eaeaea;
    overflow: hidden;
}}

.grain {{
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: url("https://www.transparenttextures.com/patterns/noise.png");
    opacity: 0.06;
}}

.container {{
    display: flex;
    gap: 20px;
    padding: 20px;
    height: 100vh;
}}

.panel {{
    width: 320px;
    background: rgba(25,25,30,0.75);
    backdrop-filter: blur(10px);
    border-radius: 14px;
    padding: 15px;
}}

.btn {{
    background: rgba(255,255,255,0.06);
    padding: 8px;
    margin: 5px 0;
    border-radius: 10px;
    cursor: pointer;
}}

audio {{
    width: 100%;
    margin-top: 10px;
}}

/* 🧾 BLOG PROFILES */
.profile {{
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 12px;
    margin-bottom: 10px;
}}

.avatar {{
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background: #888;
}}

.name {{
    font-weight: bold;
    font-size: 13px;
}}

/* 🎞 POSTS */
.feed {{
    flex: 1;
    overflow-y: auto;
    padding-right: 10px;
}}

.post {{
    background: rgba(25,25,30,0.75);
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 12px;
}}

.gif {{
    width: 100%;
    border-radius: 10px;
    margin-top: 8px;
}}

.actions {{
    display: flex;
    gap: 10px;
    margin-top: 8px;
    font-size: 12px;
    opacity: 0.8;
}}

.action {{
    cursor: pointer;
}}

.action:hover {{
    opacity: 1;
}}

</style>
</head>

<body>

<div class="grain"></div>

<div class="container">

<!-- 🎧 RADIO -->
<div class="panel">
<h3>🌙 radio</h3>

{stations}

<audio id="audio" controls></audio>
</div>

<!-- 🧾 BLOG LIST -->
<div class="panel">
<h3>👤 blogs</h3>

<div class="profile">
<div class="avatar"></div>
<div class="name">indie_night</div>
</div>

<div class="profile">
<div class="avatar"></div>
<div class="name">emo_memories</div>
</div>

<div class="profile">
<div class="avatar"></div>
<div class="name">soft_aesthetic</div>
</div>

<div class="profile">
<div class="avatar"></div>
<div class="name">nyc_late_night</div>
</div>

</div>

<!-- 🎞 FEED -->
<div class="feed">

<div class="post">
<h3>late night thoughts</h3>
<p>some songs feel like memories you never had.</p>
<img class="gif" src="https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif">

<div class="actions">
<div class="action" onclick="like(this)">❤️ like <span>0</span></div>
<div class="action" onclick="reblog(this)">🔁 reblog</div>
</div>
</div>

<div class="post">
<h3>city at 2am</h3>
<p>everything is quieter when you’re thinking too much.</p>
<img class="gif" src="https://media.giphy.com/media/l0HlQ7LRalQqdWfao/giphy.gif">

<div class="actions">
<div class="action" onclick="like(this)">❤️ like <span>0</span></div>
<div class="action" onclick="reblog(this)">🔁 reblog</div>
</div>
</div>

</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 play */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
}}

/* ❤️ like system */
function like(el) {{
    let span = el.querySelector("span");
    span.innerText = parseInt(span.innerText) + 1;
}}

/* 🔁 reblog system */
function reblog(el) {{
    let post = el.closest(".post");
    let clone = post.cloneNode(true);
    document.querySelector(".feed").prepend(clone);
}}

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "tumblr core system active", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)