from flask import Flask, render_template, request
import airsim

app = Flask(__name__)

# Инициализация клиента AirSim
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/takeoff', methods=['POST'])
def takeoff():
    client.takeoffAsync().join()
    return 'Drone has taken off'

@app.route('/fly_route', methods=['POST'])
def fly_route():
    # Пример маршрута
    route = [
        airsim.Vector3r(10, 0, -10),
        airsim.Vector3r(10, 10, -10),
        airsim.Vector3r(0, 10, -10),
        airsim.Vector3r(0, 0, -10)
    ]
    for point in route:
        client.moveToPositionAsync(point.x_val, point.y_val, point.z_val, 5).join()
    return 'Drone is flying the route'

@app.route('/return_to_base', methods=['POST'])
def return_to_base():
    client.moveToPositionAsync(0, 0, -10, 5).join()
    return 'Drone is returning to base'

@app.route('/land', methods=['POST'])
def land():
    client.landAsync().join()
    return 'Drone has landed'

if __name__ == '__main__':
    app.run(debug=True)
