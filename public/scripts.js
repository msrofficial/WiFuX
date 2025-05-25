// Clipboard copy functionality
document.querySelectorAll('.copy-btn').forEach(button => {
    button.addEventListener('click', () => {
        const textToCopy = button.dataset.copy;
        
        navigator.clipboard.writeText(textToCopy).then(() => {
            // Create toast element
            const toast = document.createElement('div');
            toast.className = 'toast align-items-center text-bg-success border-0';
            toast.setAttribute('role', 'alert');
            toast.style.position = 'fixed';
            toast.style.top = '1rem';
            toast.style.right = '1rem';
            toast.style.zIndex = '1055';
            
            // Toast content
            toast.innerHTML = `
                <div class="d-flex">
                    <div class="toast-body">Copied to clipboard!</div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>`;
            
            // Add to DOM
            document.body.appendChild(toast);
            
            // Initialize Bootstrap toast
            const bootstrapToast = new bootstrap.Toast(toast, { delay: 2000 });
            bootstrapToast.show();
            
            // Remove toast after hiding
            toast.addEventListener('hidden.bs.toast', () => {
                toast.remove();
            });
        }).catch(err => {
            console.error('Failed to copy text: ', err);
        });
    });
});

// Scroll animation for sections
document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");
    
    const observerOptions = {
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        observer.observe(section);
    });
});
