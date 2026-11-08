const ROLES = { buyer: "kupec", seller: "prodajalec", admin: "administrator" };
const CONDITIONS = { sealed: "zapečaten", new: "nov", used: "rabljen" };
const STATUSES = { pending: "v pregledu", approved: "objavljen", rejected: "zavrnjen", reserved: "rezerviran", sold: "prodan" };
const eur = new Intl.NumberFormat("sl-SI", { style: "currency", currency: "EUR" });

const MENU = {
    buyer: [["index.html", "Oglasi"], ["iskanja.html", "Moja iskanja"], ["profil.html", "Profil"]],
    seller: [["index.html", "Oglasi"], ["oddaj.html", "Oddaj oglas"], ["moji-oglasi.html", "Moji oglasi"], ["profil.html", "Profil"]],
    admin: [["pregled.html", "Oglasi v pregledu"]],
};

function el(tag, props = {}, ...children) {
    const node = Object.assign(document.createElement(tag), props);
    node.append(...children);
    return node;
}

const badge = (status) => el("span", { className: `badge ${status}`, textContent: STATUSES[status] });

const toastBox = document.body.appendChild(el("div", { id: "toast", hidden: true }));
let toastTimer;

function toast(text, error = false) {
    toastBox.textContent = text;
    toastBox.className = error ? "error" : "";
    toastBox.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastBox.hidden = true, 3000);
}

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

async function updateCounter() {
    const link = document.querySelector('nav a[href="iskanja.html"]');
    const { ok, data } = await api("GET", "/my/searches/count");
    if (link && ok) {
        link.textContent = data.count ? `Moja iskanja (${data.count})` : "Moja iskanja";
    }
}

async function logout() {
    await api("POST", "/logout");
    location.href = "/";
}

const currentUser = api("GET", "/me").then(({ data }) => {
    const roles = document.body.dataset.role?.split(" ");
    if (!data && "login" in document.body.dataset) {
        location.href = "login.html";
    }
    if (data && roles && !roles.includes(data.role)) {
        location.href = "/";
        return null;
    }
    const page = location.pathname.split("/").pop() || "index.html";
    const nav = el("nav", {}, ...(data ? MENU[data.role] : []).map(([href, text]) =>
        el("a", { href, textContent: text, className: href === page ? "active" : "" })));
    const user = data
        ? el("div", { className: "user" }, el("span", { textContent: `${data.name} (${ROLES[data.role]})` }),
            el("button", { className: "btn ghost small", textContent: "Odjava", onclick: logout }))
        : el("div", { className: "user" }, el("a", { href: "login.html", textContent: "Prijava" }),
            el("a", { href: "register.html", textContent: "Registracija" }));
    document.getElementById("header").replaceChildren(el("div", { className: "bar" },
        el("a", { className: "logo", href: "/", innerHTML: "Kocki<span>Tsa</span>" }), nav, user));
    if (data?.role === "buyer") {
        updateCounter();
    }
    return data;
});
