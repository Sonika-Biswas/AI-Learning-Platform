// 🔐 REGISTER
async function registerUser() {
    const email = document.getElementById("regEmail").value;
    const password = document.getElementById("regPassword").value;

    const res = await fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    alert(data.msg);
}


// 🔑 LOGIN
async function loginUser() {
    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        alert("Login successful");
    } else {
        alert(data.msg);
    }
}


// 🚀 GENERATE ROADMAP
async function generate() {
    const topic = document.getElementById("topic").value;
    const token = localStorage.getItem("token");

    const response = await fetch("http://127.0.0.1:5000/generate-roadmap", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({ topic })
    });

    const data = await response.json();

    const result = document.getElementById("result");
    result.innerHTML = "";

    data.roadmap.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        result.appendChild(li);
    });
}