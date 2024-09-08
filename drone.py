from flask import Flask, render_template, request
import airsim
import threading

app = Flask(__name__)

# Инициализация клиента AirSim
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Глобальные переменные для отслеживания состояния дрона
is_flying_route = False
base_position = airsim.Vector3r(0, 0, -10)

def fly_route():
    global is_flying_route
    is_flying_route = True
    route = [
        airsim.Vector3r(10, 0, -10),
        airsim.Vector3r(10, 10, -10),
        airsim.Vector3r(0, 10, -10),
        airsim.Vector3r(0, 0, -10)
    ]
    for point in route:
        if not is_flying_route:
            break
        client.moveToPositionAsync(point.x_val, point.y_val, point.z_val, 5).join()
    is_flying_route = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/takeoff', methods=['POST'])
def takeoff():
    client.takeoffAsync().join()
    return 'Drone has taken off'

@app.route('/fly_route', methods=['POST'])
def start_fly_route():
    if not is_flying_route:
        threading.Thread(target=fly_route).start()
    return 'Drone is flying the route'

@app.route('/return_to_base', methods=['POST'])
def return_to_base():
    global is_flying_route
    is_flying_route = False
    client.moveToPositionAsync(base_position.x_val, base_position.y_val, base_position.z_val, 5).join()
    return 'Drone is returning to base'

@app.route('/land', methods=['POST'])
def land():
    global is_flying_route
    is_flying_route = False
    client.landAsync().join()
    return 'Drone has landed'

if __name__ == '__main__':
    app.run(debug=True)
