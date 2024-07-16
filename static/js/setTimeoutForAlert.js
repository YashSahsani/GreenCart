setTimeout(() => {
  const alert = document.getElementById("alert");
  if (alert) {
    alert.style.display = "none";
    alert.style.hidden = true;
  }
}, 500);

function showModal(productId, productName, productImage) {
  document.getElementById("modal-product-id").value = productId;
  document.getElementById("modal-product-name").textContent = productName;
  document.getElementById("modal-product-image").src = productImage;
  document.getElementById("deleteModal").classList.remove("hidden");
}

function hideModal() {
  document.getElementById("deleteModal").classList.add("hidden");
}
