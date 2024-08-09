import { handleFormSubmission } from './modules/form-handler.js';
import { toggleDarkMode } from './modules/dark-mode-toggle.js';
import { filterProjects } from './modules/project-filter.js';

document.addEventListener('DOMContentLoaded', () => {
    // Initialize form handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleFormSubmission);
    }

    // Initialize dark mode toggle
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', toggleDarkMode);
    }

    // Initialize project filtering
    const projectFilter = document.getElementById('project-filter');
    if (projectFilter) {
        projectFilter.addEventListener('change', filterProjects);
    }
});