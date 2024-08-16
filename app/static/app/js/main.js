document.addEventListener('DOMContentLoaded', function() {


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

    function formatNumber(phoneNumber) {
        let formattedNumber = phoneNumber.innerHTML.replace(/(\d{3})(\d{3})(\d{4})/, `($1) $2-$3`);
        phoneNumber.innerHTML = formattedNumber
    }

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

    function confirmEdit(item) {
        const text = item.querySelector('.text-edit').value;

        if (item.classList.contains("rule")) {
            const ruleId = item.id;
            const subText = item.querySelector('.subtext-edit').value;

            fetch(`/edit_rule/${ruleId}`, {
                method: 'POST',
                body: JSON.stringify({
                    text: text,
                    subtext: subText
                })
            })
            .then(response => response.text())
            .then(data => {
                console.log(data);
                cancelEdit(item);
                item.querySelector('.editable > .editable-text').innerHTML = `${text}`;
                item.querySelector('.editable > .editable-subtext').innerHTML = `${subText}`;
            })
        } else if (item.classList.contains("info")) {
            const infoId = item.id;
            const title = item.querySelector('.editable > .title-edit').value;
            const subText = item.querySelector('.subtext-edit').value;

            fetch(`/edit_info/${infoId}`, {
                method: 'POST',
                body: JSON.stringify({
                    text: text,
                    subtext: subText,
                    title: title
                })
            })
            .then(response => response.text())
            .then(data => {
                console.log(data);
                cancelEdit(item);
                item.querySelector('.editable > .editable-text').innerHTML = `${text}`;
                item.querySelector('.editable > .editable-subtext').innerHTML = `${subText}`;
                item.querySelector('.editable > .editable-title').innerHTML = `${title}`;
            })
        } else if (item.classList.contains("eats")) {
            const eatsId = item.id;
            const title = item.querySelector('.editable > .title-edit').value;
            const drive = item.querySelector('.editable > .drive-edit').value;
            const website = item.querySelector('.editable > .website-edit').value;
            const phone = item.querySelector('.editable > .phone-edit').value;

            fetch(`/edit_eats/${eatsId}`, {
                method: 'POST',
                body: JSON.stringify({
                    title: title,
                    drive: drive,
                    text: text,
                    website: website,
                    phone: phone
                })
            })
            .then (response => response.text())
            .then (data => {
                console.log(data);
                cancelEdit(item);
                item.querySelector('.editable > .editable-title').innerHTML = `${title}`;
                item.querySelector('.editable > .editable-text').innerHTML = `${text}`;
                item.querySelector('.editable > .editable-drive').innerHTML = `${drive} minute drive`;
                item.querySelector('.editable > .editable-website > .website').innerHTML = `${website}`;
                item.querySelector('.editable > .editable-phone > .phone-number').innerHTML = `${phone}`;
                formatNumber(item.querySelector('.editable > .editable-phone > .phone-number'));
            })
        }
    }


// Delete item function
    function deleteItem(item) {
        const itemId = item.id
        let type
        if (item.classList.contains('rule')) {
            type = 'rule'
        } else if (item.classList.contains('info')) {
            type = 'info'
        } else if (item.classList.contains('eats')) {
            type = 'eats'
        }

        fetch(`/delete_item/${itemId}`, {
            method: 'POST',
            body: JSON.stringify({
                type: type,
                itemId: itemId
            })
        })
        .then (response => response.text())
        .then (data => {
            console.log(data)
            item.remove()
        })
    }

// Remove image function
    function removeImage(item) {
        const infoId = item.id
        const infoImg = item.querySelector('.editable > img')

        fetch(`/edit_info/${infoId}`, {
            method: 'POST',
            body: JSON.stringify({
                remove_img: true
            })
        })
        .then(response => response.text())
        .then(data => {
            console.log(data);
            infoImg.remove();
        })
    }


// Event delegation for edit item
    document.querySelector('.list-group').addEventListener('click', function(event) {
        const action = event.target.closest('button').dataset.action;
        const item = event.target.closest('.list-group-item');

        if (action === 'edit') {
            editItem(item);
        } else if (action === 'cancel') {
            cancelEdit(item);
        } else if (action === 'confirm') {
            confirmEdit(item);
        } else if (action === 'delete') {
            deleteItem(item);
        } else if (action === 'rmv-img') {
            removeImage(item);
        }
    })


// Sorting function
    document.querySelector('.save-positions').addEventListener('click', function() {
        let type
        let dataType = this.dataset.type
        switch(dataType) {
            case 'rule':
                type = 'rule'
                break;
            case 'info':
                type = 'info'
                break;
            case 'eats':
                type = 'eats'
                break;
        }

        let positions = []

        document.querySelectorAll('.list-group-item').forEach(function(item) {
            positions.push(item.getAttribute("id"))
        }) 

        fetch(`/edit_position`, {
            method: 'POST',
            body: JSON.stringify({
                positions: positions,
                type: type
            })
        })
        .then(response => response.text())
        .then(data => {
            console.log(data);
        })
    })
})


// New item function
document.querySelector('.new-item-btn').addEventListener('click', (event) => {

    let type
    let dataType = event.target.dataset.type
    switch(dataType) {
        case 'rule':
            type = 'rule'
            break;
        case 'info':
            type = 'info'
            break;
        case 'eats':
            type = 'eats'
            break;
    }
    fetch(`/add_new_item`, {
        method: 'POST',
        body: JSON.stringify({
            type: type
        })
    })
    .then (response => response.text())
    .then (data => {
        console.log(data);
        location.reload();
    })

})