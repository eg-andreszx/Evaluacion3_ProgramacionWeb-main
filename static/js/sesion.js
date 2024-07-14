$(document).ready(function() {
  $('#registerForm').submit(function(event) {
    event.preventDefault();
    var nombre = $('#nombre').val();
    var apellido = $('#apellido').val();
    var rut = $('#rut').val();
    var email = $('#email').val();
    var password = $('#password').val();

    if (nombre === '' || apellido === '' || rut === '' || email === '' || password === '') {
      alert('Todos los campos son obligatorios.');
      return;
    }

    if (!validateEmail(email)) {
      alert('Por favor, introduce un correo electrónico válido.');
      return;
    }

    // Almacenar los datos del usuario en el localStorage
    localStorage.setItem('nombre', nombre);
    localStorage.setItem('apellido', apellido);
    localStorage.setItem('rut', rut);
    localStorage.setItem('email', email);
    localStorage.setItem('password', password);

    alert('Registro exitoso.');
  });

  $('#loginForm').submit(function(event) {
    event.preventDefault();
    var email = $('#emailLogin').val();
    var password = $('#passwordLogin').val();

    if (email === '' || password === '') {
      alert('Todos los campos son obligatorios.');
      return;
    }

    if (!validateEmail(email)) {
      alert('Por favor, introduce un correo electrónico válido.');
      return;
    }

    // Verificar las credenciales del usuario almacenadas en el localStorage
    var storedEmail = localStorage.getItem('email');
    var storedPassword = localStorage.getItem('password');

    if (email === storedEmail && password === storedPassword) {
      alert('Inicio de sesión exitoso.');
    } else {
      alert('Correo electrónico o contraseña incorrectos.');
    }
  });

  function validateEmail(email) {
    var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }
});
