import serial, time

def connect():
  try:
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1)

  except Exception:
    print('No se pudo conectar al puerto serie')
    arduino = None

  finally:
    return arduino


def read_potentiometer(arduino):
  try:
    data = arduino.readline().decode('utf-8')
    data = int(data)

  except KeyboardInterrupt:
    arduino.close()
  except UnicodeDecodeError:
    return None
  except ValueError:
    return None
  except Exception:
    return None
  else:
    return data


def write_led(arduino, led):
  cad = f'{led.get_text()} {led.checked()}'
  arduino.write(cad.encode())
