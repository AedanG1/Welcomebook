document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('vis-toggle').addEventListener('click', (event) => {
        const passwordInput = document.getElementById('password-input')
        let type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password'
        passwordInput.setAttribute('type', type)
        event.target.innerHTML = type === 'password' ? 'visibility_off' : 'visibility'
    })

})