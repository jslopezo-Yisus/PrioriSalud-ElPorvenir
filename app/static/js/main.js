// Interacciones pequeñas de la interfaz. La lógica de negocio se gestiona en Flask.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-confirm]").forEach((element) => {
    element.addEventListener("click", (event) => {
      if (!window.confirm(element.dataset.confirm)) event.preventDefault();
    });
  });
});
