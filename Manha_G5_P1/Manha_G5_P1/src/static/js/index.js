
document.getElementById('calc-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const a =  (document.getElementById('a').value);
            
            window.location.href = `/${a}`;
           
            
           
        });
