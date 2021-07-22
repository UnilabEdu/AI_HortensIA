const heatmapBtn = document.querySelector(".heatmap__btn");
const linechartBtn = document.querySelector(".linecharts__btn");

linechartBtn.addEventListener("click", () => {
  heatmapBtn.classList.remove("active__btn");

  linechartBtn.classList.add("active__btn");
});

heatmapBtn.addEventListener("click", () => {
  linechartBtn.classList.remove("active__btn");
  heatmapBtn.classList.add("active__btn");
});

const weaklyBtn = document.querySelector(".weakly__btn");
const top10Btn = document.querySelector(".top10__btn");
const recordsBtn = document.querySelector(".records__btn");
const anytimeBtn = document.querySelector(".anytime__btn");
const monthBtn = document.querySelector(".month__btn");
const weekBtn = document.querySelector(".week__btn");
const todayBtn = document.querySelector(".today__btn");

const activetaBtn = (x, ...y) => {
  x.classList.add("active__btn");
  for (var i = 0; i < y.length; i++) {
    y[i].classList.remove("active__btn");
  }
};

weaklyBtn.addEventListener("click", () => {
  activetaBtn(weaklyBtn, recordsBtn, top10Btn);
});
top10Btn.addEventListener("click", () => {
  activetaBtn(top10Btn, recordsBtn, weaklyBtn);
});
recordsBtn.addEventListener("click", () => {
  activetaBtn(recordsBtn, top10Btn, weaklyBtn);
});
anytimeBtn.addEventListener("click", () => {
  activetaBtn(anytimeBtn, monthBtn, weekBtn, todayBtn);
});
monthBtn.addEventListener("click", () => {
  activetaBtn(monthBtn, anytimeBtn, weekBtn, todayBtn);
});
weekBtn.addEventListener("click", () => {
  activetaBtn(weekBtn, monthBtn, anytimeBtn, todayBtn);
});
todayBtn.addEventListener("click", () => {
  activetaBtn(todayBtn, weekBtn, monthBtn, anytimeBtn);
});
