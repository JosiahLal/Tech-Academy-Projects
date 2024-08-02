document.addEventListener('DOMContentLoaded', () => {
    const box = document.querySelector('.animated-box');
    box.addEventListener('mouseover', () => {
        box.style.backgroundColor = '#4682b4';
    });
    box.addEventListener('mouseout', () => {
        box.style.backgroundColor = '#ff6347';
    });
});
