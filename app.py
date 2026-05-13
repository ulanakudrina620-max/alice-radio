from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "late night indie": "https://ice1.somafm.com/indiepop-128-mp3",
    "emo memories": "https://ice1.somafm.com/punkrockers-128-mp3",
    "soft 2000s pop": "https://ice1.somafm.com/poptron-128-mp3",
    "dreamy beats": "https://ice1.somafm.com/beatblender-128-mp3",
    "sleepy chill": "https://ice1.somafm.com/groovesalad-128-mp3"
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
<title>deep tumblr core</title>

<style>

/* 🌙 BASE NIGHT AESTHETIC */
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

/* 🌫 grain */
.grain {{
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: url("https://www.transparenttextures.com/patterns/noise.png");
    opacity: 0.06;
}}

/* 🧠 layout */
.container {{
    display: flex;
    gap: 20px;
    padding: 20px;
    height: 100vh;
}}

/* 🎧 radio */
.panel {{
    width: 360px;
    background: rgba(25,25,30,0.75);
    backdrop-filter: blur(10px);
    border-radius: 14px;
    padding: 15px;
    box-shadow: 0 0 40px rgba(0,0,0,0.6);
}}

.title {{
    font-size: 16px;
    opacity: 0.85;
    margin-bottom: 10px;
}}

.btn {{
    background: rgba(255,255,255,0.06);
    padding: 8px;
    margin: 5px 0;
    border-radius: 10px;
    cursor: pointer;
    transition: 0.2s;
}}

.btn:hover {{
    background: rgba(255,255,255,0.12);
}}

audio {{
    width: 100%;
    margin-top: 10px;
    filter: grayscale(1);
}}

/* 💌 tumblr feed */
.feed {{
    flex: 1;
    overflow-y: auto;
    padding-right: 10px;
}}

.post {{
    background: rgba(25,25,30,0.75);
    margin-bottom: 15px;
    padding: 15px;
    border-radius: 14px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 25px rgba(0,0,0,0.5);
    animation: fade 0.4s ease-in;
}}

@keyframes fade {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.tag {{
    color: #8aa0ff;
    font-size: 12px;
    margin-top: 6px;
    opacity: 0.8;
}}

h1 {{
    font-size: 18px;
    margin: 0 0 8px 0;
    opacity: 0.9;
}}

p {{
    margin: 0;
    opacity: 0.85;
}}

</style>
</head>

<body>

<div class="grain"></div>

<div class="container">

<!-- 🎧 RADIO -->
<div class="panel">
<div class="title">🌙 late night radio</div>

{stations}

<audio id="audio" controls></audio>

<p style="opacity:0.5;font-size:12px;margin-top:10px;">
“music for people who think too much at night”
</p>

</div>

<!-- 💌 FEED -->
<div class="feed">

<div class="post">
<h1>i miss something i can’t name</h1>
<p>it’s not a person. not a place. just a feeling i had once at 2am.</p>
<div class="tag">#tumblr #nostalgia #2012</div>
</div>

<div class="post">
<h1>currently listening</h1>
<p id="now">select a station to set your mood</p>
<div class="tag">#nowplaying</div>
</div>

<div class="post">
<h1>late internet thoughts</h1>
<p>we used to express ourselves more when nobody was watching.</p>
<div class="tag">#deepcore #internet</div>
</div>

</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 play */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
    document.getElementById("now").innerText = station;
}}

/* 💌 living tumblr feed */
const lines = [
    "you are not where you used to be.",
    "this song feels like memory.",
    "some nights are heavier than others.",
    "you reblogged a feeling you can’t explain.",
    "everything is quieter at 2:37am.",
    "you are online, but not really here."
];

setInterval(()=>{{
    const feed = document.querySelector(".feed");

    const post = document.createElement("div");
    post.className = "post";

    post.innerHTML = `
        <h1>thought fragment</h1>
        <p>${{lines[Math.floor(Math.random()*lines.length)]}}</p>
        <div class="tag">#deep tumblr core</div>
    `;

    feed.appendChild(post);

    if(feed.children.length > 7) {{
        feed.removeChild(feed.children[0]);
    }}
}}, 3000);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "deep tumblr core active", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)