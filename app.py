from flask import Flask
import os
import random

app = Flask(__name__)

RADIO = {
    "late night indie": "https://ice1.somafm.com/indiepop-128-mp3",
    "emo memories": "https://ice1.somafm.com/punkrockers-128-mp3",
    "soft 2000s pop": "https://ice1.somafm.com/poptron-128-mp3",
    "dream beats": "https://ice1.somafm.com/beatblender-128-mp3",
    "sleepy ambient": "https://ice1.somafm.com/groovesalad-128-mp3"
}

MOODS = [
    "it feels like 2am in my thoughts",
    "i miss something i can’t explain",
    "this song feels like memory fragments",
    "everything is softer at night",
    "i reblogged a feeling again",
    "some people exist only in nostalgia"
]

USERS = [
    ("indie_night", "🌙"),
    ("emo_memories", "🖤"),
    ("soft_aesthetic", "🌸"),
    ("nyc_late", "🌆"),
    ("dreamcore", "🌫")
]


@app.route("/")
def home():

    stations = ""
    for k in RADIO:
        stations += f"<div class='btn' onclick=\"play('{k}')\">{k}</div>"

    posts = ""
    for i in range(4):
        u = random.choice(USERS)
        posts += f"""
        <div class="post">
            <div class="user">
                <div class="avatar">{u[1]}</div>
                <div class="name">{u[0]}</div>
            </div>

            <p>{random.choice(MOODS)}</p>

            <div class="actions">
                <span onclick="like(this)">❤️ <b>0</b></span>
                <span onclick="comment(this)">💬 comment</span>
                <span onclick="reblog(this)">🔁 reblog</span>
            </div>

            <div class="comments"></div>
        </div>
        """

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>REAL TUMBLR SOCIAL</title>

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

.rain {{
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: url("https://www.transparenttextures.com/patterns/asfalt-light.png");
    opacity: 0.08;
    animation: rainMove 10s linear infinite;
}}

@keyframes rainMove {{
    from {{ transform: translateY(0); }}
    to {{ transform: translateY(100px); }}
}}

.container {{
    display: flex;
    gap: 15px;
    padding: 15px;
    height: 100vh;
}}

.panel {{
    width: 320px;
    background: rgba(25,25,30,0.75);
    backdrop-filter: blur(10px);
    border-radius: 14px;
    padding: 12px;
}}

.feed {{
    flex: 1;
    overflow-y: auto;
}}

.post {{
    background: rgba(25,25,30,0.75);
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 12px;
}}

.user {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 6px;
}}

.avatar {{
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(255,255,255,0.1);
    display: flex;
    align-items: center;
    justify-content: center;
}}

.actions span {{
    margin-right: 10px;
    cursor: pointer;
    font-size: 12px;
    opacity: 0.8;
}}

.actions span:hover {{
    opacity: 1;
}}

.commentBox {{
    margin-top: 6px;
}}

input {{
    width: 100%;
    padding: 5px;
    border-radius: 6px;
    border: none;
}}

.btn {{
    background: rgba(255,255,255,0.06);
    padding: 6px;
    margin: 4px 0;
    border-radius: 8px;
    cursor: pointer;
}}

audio {{
    width: 100%;
}}

</style>
</head>

<body>

<div class="rain"></div>

<div class="container">

<!-- RADIO -->
<div class="panel">
<h3>🌙 radio mood</h3>
{stations}
<audio id="audio" controls></audio>
</div>

<!-- FEED -->
<div class="feed">
{posts}
</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 music */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
}}

/* ❤️ like */
function like(el) {{
    let b = el.querySelector("b");
    b.innerText = parseInt(b.innerText) + 1;
}}

/* 💬 comment */
function comment(el) {{
    let post = el.closest(".post");
    let box = post.querySelector(".comments");

    let input = document.createElement("input");
    input.placeholder = "write a thought...";

    input.onkeydown = function(e) {{
        if(e.key === "Enter") {{
            let div = document.createElement("div");
            div.innerText = "💬 " + input.value;
            box.appendChild(div);
            input.remove();
        }}
    }}

    box.appendChild(input);
    input.focus();
}}

/* 🔁 reblog */
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
    return {"response": {"text": "tumblr social network active", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)