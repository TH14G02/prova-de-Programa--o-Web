import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')


def hex_para_rgb(cor_hex):
    """Converte uma cor hexadecimal para uma tupla RGB."""
    # Remove o '#' se ele existir, usando fatiamento de string
    if cor_hex.startswith('#'):
        cor_hex = cor_hex[1:]
    return tuple(int(cor_hex[i:i+2], 16) for i in (0, 2, 4)) # Converte pares de hex para inteiros


def rgb_para_hex(rgb):
    """Converte uma tupla RGB para uma string hexadecimal."""
    # Garante que os valores estão no intervalo 0-255
    r, g, b = [max(0, min(255, int(c))) for c in rgb]
    return f"#{r:02x}{g:02x}{b:02x}"


def gerar_variacoes(cor_hex):
    """Gera uma versão mais clara e uma mais escura de uma cor."""
    try:
        # Validação simples para garantir que o código hex tenha 6 caracteres
        if len(cor_hex.replace('#', '')) != 6:
            return None, None, None

        rgb_original = hex_para_rgb(cor_hex)
        fator_clarear = 1.3
        fator_escurecer = 0.7

        rgb_claro = tuple(c * fator_clarear for c in rgb_original)
        rgb_escuro = tuple(c * fator_escurecer for c in rgb_original)

        cor_original_hex = rgb_para_hex(rgb_original)
        cor_clara_hex = rgb_para_hex(rgb_claro)
        cor_escura_hex = rgb_para_hex(rgb_escuro)
        return cor_clara_hex, cor_original_hex, cor_escura_hex
    except (ValueError, IndexError):
        # Retorna None se a cor hexadecimal for inválida
        return None, None, None


@app.route('/')
def index():
    """Renderiza a página inicial."""
    return render_template('index.html')


@app.route('/gerar-paleta/<string:cor_hex>')
def gerar_paleta(cor_hex):
    """Gera a paleta de cores e renderiza a página de resultado."""
    cor_clara, cor_original, cor_escura = gerar_variacoes(cor_hex)

    if cor_original is None:
        return redirect(url_for('index'))

    return render_template('resultado.html', cor_clara=cor_clara, cor_original=cor_original, cor_escura=cor_escura)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001)) # Usando uma porta diferente (5001) para evitar conflito
    app.run(debug=True, host='0.0.0.0', port=port)