document.addEventListener('keydown', (e) => {
  if (e.ctrlKey && e.key === 's') {
    e.preventDefault();
    let prompt = window.getSelection().toString() || prompt("プロンプト貼って", "");
    let model = location.hostname.includes("claude") ? "claude" : location.hostname.includes("gemini") ? "gemini" : "chatgpt";
    fetch('http://localhost:8000/save', {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: `content=${encodeURIComponent(prompt)}&model=${model}`
    });
    alert("Vaultに保存した！");
  }
});
