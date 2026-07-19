"use strict";

const firstNumberInput = document.getElementById("firstNumber");
const secondNumberInput = document.getElementById("secondNumber");
const result = document.getElementById("result");
const operationButtons = document.querySelectorAll("[data-operation]");

function parseNumber(value) {
    const normalizedValue = value.trim().replace(",", ".");
    if (normalizedValue === "") {
        return Number.NaN;
    }
    return Number(normalizedValue);
}

function showResult(text, type) {
    result.textContent = text;
    result.className = `result ${type}`;
}

function calculate(operation) {
    const firstNumber = parseNumber(firstNumberInput.value);
    const secondNumber = parseNumber(secondNumberInput.value);

    if (!Number.isFinite(firstNumber) || !Number.isFinite(secondNumber)) {
        showResult("Ошибка! Введите числа.", "error");
        return;
    }

    let calculationResult;
    if (operation === "sum") calculationResult = firstNumber + secondNumber;
    if (operation === "difference") calculationResult = firstNumber - secondNumber;
    if (operation === "product") calculationResult = firstNumber * secondNumber;
    if (operation === "division") {
        if (secondNumber === 0) {
            showResult("Деление на ноль невозможно.", "error");
            return;
        }
        calculationResult = firstNumber / secondNumber;
    }

    showResult(`Результат: ${calculationResult}`, "success");
}

operationButtons.forEach((button) => {
    button.addEventListener("click", () => calculate(button.dataset.operation));
});

