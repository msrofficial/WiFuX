// Initialize Particles.js
particlesJS("particles-js", {
  particles: {
    number: { value: 80, density: { enable: true, value_area: 800 } },
    color: { value: "#00ffaa" },
    shape: { type: "circle" },
    opacity: { value: 0.5 },
    size: { value: 3 },
    line_linked: { enable: true, distance: 150, color: "#00ffaa", opacity: 0.4, width: 1 },
    move: { enable: true, speed: 2 }
  },
  interactivity: {
    detect_on: "canvas",
    events: { onhover: { enable: true, mode: "repulse" }, onclick: { enable: true, mode: "push" } }
  },
  retina_detect: true
});

// GitHub Stars Counter
fetch('https://api.github.com/repos/msrofficial/WiFuX ')
  .then(res => res.json())
  .then(data => {
    document.getElementById('github-stars').innerText = `⭐ ${data.stargazers_count} stars`;
  })
  .catch(() => {
    document.getElementById('github-stars').innerText = '⭐ Fetching stars...';
  });

// Copy Code Function
function copyCode(id) {
  const code = document.querySelector(`#${id} code`).innerText;
  navigator.clipboard.writeText(code).then(() => {
    alert('Copied to clipboard!');
  });
}
