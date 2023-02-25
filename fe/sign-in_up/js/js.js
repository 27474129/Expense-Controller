"use strict"



/* ---------------------------------------------------------- SizeOfContainer ---------------------------------------------------------- */

const container = document.querySelector('.container')
const sizeOfContainer = container.offsetHeight
let screenHeight = window.innerHeight

container.style.marginTop = (screenHeight * 0.5 - sizeOfContainer / 2) + "px"

addEventListener('resize', function() {
    screenHeight = window.innerHeight
    container.style.marginTop = (screenHeight * 0.5 - sizeOfContainer / 2) + "px"
})



/* ---------------------------------------------------------- pass&re-pass ---------------------------------------------------------- */

const password = document.querySelectorAll('.registration .correcting')
const buttonSignUp = document.querySelector('.buttonSignUp')

let correctArray = []

password.forEach(element => element.addEventListener('keyup', (event) => {
    if (element.hasAttribute('name')) {
        correctArray[0] = element.value
    } else {
        correctArray[1] = element.value
    }
    
    if (correctArray[0] != correctArray[1]) {
        buttonSignUp.classList.add('disabled')
    } else {
        buttonSignUp.classList.remove('disabled')
    }
}))



/* ---------------------------------------------------------- InputFocus-AutoEnter ---------------------------------------------------------- */

window.addEventListener('keypress', () => {
    document.querySelector('input').focus()
})

// есть класс Swap - нужно проверить доверние элементы и сделать фокус на первый input



/* ---------------------------------------------------------- Change SignIn/SignUp ---------------------------------------------------------- */

const auth = document.querySelector('.authrorization')
const reg = document.querySelector('.registration')

window.addEventListener('click', (event) => {
    if (event.target.className.includes('goTo')) {
        auth.classList.toggle('Swap')
        reg.classList.toggle('Swap')
    }
})