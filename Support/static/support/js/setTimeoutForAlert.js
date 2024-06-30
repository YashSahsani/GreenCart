console.log("setTimeoutForAlert.js loaded");
// Your setTimeoutForAlert.js code here

setTimeout(() => {
        const alert = document.getElementById('alert');
        if (alert) {
            alert.style.display = 'none';
        }
    }, 1000);