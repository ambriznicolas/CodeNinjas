document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
 
    // Form fields name, email, message, feedback 
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    const feedback = document.getElementById('formFeedback');
 
    // Simple validation
    if (name === '' || email === '' || message === '') {
       feedback.textContent = 'All fields are required!';
       feedback.className = 'form-feedback error';
       feedback.style.display = 'block';
       return;
    }
 
    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
       feedback.textContent = 'Please enter a valid email address.';
       feedback.className = 'form-feedback error';
       feedback.style.display = 'block';
       return;
    }
 
    // Success message
    feedback.textContent = 'Thank you for your message!';
    feedback.className = 'form-feedback success';
    feedback.style.display = 'block';
 
    // Clear the form after successful submission
    document.getElementById('contactForm').reset();
 
    // Hide feedback after a few seconds
    setTimeout(() => {
       feedback.style.display = 'none';
    }, 3000);
 });