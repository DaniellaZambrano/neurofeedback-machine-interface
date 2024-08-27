from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy.NeuroPy()

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None

def theta_callback(theta_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of theta is: ", theta_value)
    return None

def blinkStrength_callback(blinkStrength_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of blinkStrength is: ", blinkStrength_value)
    return None

neuropy.setCallBack("attention", attention_callback)
neuropy.setCallBack("theta", theta_callback)
neuropy.setCallBack("blinkStrength", blinkStrength_callback)
neuropy.start()

try:
    while True:
        sleep(0.2)
finally:
    neuropy.stop()