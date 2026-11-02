const ROLES = { buyer: "kupec", seller: "prodajalec", admin: "administrator" };

const MENU = {
    buyer: [["index.html", "Oglasi"], ["iskanja.html", "Moja iskanja"], ["profil.html", "Profil"]],
    seller: [["index.html", "Oglasi"], ["oddaj.html", "Oddaj oglas"], ["moji-oglasi.html", "Moji oglasi"], ["profil.html", "Profil"]],
    admin: [["pregled.html", "Oglasi v pregledu"]],
};

async function api(method, url, body) {
    const response = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: body && JSON.stringify(body),
    });
    const data = await response.json().catch(() => null);
    return { ok: response.ok, data };
}

function errorText(data, fallback) {
    return typeof data?.detail === "string" ? data.detail : fallback;
}

async function logout() {
    await api("POST", "/logout");
    location.href = "/";
}

const currentUser = api("GET", "/me").then(({ data }) => {
    if (!data && "login" in document.body.dataset) {
        location.href = "login.html";
    }
    const header = document.getElementById("header");
    const items = data ? MENU[data.role] : [["login.html", "Prijava"], ["register.html", "Registracija"]];
    header.innerHTML = '<a href="/">KockiTsa</a> ' + items.map(([href, text]) => `<a href="${href}">${text}</a>`).join(" ");
    if (data) {
        const user = document.createElement("span");
        user.textContent = ` | ${data.name} (${ROLES[data.role]}) `;
        const button = document.createElement("button");
        button.textContent = "Odjava";
        button.onclick = logout;
        header.append(user, button);
    }
    return data;
});
