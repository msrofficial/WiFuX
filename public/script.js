document.addEventListener('DOMContentLoaded', () => {

    // 1. Copy to Clipboard Functionality
    const copyButtons = document.querySelectorAll('.copy-btn');
    
    copyButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const codeElement = btn.nextElementSibling;
            const textToCopy = codeElement.innerText;
            
            navigator.clipboard.writeText(textToCopy).then(() => {
                // Change icon to checkmark
                const icon = btn.querySelector('i');
                icon.className = 'fas fa-check';
                btn.style.color = '#10b981';
                btn.style.borderColor = '#10b981';
                
                // Revert back after 2 seconds
                setTimeout(() => {
                    icon.className = 'far fa-copy';
                    btn.style.color = '';
                    btn.style.borderColor = '';
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy text: ', err);
            });
        });
    });

    // 2. Accordion Functionality for "Fix Superuser"
    const accordionHeader = document.querySelector('.accordion-header');
    if(accordionHeader) {
        accordionHeader.addEventListener('click', () => {
            const accordion = accordionHeader.parentElement;
            accordion.classList.toggle('active');
        });
    }

    // 3. Scroll Reveal Animation
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Trigger only once
            }
        });
    }, observerOptions);

    document.querySelectorAll('.box-reveal').forEach(box => {
        observer.observe(box);
    });

    // Trigger reveal immediately for elements already in viewport
    setTimeout(() => {
        document.querySelectorAll('.box-reveal').forEach(box => {
            const rect = box.getBoundingClientRect();
            if(rect.top < window.innerHeight) {
                box.classList.add('visible');
            }
        });
    }, 100);
});
