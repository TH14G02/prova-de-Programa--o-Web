document.addEventListener('DOMContentLoaded', () => {
    const gerarBtn = document.getElementById('gerarBtn');
    const corInput = document.getElementById('corInput');

    gerarBtn.addEventListener('click', () => {
        // Remove o '#' se o usuário o digitou
        const cor = corInput.value.replace('#', '');
        
        // Redireciona para a rota do backend
        window.location.href = `/gerar-paleta/${cor}`;
    });
});