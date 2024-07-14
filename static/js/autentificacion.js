document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Perform simple validation
    if (email === "" || password === "") {
        document.getElementById('error-message').innerText = "Please fill in all fields.";
        return;
    }

    fetch("{% url 'login' %}", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Login successful!");
            window.location.href = "{% url 'usuarios_list' %}";
        } else {
            document.getElementById('error-message').innerText = "Invalid email or password.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
