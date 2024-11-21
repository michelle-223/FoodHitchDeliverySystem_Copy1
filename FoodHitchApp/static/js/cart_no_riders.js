document.addEventListener('DOMContentLoaded', function () {
    const checkoutForm = document.getElementById('checkout-form');
    const noAvailableRidersElement = document.getElementById('no-available-riders');
    const noAvailableRiders = noAvailableRidersElement.dataset.noAvailableRiders === 'true';

    // Attach event listener for the checkout button click
    checkoutForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent immediate form submission

        if (noAvailableRiders) {
            Swal.fire({
                title: 'Please try again later',
                text: 'No available riders are currently online. You cannot proceed to checkout.',
                icon: 'warning',
                confirmButtonText: 'OK',
                confirmButtonColor: '#009914'
            }).then(function () {
                // Reload the current page (stay on the cart page)
                window.location.reload();
            });
        } else {
            // If there are available riders, submit the form
            checkoutForm.submit();
        }
    });
});
