/* 课程门户顶栏。样式写在本文件里，页面只留挂载点：
   <div id="site-nav" data-current="home" data-root="./"></div>
   <script src="./site-nav.js" defer></script>
   data-current：home syllabus tools agents showcase trends kg library ethics obe assess
   weeks/、course-kg/、assess/ 的 data-root 与脚本地址用 ../
   窄屏顶栏保持一行，链接放进带 aria-expanded 的按钮。 */
(function () {
  var mount = document.getElementById("site-nav");
  if (!mount || mount.getAttribute("data-ready") === "1") return;

  var ALLOWED = {
    home: 1, syllabus: 1, tools: 1, agents: 1, showcase: 1,
    trends: 1, kg: 1, library: 1, ethics: 1, obe: 1, assess: 1
  };
  var GITHUB = "https://github.com/icgma/cpnm-ai-comm-practice";
  var GROUPS = [
    {
      name: "学习",
      items: [
        ["syllabus", "syllabus.html", "教学大纲"],
        ["kg", "course-kg/index.html", "知识图谱"],
        ["assess", "assess/index.html", "周挑战"],
        ["trends", "ai-trends.html", "前沿动态"]
      ]
    },
    {
      name: "课程",
      items: [
        ["ethics", "ai-ethics-handbook.html", "AI伦理手册"],
        ["obe", "obe-matrix.html", "评价与OBE"],
        ["library", "library.html", "资料库"]
      ]
    },
    {
      name: "延伸",
      items: [
        ["tools", "tools.html", "教学工具"],
        ["agents", "agents.html", "AI智能体"],
        ["showcase", "showcase.html", "学生作品"]
      ]
    }
  ];

  var root = mount.getAttribute("data-root") || "./";
  if (root.slice(-1) !== "/") root += "/";
  var current = mount.getAttribute("data-current") || "";
  if (!ALLOWED[current]) current = "";

  if (!document.getElementById("site-nav-style")) {
    var style = document.createElement("style");
    style.id = "site-nav-style";
    style.textContent = [
      "#site-nav{position:sticky;top:0;z-index:1000;font-family:'Noto Sans SC','Microsoft YaHei','PingFang SC',sans-serif}",
      "#site-nav .snav{background:rgba(240,230,207,.96);backdrop-filter:blur(14px);border-bottom:3px double #C7B189}",
      "#site-nav .snav-bar{position:relative;display:flex;align-items:center;gap:12px;flex-wrap:nowrap;width:100%;max-width:1200px;margin:0 auto;padding:8px 28px;min-height:56px;box-sizing:border-box}",
      "#site-nav .snav-brand{display:flex;align-items:center;gap:10px;min-width:0;flex:0 1 auto;color:#3A2E20;text-decoration:none}",
      "#site-nav .snav-brand:hover{color:#3A2E20}",
      "#site-nav .snav-seal{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;flex:none;border:2px solid #A2402F;border-radius:6px;background:rgba(162,64,47,.06);box-shadow:inset 0 0 0 1px rgba(162,64,47,.25);transform:rotate(-4deg)}",
      "#site-nav .snav-seal svg{width:62%;height:62%;display:block}",
      "#site-nav .snav-name{min-width:0}",
      "#site-nav .snav-title{display:block;font-family:'Kaiti SC','STKaiti','KaiTi','Noto Serif SC','Songti SC',serif;font-size:18px;font-weight:700;letter-spacing:1px;line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}",
      "#site-nav .snav-sub{display:block;margin-top:1px;font-family:'EB Garamond',Georgia,serif;font-size:10.5px;letter-spacing:1.5px;text-transform:uppercase;color:#9C8964;white-space:nowrap}",
      "#site-nav .snav-toggle{display:none;appearance:none;margin-left:auto;flex:none;border:1px solid #C7B189;border-radius:4px;background:#F7EFDA;color:#3A2E20;font:600 14px/1 'Noto Sans SC','Microsoft YaHei','PingFang SC',sans-serif;padding:8px 12px;cursor:pointer}",
      "#site-nav .snav-toggle:hover{color:#A2402F;border-color:rgba(162,64,47,.45)}",
      "#site-nav .snav-panel{display:flex;align-items:center;justify-content:flex-end;flex:1 1 auto;flex-wrap:wrap;gap:4px 12px;min-width:0}",
      "#site-nav .snav-group{display:flex;align-items:center;gap:2px;min-width:0}",
      "#site-nav .snav-label{flex:none;padding:0 4px;font-size:12px;letter-spacing:2px;color:#8C6A2F}",
      "#site-nav .snav-panel a{color:#6E5B41;text-decoration:none;font-size:14px;line-height:1.3;padding:5px 8px;border-radius:4px;border:1px solid transparent;white-space:nowrap}",
      "#site-nav .snav-panel a:hover{color:#A2402F;border-color:rgba(162,64,47,.35);background:rgba(162,64,47,.05)}",
      "#site-nav .snav-panel a.is-current{color:#A2402F;border-color:rgba(162,64,47,.4);background:rgba(162,64,47,.07);font-weight:600}",
      "#site-nav .snav-github{font-family:'EB Garamond',Georgia,serif;letter-spacing:.04em}",
      "@media (max-width:960px){",
      "#site-nav .snav-sub{display:none}",
      "#site-nav .snav-title{font-size:15px;max-width:46vw}",
      "#site-nav .snav-bar{padding:8px 14px;gap:8px}",
      "#site-nav .snav-toggle{display:inline-flex}",
      "#site-nav .snav-panel{display:none;position:absolute;z-index:1001;top:100%;left:0;right:0;flex:none;flex-direction:column;align-items:stretch;justify-content:flex-start;flex-wrap:nowrap;gap:0;max-height:min(70vh,560px);overflow:auto;padding:6px 10px 12px;background:#F7EFDA;border-bottom:3px double #C7B189;box-shadow:0 12px 24px rgba(58,46,32,.12)}",
      "#site-nav .snav.is-open .snav-panel{display:flex}",
      "#site-nav .snav-group{flex-direction:column;align-items:stretch;margin-top:6px}",
      "#site-nav .snav-label{padding:8px 10px 2px}",
      "#site-nav .snav-panel a{padding:10px 12px}",
      "}"
    ].join("");
    document.head.appendChild(style);
  }

  var seal = '<svg viewBox="0 0 40 40" aria-hidden="true"><path fill="none" stroke="#A2402F" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round" d="M20 36.5 L11.2 16.5 C13.6 13 16.6 11.2 20 10.9 C23.4 11.2 26.4 13 28.8 16.5 Z"/><path fill="#A2402F" d="M20 13.6 L21.3 16.9 L24.6 18.2 L21.3 19.5 L20 22.8 L18.7 19.5 L15.4 18.2 L18.7 16.9 Z"/><path fill="none" stroke="#A2402F" stroke-width="2.2" stroke-linecap="round" d="M20 23.6 L20 33.4"/></svg>';

  var nav = document.createElement("nav");
  nav.className = "snav";
  nav.setAttribute("aria-label", "课程门户");

  var bar = document.createElement("div");
  bar.className = "snav-bar";

  var brand = document.createElement("a");
  brand.className = "snav-brand";
  brand.href = root + "index.html";
  if (current === "home") brand.setAttribute("aria-current", "page");
  brand.innerHTML = '<span class="snav-seal">' + seal + '</span><span class="snav-name"><span class="snav-title">AI驱动的传媒内容制作</span><span class="snav-sub">AI-Driven Media Content Production</span></span>';

  var button = document.createElement("button");
  button.type = "button";
  button.className = "snav-toggle";
  button.id = "site-nav-toggle";
  button.setAttribute("aria-expanded", "false");
  button.setAttribute("aria-controls", "site-nav-panel");
  button.textContent = "菜单";

  var panel = document.createElement("div");
  panel.className = "snav-panel";
  panel.id = "site-nav-panel";

  GROUPS.forEach(function (group) {
    var wrap = document.createElement("div");
    wrap.className = "snav-group";
    var label = document.createElement("span");
    label.className = "snav-label";
    label.textContent = group.name;
    wrap.appendChild(label);
    group.items.forEach(function (item) {
      var link = document.createElement("a");
      link.href = root + item[1];
      link.textContent = item[2];
      if (item[0] === current) {
        link.className = "is-current";
        link.setAttribute("aria-current", "page");
      }
      wrap.appendChild(link);
    });
    panel.appendChild(wrap);
  });

  var github = document.createElement("a");
  github.className = "snav-github";
  github.href = GITHUB;
  github.target = "_blank";
  github.rel = "noopener noreferrer";
  github.textContent = "GitHub";
  panel.appendChild(github);

  bar.appendChild(brand);
  bar.appendChild(panel);
  bar.appendChild(button);
  nav.appendChild(bar);
  mount.textContent = "";
  mount.appendChild(nav);
  mount.setAttribute("data-ready", "1");

  var mq = window.matchMedia("(max-width: 960px)");

  function sync() {
    var narrow = mq.matches;
    var open = nav.classList.contains("is-open");
    if (!narrow && open) nav.classList.remove("is-open");
    open = nav.classList.contains("is-open");
    button.setAttribute("aria-expanded", narrow && open ? "true" : "false");
    button.setAttribute("aria-label", narrow && open ? "关闭导航" : "打开导航");
    panel.setAttribute("aria-hidden", narrow && !open ? "true" : "false");
  }

  button.addEventListener("click", function () {
    if (!mq.matches) return;
    nav.classList.toggle("is-open");
    sync();
  });

  document.addEventListener("click", function (ev) {
    if (!nav.classList.contains("is-open")) return;
    if (nav.contains(ev.target)) return;
    nav.classList.remove("is-open");
    sync();
  });

  document.addEventListener("keydown", function (ev) {
    if (ev.key !== "Escape" || !nav.classList.contains("is-open")) return;
    nav.classList.remove("is-open");
    sync();
    button.focus();
  });

  panel.addEventListener("click", function (ev) {
    var link = ev.target.closest ? ev.target.closest("a") : null;
    if (!link || !mq.matches) return;
    nav.classList.remove("is-open");
    sync();
  });

  if (mq.addEventListener) mq.addEventListener("change", sync);
  else if (mq.addListener) mq.addListener(sync);
  sync();

  var privacyHref = root + "privacy.html";
  var footers = document.querySelectorAll("footer");
  if (!footers.length) {
    var created = document.createElement("footer");
    created.className = "snav-fallback-footer";
    created.style.cssText = "padding:28px 16px 36px;text-align:center;font-size:14px";
    document.body.appendChild(created);
    footers = [created];
  }
  Array.prototype.forEach.call(footers, function (footer) {
    var links = footer.querySelectorAll("a[href]");
    for (var i = 0; i < links.length; i++) {
      if (/privacy\.html(?:[?#]|$)/.test(links[i].getAttribute("href") || "")) return;
    }
    var row = footer.querySelector("p:last-of-type");
    var anchor = document.createElement("a");
    anchor.href = privacyHref;
    anchor.textContent = "隐私政策";
    if (!row) {
      row = document.createElement("p");
      footer.appendChild(row);
    }
    if (row.textContent.trim()) row.appendChild(document.createTextNode(" · "));
    row.appendChild(anchor);
  });
})();
