document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.phone-number').forEach((phoneNumber) => {
        formatNumber(phoneNumber)
    })

    function formatNumber(phoneNumber) {
        let formattedNumber = phoneNumber.innerHTML.replace(/(\d{3})(\d{3})(\d{4})/, `($1) $2-$3`);
        phoneNumber.innerHTML = formattedNumber
    }

})