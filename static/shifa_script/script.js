// Function to toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

// Function to animate scrolling
function scrollToElement(element) {
    element.scrollIntoView({ behavior: 'smooth' });
}

// Add event listener to toggle theme button
document.getElementById('toggle-theme').addEventListener('click', toggleDarkMode);

// Add event listeners to headings for smooth scrolling
document.querySelectorAll('h1, h2').forEach(heading => {
    heading.addEventListener('click', () => scrollToElement(heading));
});

// Initialize event listeners when the page loads
document.addEventListener('DOMContentLoaded', () => {
    console.log('Page loaded!');
});