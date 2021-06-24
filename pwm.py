import RPi.GPIO as GPIO
import time

output_pin = 13 #Has to be configured
print(f"Pwm pin:{output_pin}")
led_pin = 7
print(f"Led pin:{output_pin}")

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)
    p = GPIO.PWM(output_pin, 50)
    print(f"P object {p}")
    p.start(0)

    try:
        print(f"Led on:")
        GPIO.output(led_pin, True)
        time.sleep(5)
        print(f"Led off:")
        GPIO.output(led_pin, False)

        print(f"PWM 10")
        p.ChangeDutyCycle(10)
        time.sleep(10)
        print(f"PWM 90")
        p.ChangeDutyCycle(90)
        time.sleep(10)

    finally:

        p.stop()
        GPIO.cleanup()

if __name__=='__main__':

    main()