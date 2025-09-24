import React, { useEffect, useState } from "react";

function ThemeToggle() {
  const [dark, setDark] = useState(() => {
    try {
      const val = localStorage.getItem("theme");
      return val === "dark" || (!val && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
    } catch {
      return false;
    }
  });

  useEffect(() => {
    const root = document.documentElement;
    if (dark) root.classList.add("dark"); else root.classList.remove("dark");
    localStorage.setItem("theme", dark ? "dark" : "light");
  }, [dark]);

  return (
    <button onClick={() => setDark(!dark)} style={{
      padding: "6px 10px", borderRadius: 8, border: "none", cursor: "pointer",
      background: dark ? "#ffffff22" : "#00000008", color: "white", fontWeight: 600
    }}>
      {dark ? "🌙 Dark" : "☀️ Light"}
    </button>
  );
}

export default ThemeToggle;
