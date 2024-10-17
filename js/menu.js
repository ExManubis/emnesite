// CONSTANTS
const burger = document.querySelector('.burger');
const nav = document.querySelector('nav');
const menu = document.querySelector('.menu');
const profile = document.querySelector('.profile_icon');
const login = document.querySelector('.login');
const exit = document.querySelector('.exit');


// FUNCTIONS
burger.addEventListener('click', burgerClick);
function burgerClick() {
    burger.classList.toggle('active');
    login.classList.remove('active');
    nav.classList.toggle('active');
}

menu.addEventListener('click', menuClick);
function menuClick() {
    burger.classList.remove('active');
    nav.classList.remove('active');
}

profile.addEventListener('click', loginClick);
exit.addEventListener('click', loginClick);
function loginClick() {
    login.classList.toggle('active');
}