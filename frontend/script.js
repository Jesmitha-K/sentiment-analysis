async function analyze() {
  const text = document.getElementById("text").value;

  const res = await fetch("https://sentiment-analysis-3-04uy.onrender.com/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
});

  const data = await res.json();
  document.getElementById("result").innerText = data.sentiment;
}
document.querySelector(".toggle-btn").onclick = () => {
  document.body.classList.toggle("dark");
};
