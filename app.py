from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)

# Configuración de la conexión a Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/calificaciones', methods=['POST'])
def guardar_calificacion():
    data = request.get_json()

    if not data or 'usuarioId' not in data or 'peliculaId' not in data or 'calificacion' not in data:
        return jsonify({'error': 'Datos inválidos'}), 400

    usuario_id = data['usuarioId']
    pelicula_id = data['peliculaId']
    calificacion = data['calificacion']

    # Genera una clave única para Redis
    clave_redis = f'calificacion:{usuario_id}:{pelicula_id}:{calificacion}'

    # Almacena los datos en Redis
    redis_client.set(clave_redis, json.dumps(data))

    return jsonify({'mensaje': 'Calificación guardada exitosamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)
