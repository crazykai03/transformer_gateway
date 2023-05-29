import time
import json
from azure.iot.device import IoTHubDeviceClient

RECEIVED_MESSAGES = 0

CONNECTION_STRING = "HostName=ess-iot-hub.azure-devices.net;DeviceId=device01;SharedAccessKey=qFY0/xZADhM1n60DFqJDeY+HuV0otlW0J4ZTVZn46Q4="

def message_handler(message):
    res = json.loads(message.data.decode('ascii'))
    print(res['topic'])
    print(res['action'])




def main():
    print ("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = message_handler

        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()

if __name__ == '__main__':
    main()