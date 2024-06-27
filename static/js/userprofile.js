document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.getElementById("editButton");
    const saveButton = document.getElementById("saveButton");
    const profileForm = document.getElementById("profileForm");
    const profileImageWrapper = document.querySelector(".profile-image-wrapper");

    editButton.addEventListener("click", function () {
        // Show the save button and make fields editable
        saveButton.classList.remove("hidden");
        editButton.classList.add("hidden");

        // Enable editing for input fields
        const editableFields = document.querySelectorAll(".editable-field");
        editableFields.forEach(field => field.removeAttribute("readonly"));

        // Add edit mode to profile image wrapper
        profileImageWrapper.classList.add("edit-mode");
    });

    saveButton.addEventListener("click", function () {
        // Hide the save button and disable fields
        saveButton.classList.add("hidden");
        editButton.classList.remove("hidden");

        // Disable editing for input fields
        const editableFields = document.querySelectorAll(".editable-field");
        editableFields.forEach(field => field.setAttribute("readonly", true));

        // Remove edit mode from profile image wrapper
        profileImageWrapper.classList.remove("edit-mode");

        // Submit the form
        profileForm.submit();
    });

    // Handle image upload
    profileImageWrapper.addEventListener("click", function () {
        if (profileImageWrapper.classList.contains("edit-mode")) {
            const imageInput = document.getElementById("imageInput");
            imageInput.click();
        }
    });

    // Display selected image
    const imageInput = document.getElementById("imageInput");
    imageInput.addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                document.getElementById("profileImage").src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});