

config-pico:
	cp deps/pimoroni-pico-v1.19.6-micropython.uf2 /Volumes/RPI-RP2

env:
	workon pimorini && pip3 install adafruit-ampy

clean:
	ampy --port /dev/tty.usbmodem2201 rm main.py

deploy:
	 ampy --port /dev/tty.usbmodem2201 put src/main.py