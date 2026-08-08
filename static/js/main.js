// Mensaje para Console
console.log("Hola! 👋\n\nSi estás viendo esto, probablemente estás interesado en ver el código este proyecto.\n\nEncontralo en GitHub: https://github.com/gomeznieto/foobarcode\n\nSi querés colaborar, ¡no dudes en hacer un fork y enviar un pull request!\n\n¡Gracias por tu interés!");

// Copy-clipboard
function copyToClipboard() {
    const textarea = document.getElementById('html-result');
    const copyBtn = document.getElementById('copy-btn');

    navigator.clipboard.writeText(textarea.value).then(function() {
        const originalText = copyBtn.innerHTML;
        const originalBg = copyBtn.style.backgroundColor;
        copyBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <polyline points="20 6 9 17 4 12"></polyline></svg> <span>¡Copiado!</span>';
        copyBtn.style.backgroundColor = '#a6e3a1';
        copyBtn.style.color = '#1e1e2e';
        setTimeout(function() {
            copyBtn.innerHTML = originalText;
            copyBtn.style.backgroundColor = originalBg;
            copyBtn.style.color = '';
        }, 2000);
    }, function(err) {
            console.error('Error al copiar: ', err);
            alert('Error al copiar al portapapeles');
        });
}

const copyBtn = document.getElementById('copy-btn');
if (copyBtn) {
    copyBtn.addEventListener('click', copyToClipboard);
}

// Load-files
document.getElementById('file').addEventListener('change', () => {
    document.getElementById("form").submit();
})

// toggle-mode
const themeToggle = document.getElementById('theme-toggle');
const htmlElement = document.documentElement;

function updateThemeUI() {
    if (htmlElement.classList.contains('dark')) {
        themeToggle.textContent = '☀️';
    } else {
        themeToggle.textContent = '🌙';
    }
}

const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    if (savedTheme === 'light') {
        htmlElement.classList.remove('dark');
        editor.setOption("theme", "default");

    } else {
        htmlElement.classList.add('dark');
        editor.setOption("theme", "dracula");

    }
} else {
    htmlElement.classList.add('dark');
    editor.setOption("theme", "dracula");
}
updateThemeUI();

themeToggle.addEventListener('click', () => {
    htmlElement.classList.toggle('dark');
    const newTheme = htmlElement.classList.contains('dark') ? 'dark' : 'light';

    editor.setOption("theme", newTheme === 'dark' ? "dracula" : "default");

    localStorage.setItem('theme', newTheme);
    updateThemeUI();
});

// Current-year
const year = document.getElementById("year")
year.innerText = new Date().getFullYear();

// Clean-Code
document.addEventListener("click", (e) => {
    if(e.target.matches('#clean-btn')){
        window.location.href = "/"; 
    }
})

