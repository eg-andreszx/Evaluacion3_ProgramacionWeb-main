
let carrito = [];

document.querySelectorAll('.agregar-carrito').forEach(button => {
  button.addEventListener('click', () => {
    const producto = {
      nombre: button.getAttribute('data-nombre'),
      precio: button.getAttribute('data-precio'),
      cantidad: 1
    };

    // Agregar producto al carrito
    carrito.push(producto);

    // Guardar en localStorage
    localStorage.setItem('carrito', JSON.stringify(carrito));

    alert('Producto agregado al carrito');
  });
});

// Cargar el carrito desde localStorage al iniciar la página
document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('carrito')) {
    carrito = JSON.parse(localStorage.getItem('carrito'));
  }
});
