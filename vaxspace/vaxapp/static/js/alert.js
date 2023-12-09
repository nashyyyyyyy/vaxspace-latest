document.addEventListener('DOMContentLoaded', function () {
    let alerts = document.querySelectorAll('.s_alert');
    
    alerts.forEach(function (s_alert) {
        let delay = 3000; // Set the delay in milliseconds (here, 5 seconds)

        setTimeout(function () {
            s_alert.classList.add('fade');
            setTimeout(function () {
                s_alert.remove(); // Remove the alert after the fade out effect
            }, 1000); // Time for fade out (adjust according to transition duration in CSS)
        }, delay);
    });
});