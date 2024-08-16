document.addEventListener('DOMContentLoaded', function() {


// Create sortable.js list
    const sortableList = document.getElementById('sortable');
    Sortable.create(sortableList, {
        handle: '.drag-btn',
        animation: 150
    });
    
// Format Phone-numbers
    if (document.querySelector('.phone-number')) {
        document.querySelectorAll('.phone-number').forEach((phoneNumber) => {
            let formattedNumber = phoneNumber.innerHTML.replace(/(\d{3})(\d{3})(\d{4})/, `($1) $2-$3`);
            phoneNumber.innerHTML = formattedNumber
        })
    }

// Toggle Rule display function
    function toggleRuleDisplay(item, displayState) {
        // Object of elements to be changed
        const elements = {
            // Buttons
            editBtn: item.querySelector('.edit-btn-group > .edit-btn'),
            cancelBtn: item.querySelector('.edit-btn-group > .edit-cancel'),
            confirmBtn: item.querySelector('.edit-btn-group > .edit-confirm'),
            deleteBtn: item.querySelector('.delete-btn'),
        }

        // Default text
        if (item.querySelector('.editable > .editable-text')) {
            const textObject = {
                text: item.querySelector('.editable > .editable-text'),
                textArea: item.querySelector('.editable > .text-edit'),
                label: item.querySelector('.editable > .text-edit-label'),
            }
            Object.assign(elements, textObject);
        }

        // Sub text
        if (item.querySelector('.editable > .editable-subtext')) {
            const subTextObject = {
                subText: item.querySelector('.editable > .editable-subtext'),
                subTextArea: item.querySelector('.editable > .subtext-edit'),
                subLabel: item.querySelector('.editable > .subtext-edit-label'),
            }
            Object.assign(elements, subTextObject);
        }

        if (item.classList.contains('info')) {
            const infoObject = {
                title: item.querySelector('.editable > .editable-title'),
                titleArea: item.querySelector('.editable > .title-edit'),
                titleLabel: item.querySelector('.editable > .title-edit-label'),
                imgForm: item.querySelector('.editable > .img-form'),
                imgRemove: item.querySelector('.editable > .img-remove')
            }
            Object.assign(elements, infoObject);
        }

        if (item.classList.contains('eats')) {
            const eatsObject = {
                title: item.querySelector('.editable > .editable-title'),
                titleArea: item.querySelector('.editable > .title-edit'),
                titleLabel: item.querySelector('.editable > .title-edit-label'),
                imgForm: item.querySelector('.editable > .img-form'),
                imgRemove: item.querySelector('.editable > .img-remove'),
                drive: item.querySelector('.editable > .editable-drive'),
                driveArea: item.querySelector('.editable > .drive-edit'),
                driveLabel: item.querySelector('.editable > .drive-edit-label'),
                website: item.querySelector('.editable > .editable-website'),
                websiteArea: item.querySelector('.editable > .website-edit'),
                websiteLabel: item.querySelector('.editable > .website-edit-label'),
                phone: item.querySelector('.editable > .editable-phone'),
                phoneArea: item.querySelector('.editable > .phone-edit'),
                phoneLabel: item.querySelector('.editable > .phone-edit-label')
            }
            Object.assign(elements, eatsObject);
        }

        // Iterates over the elements Object
        for (const [key, element] of Object.entries(elements)) {
            // Changes the current element's display style to the corresponding
            // display state value passed in by either editRule or cancelEdit function.
            element.style.display = displayState[key];
        }
    }


// Edit Rule function
    function editRule(item) {
        // function call passing an Object with corresponding display states
        const displayStates = {
            text: 'none',
            textArea: 'block',
            label: 'block',
            subText: 'none',
            subTextArea: 'block',
            subLabel: 'block',
            editBtn: 'none',
            cancelBtn: 'block',
            confirmBtn: 'block',
            deleteBtn: 'none',
        };

        if (item.classList.contains('info')) {
            const infoStates = {
                title: 'none',
                titleArea: 'block',
                titleLabel: 'block',
                imgRemove: 'block',
                imgForm: 'flex'
            };
            Object.assign(displayStates, infoStates);
        }

        if (item.classList.contains('eats')) {
            const eatsStates = {
                title: 'none',
                titleArea: 'block',
                titleLabel: 'block',
                imgRemove: 'block',
                imgForm: 'flex',
                drive: 'none',
                driveArea: 'block',
                driveLabel: 'block',
                website: 'none',
                websiteArea: 'block',
                websiteLabel: 'block',
                phone: 'none',
                phoneArea: 'block',
                phoneLabel: 'block'
            }
            Object.assign(displayStates, eatsStates)
        }

        toggleRuleDisplay(item, displayStates);

    }    


    function cancelEdit(item) {
        // function call passing an Object with corresponding display states
        const displayStates = {
            text: 'block',
            textArea: 'none',
            label: 'none',
            subText: 'block',
            subTextArea: 'none',
            subLabel: 'none',
            editBtn: 'block',
            cancelBtn: 'none',
            confirmBtn: 'none',
            deleteBtn: 'block'
        }

        if (item.classList.contains('info')) {
            const infoStates = {
                title: 'block',
                titleArea: 'none',
                titleLabel: 'none',
                imgRemove: 'none',
                imgForm: 'none'
            };
            Object.assign(displayStates, infoStates);
        }

        if (item.classList.contains('eats')) {
            const eatsStates = {
                title: 'block',
                titleArea: 'none',
                titleLabel: 'none',
                imgRemove: 'none',
                imgForm: 'none',
                drive: 'block',
                driveArea: 'none',
                driveLabel: 'none',
                website: 'block',
                websiteArea: 'none',
                websiteLabel: 'none',
                phone: 'block',
                phoneArea: 'none',
                phoneLabel: 'none'
            }
            Object.assign(displayStates, eatsStates);
        }

        toggleRuleDisplay(item, displayStates);
    }


    function confirmEdit(item) {
        const text = item.querySelector('.text-edit').value
        const subText = item.querySelector('.subtext-edit').value

        if (item.classList.contains("rule")) {
            const ruleId = item.id;

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
            const title = item.querySelector('.editable > .title-edit').value

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
            editRule(item);
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