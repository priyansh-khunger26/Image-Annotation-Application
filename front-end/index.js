function fetchClassAndDisplayOverlay(imgSrc, imgId) {
    fetch(`/api/images/get_class/${imgId}`)
    .then(response => response.json())
    .then(data => {
        const className = data.class_name;
        overlay.innerHTML = `
            <div>
                <img src="${imgSrc}" class="enlarged-img" style="display:block; max-width:90%; margin:auto;">
                <input type="text" id="img-class" value="${className}" style="margin: 10px auto; display:block;">
                <button onclick="updateClassName(${imgId})">Update Class</button>
            </div>
        `;
        overlay.style.display = 'flex';
    })
    .catch(error => console.error('Error:', error));
}

window.updateClassName = function(imgId) {
    const newClass = document.getElementById('img-class').value;
    // Update the class name on the server
    fetch(`/api/images/update_class/${imgId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ class_name: newClass })
    })
    .then(response => {
        if (response.ok) {
            alert('Class updated successfully!');
            overlay.style.display = 'none'; // Close overlay
        } else {
            throw new Error('Failed to update class.');
        }
    })
    .catch(error => console.error('Error:', error));
};

overlay.addEventListener('click', function() {
    this.style.display = 'none';  // Hide the overlay when clicked
});













function onImageClick(imageId, currentClassName) {
    const newClassName = prompt("Enter new class name:", currentClassName);
    if (newClassName !== null) {
        saveClassName(imageId, newClassName);
    }
}

function saveClassName(imageId, newClassName) {
    const data = {
        class_name: newClassName
    };

    fetch(`/api/images/${imageId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Update UI to reflect the changes if needed
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}