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


// Create sortable.js list
    const sortableList = document.getElementById('sortable');
    Sortable.create(sortableList, {
        handle: '.drag-btn',
        animation: 150
    });
    

// Format Phone-numbers
    document.querySelectorAll('.phone-number').forEach((phoneNumber) => {
        formatNumber(phoneNumber)
    })

    // Reference: https://www.geeksforgeeks.org/how-to-format-a-phone-number-in-human-readable-using-javascript/
    function formatNumber(phoneNumber) {
        let formattedNumber = phoneNumber.innerHTML.replace(/(\d{3})(\d{3})(\d{4})/, `($1) $2-$3`);
        phoneNumber.innerHTML = formattedNumber
    }


// Toggle Edit Functions
    function editItem(item) {
        item.querySelectorAll('.non-edit').forEach((element) => {
            element.style.display = 'none';
        })

        item.querySelectorAll('.edit').forEach((element) => {
            element.style.display = 'block';
        })
    }


    function cancelEdit(item) {
        item.querySelectorAll('.non-edit').forEach((element) => {
            element.style.display = 'block';
        })

        item.querySelectorAll('.edit').forEach((element) => {
            element.style.display = 'none';
        })
    }


// Confirm edit function
    function confirmEdit(item, itemId, type) {
        const userInput = item.getElementsByClassName('user-input');
        const elements = item.getElementsByClassName('display');
        let itemObject = {};
        itemObject.type = type;

        for (let i = 0; i < userInput.length; i++) {
            itemObject[userInput[i].dataset.name] = userInput[i].value;
        }

        const body = JSON.stringify(itemObject);
        fetch(`/edit_item/${itemId}`, {...requestOptions, body})
        .then(response => response.text())
        .then(data => {
            console.log(data);
            cancelEdit(item);
            for (let i = 0; i < elements.length; i++) {
                elements[i].innerHTML = userInput[i].value;
            }
            if (item.classList.contains("eats")) {
                formatNumber(item.querySelector('.phone-number'))
            }
        })
    }


// Delete item function
    function deleteItem(item, itemId, type) {
        const body = JSON.stringify({type: type});
        fetch(`/delete_item/${itemId}`, {...requestOptions, body})
        .then (response => response.text())
        .then (data => {
            console.log(data);
            item.remove();
        })
    }


// Remove image function
    function removeImage(item, itemId, type) {
        const itemImg = item.querySelector('.editable > div > img');

        const body = JSON.stringify({type: type})
        fetch(`/remove_image/${itemId}`, {...requestOptions, body})
        .then(response => response.text())
        .then(data => {
            console.log(data);
            itemImg.remove();
        })
    }


// Event delegation for edit item
    document.querySelector('.list-group').addEventListener('click', function(event) {
        const action = event.target.closest('button').dataset.action;
        const item = event.target.closest('.list-group-item');
        const itemId = event.target.closest('.list-group-item').id;
        const type = event.target.closest('.list-group-item').dataset.type;

        if (action === 'edit') {
            editItem(item, itemId, type);
        } else if (action === 'cancel') {
            cancelEdit(item, itemId, type);
        } else if (action === 'confirm') {
            confirmEdit(item, itemId, type);
        } else if (action === 'delete') {
            deleteItem(item, itemId, type);
        } else if (action === 'rmv-img') {
            removeImage(item, itemId, type);
        }
    })


// Sorting function
    document.querySelector('.save-positions').addEventListener('click', (event) => {
        const type = event.target.dataset.type

        let positions = []

        document.querySelectorAll('.list-group-item').forEach(function(item) {
            positions.push(item.getAttribute("id"))
        }) 

        const body = JSON.stringify({
            positions: positions,
            type: type
        })
        fetch(`/edit_position`, {...requestOptions, body})
        .then(response => response.text())
        .then(data => {
            console.log(data);
        })
    })



// New item function
    document.querySelector('.new-item-btn').addEventListener('click', (event) => {
        const type = event.target.dataset.type

        const body = JSON.stringify({type: type})
        fetch(`/add_new_item`, {...requestOptions, body})
        .then (response => response.text())
        .then (data => {
            console.log(data);
            location.reload();
        })

    })

// end
})