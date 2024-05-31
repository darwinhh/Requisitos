const tabs = document.querySelectorAll(".tab");
const tabBtns = document.querySelectorAll(".tab-btn");

const tab_Nav = function(tabBtnClick){
    tabBtns.forEach((btn, index) => {
        if(index === tabBtnClick) {
            btn.classList.add("active");
            tabs[index].classList.add("active");
        } else {
            btn.classList.remove("active");
            tabs[index].classList.remove("active");
        }
    });
}

tabBtns.forEach((tabBtn, i) => {
    tabBtn.addEventListener("click", () => {
        tab_Nav(i);
    });
});