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
    document.querySelector('.Swap input').focus()
})

// есть класс Swap - нужно проверить доверние элементы и сделать фокус на первый input



/* ---------------------------------------------------------- Change SignIn/SignUp ---------------------------------------------------------- */

const auth = document.querySelector('.authrorization')
const reg = document.querySelector('.registration')
const inputs = document.querySelectorAll('input')

window.addEventListener('click', (event) => {
    if (event.target.className.includes('goTo')) {
        auth.classList.toggle('Swap')
        reg.classList.toggle('Swap')
        inputs.forEach(element => element.value ='')
    }
})



/* ---------------------------------------------------------- Async ---------------------------------------------------------- */

const urlOfRegist ='http://127.0.0.1:8000/api/v1/users/regist', 
    urlOfAuth = 'http://127.0.0.1:8000/api/v1/users/auth',
    urlOfIsAuth = 'http://127.0.0.1:8000/api/v1/users/is_auth'

// take email and pass from active form

const buttons = document.querySelectorAll('button')
let email
let pass
let data

function nodes() {

    buttons.forEach(element => element.addEventListener('click', (event) => {
        let childsOfSwap = event.target.parentNode.childNodes
        for (let node of childsOfSwap) {
            if (node.name == 'email') {
                email = node.value
            }
            if (node.name == 'password') {
                pass = node.value
            }
        }

        data = {
            email: email,
            password: pass
        }

        paths()
    }))


}
nodes()

// choice of response

function paths() {
    if (auth.className.includes('Swap')) {
        response_auth()
    } else {
        response_regist()
    }
}

async function response_auth() {
    try {
        const request = await fetch(urlOfAuth, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }
    catch (error) {
        console.log(error.message);
    }
}

async function response_regist() {
    try {
        const request = await fetch(urlOfRegist, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
            body: JSON.stringify(data)
        })
    }
    catch (error) {
        console.log(error.message);
    }
}



/* ---------------------------------------------------------- preventDefault ---------------------------------------------------------- */

const forms = document.querySelectorAll('form')
forms.forEach(element => element.addEventListener('submit', (event) => {
    event.preventDefault()
}))