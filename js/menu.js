// CONSTANTS
const burger = document.querySelector('.burger');
const nav = document.querySelector('nav');
const menu = document.querySelector('.menu');
const login = document.querySelector('.login');


// FUNCTIONS
burger.addEventListener('click', burgerClick);
function burgerClick() {
    burger.classList.toggle('active');
    nav.classList.toggle('active');
}

menu.addEventListener('click', menuClick);
function menuClick() {
    burger.classList.remove('active');
    nav.classList.remove('active');
}

login.addEventListener('click', loginClick);
function loginClick() {
    login.classList.toggle('active');
    nav.classList.toggle('active');
}