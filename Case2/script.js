"use strict";

const MINIMUM_VALUE = -10;
const MAXIMUM_VALUE = 10;
let currentValue = 0;

const result = document.getElementById("result");
const message = document.getElementById("message");
const increaseButton = document.getElementById("increaseButton");
const decreaseButton = document.getElementById("decreaseButton");

function updateCounter() {
    result.textContent = currentValue;
    increaseButton.disabled = currentValue === MAXIMUM_VALUE;
    decreaseButton.disabled = currentValue === MINIMUM_VALUE;

    if (currentValue > 0) {
        result.style.background = "#f2c94c";
        result.style.color = "#202020";
    } else if (currentValue < 0) {
        result.style.background = "#27ae60";
        result.style.color = "#ffffff";
    } else {
        result.style.background = "#d61f3c";
        result.style.color = "#ffffff";
    }

    message.textContent = Math.abs(currentValue) === MAXIMUM_VALUE
        ? "Вы достигли экстремального значения"
        : "";
}

increaseButton.addEventListener("click", () => {
    if (currentValue < MAXIMUM_VALUE) {
        currentValue += 1;
        updateCounter();
    }
});

decreaseButton.addEventListener("click", () => {
    if (currentValue > MINIMUM_VALUE) {
        currentValue -= 1;
        updateCounter();
    }
});

updateCounter();

