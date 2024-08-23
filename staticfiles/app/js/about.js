document.addEventListener('DOMContentLoaded', function() {
    // Obtain CSRFtoken
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    const requestOptions = {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
    }

    const quill = new Quill('#editor', {
        theme: 'snow'
    })

    const saveBtn = document.getElementById('save-btn')
    saveBtn.addEventListener('click', (event) => {
        const html = quill.getSemanticHTML()
        const body = JSON.stringify({html: html})
        fetch(`/save_about`, {...requestOptions, body})
        .then(request => request.text())
        .then(data => {
            console.log(data)
        })
    })

})