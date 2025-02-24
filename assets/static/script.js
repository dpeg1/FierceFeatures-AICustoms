// Fetch and load images dynamically
function loadLashImages() {
    const style = document.getElementById('lash-style').value;
    const length = document.getElementById('lash-length').value;
    const curl = document.getElementById('lash-curl').value;
    const thickness = document.getElementById('lash-thickness').value;
    const container = document.getElementById('lash-preview');
    container.innerHTML = ''; // Clear previous images

    // Fetch image paths from backend
    fetch('/get-lash-images/')
        .then(response => response.json())
        .then(data => {
            data[style].forEach(imagePath => {
                if (
                    imagePath.includes(length) &&
                    imagePath.includes(curl) &&
                    imagePath.includes(thickness)
                ) {
                    const img = document.createElement('img');
                    img.src = `/static/${imagePath}`;
                    img.alt = style;
                    container.appendChild(img);
                }
            });
        })
        .catch(error => console.error('Error:', error));
}

// Event Listeners for Dynamic Loading
document.getElementById('lash-style').addEventListener('change', loadLashImages);
document.getElementById('lash-length').addEventListener('change', loadLashImages);
document.getElementById('lash-curl').addEventListener('change', loadLashImages);
document.getElementById('lash-thickness').addEventListener('change', loadLashImages);
// Show Loading Spinner
function showLoading() {
    const container = document.getElementById('lash-preview');
    container.innerHTML = '<div class="loading-spinner"></div>';
}

// Hide Loading Spinner
function hideLoading() {
    const spinner = document.querySelector('.loading-spinner');
    if (spinner) spinner.remove();
}

// Fetch and load images dynamically
function loadLashImages() {
    const style = document.getElementById('lash-style').value;
    const length = document.getElementById('lash-length').value;
    const curl = document.getElementById('lash-curl').value;
    const thickness = document.getElementById('lash-thickness').value;
    const container = document.getElementById('lash-preview');

    // Show loading spinner while fetching images
    showLoading();

    // Fetch image paths from backend
    fetch('/get-lash-images/')
        .then(response => response.json())
        .then(data => {
            hideLoading();
            container.innerHTML = ''; // Clear previous images

            data[style].forEach(imagePath => {
                if (
                    imagePath.includes(length) &&
                    imagePath.includes(curl) &&
                    imagePath.includes(thickness)
                ) {
                    const img = document.createElement('img');
                    img.src = `/static/${imagePath}`;
                    img.alt = style;
                    container.appendChild(img);
                }
            });
        })
        .catch(error => {
            hideLoading();
            console.error('Error:', error);
            container.innerHTML = '<p style="color:red;">Error loading images. Please try again.</p>';
        });
}

// Event Listeners for Dynamic Loading
document.getElementById('lash-style').addEventListener('change', loadLashImages);
document.getElementById('lash-length').addEventListener('change', loadLashImages);
document.getElementById('lash-curl').addEventListener('change', loadLashImages);
document.getElementById('lash-thickness').addEventListener('change', loadLashImages);
// Multi-Selection Mode Toggle
let multiSelection = false;
document.getElementById('multi-selection').addEventListener('change', (event) => {
    multiSelection = event.target.checked;
    loadLashImages();
});

// Reset Button Functionality
document.getElementById('reset-button').addEventListener('click', () => {
    document.getElementById('lash-style').selectedIndex = 0;
    document.getElementById('lash-length').selectedIndex = 0;
    document.getElementById('lash-curl').selectedIndex = 0;
    document.getElementById('lash-thickness').selectedIndex = 0;
    document.getElementById('multi-selection').checked = false;
    multiSelection = false;
    document.getElementById('lash-preview').innerHTML = '<p>Select options to preview lashes...</p>';
});

// Update loadLashImages Function for Multi-Selection Mode
function loadLashImages() {
    const style = document.getElementById('lash-style').value;
    const length = document.getElementById('lash-length').value;
    const curl = document.getElementById('lash-curl').value;
    const thickness = document.getElementById('lash-thickness').value;
    const container = document.getElementById('lash-preview');

    // Show loading spinner while fetching images
    showLoading();

    // Fetch image paths from backend
    fetch('/get-lash-images/')
        .then(response => response.json())
        .then(data => {
            hideLoading();
            container.innerHTML = ''; // Clear previous images

            if (multiSelection) {
                Object.keys(data).forEach(category => {
                    data[category].forEach(imagePath => {
                        if (
                            imagePath.includes(length) &&
                            imagePath.includes(curl) &&
                            imagePath.includes(thickness)
                        ) {
                            const img = document.createElement('img');
                            img.src = `/static/${imagePath}`;
                            img.alt = category;
                            container.appendChild(img);
                        }
                    });
                });
            } else {
                data[style].forEach(imagePath => {
                    if (
                        imagePath.includes(length) &&
                        imagePath.includes(curl) &&
                        imagePath.includes(thickness)
                    ) {
                        const img = document.createElement('img');
                        img.src = `/static/${imagePath}`;
                        img.alt = style;
                        container.appendChild(img);
                    }
                });
            }
        })
        .catch(error => {
            hideLoading();
            console.error('Error:', error);
            container.innerHTML = '<p style="color:red;">Error loading images. Please try again.</p>';
        });
}
// Zoom on Hover Animation
document.addEventListener('mouseover', function (event) {
    if (event.target.tagName === 'IMG' && event.target.parentElement.id === 'lash-preview') {
        event.target.style.transform = 'scale(1.2)';
    }
});

document.addEventListener('mouseout', function (event) {
    if (event.target.tagName === 'IMG' && event.target.parentElement.id === 'lash-preview') {
        event.target.style.transform = 'scale(1)';
    }
});
// Fetch and load images dynamically with Lazy Loading
function loadLashImages() {
    const style = document.getElementById('lash-style').value;
    const length = document.getElementById('lash-length').value;
    const curl = document.getElementById('lash-curl').value;
    const thickness = document.getElementById('lash-thickness').value;
    const container = document.getElementById('lash-preview');

    // Show loading spinner while fetching images
    showLoading();

    // Fetch image paths from backend
    fetch('/get-lash-images/')
        .then(response => response.json())
        .then(data => {
            hideLoading();
            container.innerHTML = ''; // Clear previous images

            data[style].forEach(imagePath => {
                if (
                    imagePath.includes(length) &&
                    imagePath.includes(curl) &&
                    imagePath.includes(thickness)
                ) {
                    const img = document.createElement('img');
                    img.dataset.src = `/static/${imagePath}`;
                    img.alt = style;
                    img.classList.add('lazy-load');
                    container.appendChild(img);
                }
            });

            // Apply Lazy Loading
            const lazyImages = document.querySelectorAll('.lazy-load');
            const lazyObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy-load');
                        observer.unobserve(img);
                    }
                });
            });

            lazyImages.forEach(image => {
                lazyObserver.observe(image);
            });
        })
        .catch(error => {
            hideLoading();
            console.error('Error:', error);
            container.innerHTML = '<p style="color:red;">Error loading images. Please try again.</p>';
        });
}
