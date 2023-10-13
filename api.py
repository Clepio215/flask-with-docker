from flask import Flask
from flask import jsonify
from flask import request
import os

app = Flask(__name__)

@app.route('/ivaproductos', methods=['POST'])
def ivaproductos():
    nmproducto = request.json["Nombre del Producto : "]
    tpproducto = request.json["Tipo de producto : "]
    valor = request.json["Valor Sin Iva"]
    
    if(tpproducto=="Café" or tpproducto=="Harina" or tpproducto=="Pastas" or tpproducto=="Embutidos" ):
        valoriva = valor* 0.05 
        valortotal = valoriva + valor
        return jsonify({" Precio con iva es ": valortotal})

    elif(tpproducto=="Licores" or tpproducto=="Cereales" or tpproducto=="Aceites" or tpproducto=="Condimentos" ):
        valoriva = valor* 0.19 
        valortotal = valoriva + valor
        return jsonify({" Precio con iva es ": valortotal})

    elif(tpproducto=="Carne" or tpproducto=="Pescado" or tpproducto=="Leche" or tpproducto=="Queso" ):
        valoriva = valor
        valortotal = valoriva + valor
        return jsonify({" Precio con iva es ": valortotal})

    else:
        return jsonify({"error": 0})

if (__name__ == "__main__"):
    puerto = int(os.environ.get('PORT', 2150))
    app.run(debug=True, host='0.0.0.0', port=puerto )