// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get form element
    const form = document.getElementById('prediction-form');
    
    // Add validation on form submit
    if (form) {
        form.addEventListener('submit', function(event) {
            // Check if all required fields are filled
            const selectElements = form.querySelectorAll('select[required]');
            let isValid = true;
            
            selectElements.forEach(function(select) {
                if (!select.value) {
                    isValid = false;
                    // Add error styling
                    select.style.borderColor = '#e74c3c';
                    
                    // Create or update error message
                    let errorMsg = select.parentNode.querySelector('.error-message');
                    if (!errorMsg) {
                        errorMsg = document.createElement('div');
                        errorMsg.className = 'error-message';
                        errorMsg.style.color = '#e74c3c';
                        errorMsg.style.fontSize = '0.8rem';
                        errorMsg.style.marginTop = '5px';
                        select.parentNode.appendChild(errorMsg);
                    }
                    errorMsg.textContent = 'This field is required';
                } else {
                    // Remove error styling
                    select.style.borderColor = '#ddd';
                    
                    // Remove error message if exists
                    const errorMsg = select.parentNode.querySelector('.error-message');
                    if (errorMsg) {
                        select.parentNode.removeChild(errorMsg);
                    }
                }
            });
            
            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
                
                // Scroll to the first error
                const firstError = form.querySelector('select[style*="border-color: rgb(231, 76, 60)"]');
                if (firstError) {
                    firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });
        
        // Add input event listeners to clear error styling on input
        const selectElements = form.querySelectorAll('select');
        selectElements.forEach(function(select) {
            select.addEventListener('change', function() {
                if (this.value) {
                    // Remove error styling
                    this.style.borderColor = '#ddd';
                    
                    // Remove error message if exists
                    const errorMsg = this.parentNode.querySelector('.error-message');
                    if (errorMsg) {
                        this.parentNode.removeChild(errorMsg);
                    }
                }
            });
        });
    }
    
    // Add animation to the probability bar on the results page
    const probabilityFill = document.querySelector('.probability-fill');
    if (probabilityFill) {
        // Trigger animation after a small delay
        setTimeout(function() {
            const width = probabilityFill.style.width;
            probabilityFill.style.width = '0%';
            
            setTimeout(function() {
                probabilityFill.style.width = width;
            }, 100);
        }, 300);
    }
    
    // Dynamic behavior for stress level field
    const stressSelect = document.getElementById('stress');
    const stressLevelSelect = document.getElementById('stress_level');
    
    if (stressSelect && stressLevelSelect) {
        // Function to toggle stress level field
        function toggleStressLevel() {
            if (stressSelect.value === 'no') {
                stressLevelSelect.value = '1';
                stressLevelSelect.disabled = true;
                stressLevelSelect.parentNode.style.opacity = '0.6';
            } else {
                stressLevelSelect.disabled = false;
                stressLevelSelect.parentNode.style.opacity = '1';
            }
        }
        
        // Initial call
        toggleStressLevel();
        
        // Set up event listener
        stressSelect.addEventListener('change', toggleStressLevel);
    }
    
    // Reset button functionality
    const resetButton = document.querySelector('.btn-reset');
    if (resetButton) {
        resetButton.addEventListener('click', function() {
            // Remove all error messages
            const errorMessages = document.querySelectorAll('.error-message');
            errorMessages.forEach(function(error) {
                error.parentNode.removeChild(error);
            });
            
            // Reset border colors
            const selectElements = form.querySelectorAll('select');
            selectElements.forEach(function(select) {
                select.style.borderColor = '#ddd';
            });
            
            // Reset stress level field state
            if (stressSelect && stressLevelSelect) {
                setTimeout(toggleStressLevel, 10);
            }
        });
    }
});