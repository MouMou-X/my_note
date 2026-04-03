---
tags: [Obsidian]
type: moc
status: 🌿
---

```dataviewjs
const items = [
    ["🏠", "主页", "01个人主页/主页"],
    ["💡", "收集箱", "02Inbox(收集箱)/Inbox_main"],
    ["💼", "项目", "03Project(项目)/Project_main"],
    ["✨", "领域", "04Areas(领域)/Areas_main"],
    ["📚", "资源", "05Resources(资源)/Resources_main"],
    ["🥇", "归档", "06Archive(归档)/Archive_main"],
    ["🔍", "Wiki", "Wiki"],
];
const cur = dv.current().file.name;
const nav = dv.el("nav", "", {
    attr: { style: "display:flex;gap:4px;padding:8px 12px;background:var(--background-secondary);border-radius:8px;flex-wrap:wrap;justify-content:center;border:1px solid var(--background-modifier-border);margin-bottom:16px;" }
});
for (const [emoji, label, path] of items) {
    const active = cur === path.split("/").pop();
    nav.createEl("a", {
        text: `${emoji} ${label}`,
        cls: "internal-link",
        attr: { "data-href": path, href: path,
            style: `padding:6px 14px;border-radius:6px;text-decoration:none;font-size:14px;font-weight:${active?"600":"normal"};background:${active?"var(--interactive-accent)":"transparent"};color:${active?"var(--text-on-accent)":"var(--text-muted)"};` }
    });
}
```

