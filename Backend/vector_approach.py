import math
def calcular_angulo(A, B):
    diff_x = B[0] - A[0]
    diff_y = B[1] - A[1]
    ang_rad = math.atan2(diff_y, diff_x)
    ang_deg = math.degrees(ang_rad)
    return ang_deg

def calcular_vector(A, B):
    vector_AB = (B[0] - A[0], B[1] - A[1])
    return vector_AB

def calcular_nuevo_punto(A, w):
    longitud_w = math.sqrt(w[0]**2 + w[1]**2)
    unitario_w = (w[0] / longitud_w, w[1] / longitud_w)

    # Sumar el punto A y el vector unitario escalado
    nuevo_punto = (A[0] + unitario_w[0], A[1] + unitario_w[1])
    return nuevo_punto

destino = (5, 5)
actual = (0, 0)
dest_changed = False
wants_stop = False
while actual != destino and not dest_changed and not wants_stop:
  angulo = calcular_angulo(actual, destino)
  vector_movimiento = calcular_vector(actual, destino)
  new_point = calcular_nuevo_punto(actual, vector_movimiento) # change to GPS location

  # change
  actual = new_point