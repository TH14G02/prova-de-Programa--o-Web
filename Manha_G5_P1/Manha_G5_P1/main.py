import os

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<a>')
def oper(a: str):
       
        cor_hex = str(a)
        r = int(cor_hex[0:2], 16)  
        g = int(cor_hex[2:4], 16)  
        b = int(cor_hex[4:6], 16)  
        normal = f"#{a}"
        
        resultado_red_esclarecer = r*1.5
        resultado_green_esclarecer = g*1.5
        resultado_blue_esclarecer = b*1.5

        resultado_red_escurecer = r*0.5
        resultado_green_escurecer = g*0.5
        resultado_blue_escurecer = b*0.5

        lista_escurecer = [resultado_red_escurecer,resultado_green_escurecer,resultado_blue_escurecer]
        
        print(lista_escurecer)
        lista_esclarecer = [resultado_red_esclarecer,resultado_green_esclarecer,resultado_blue_esclarecer]
      
        print(lista_esclarecer)
        
        cor_hex_final_esclarecer = f"#{int(resultado_red_esclarecer):02x}{int(resultado_green_esclarecer):02x}{int(resultado_blue_esclarecer):02x}"
        cor_hex_final_escurecer = f"#{int(resultado_red_escurecer):02x}{int(resultado_green_escurecer):02x}{int(resultado_blue_esclarecer):02x}"
        return render_template('math.html', name =  cor_hex_final_esclarecer, namee =  cor_hex_final_escurecer, name1 = normal )
        




if __name__ == '__main__':
    # Define a porta a partir da variável de ambiente PORT, ou usa 5000 como padrão
    # A porta 80 geralmente requer privilégios de administrador, então 5000 é mais comum para desenvolvimento.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)