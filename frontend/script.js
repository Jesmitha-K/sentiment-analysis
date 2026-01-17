async function analyze() {
  const text = document.getElementById("text").value;

  const res = await fetch("http://127.0.0.1:8000/predict", {
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
