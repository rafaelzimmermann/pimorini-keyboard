
deploy-circuitpython:
	wget https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2 -O deps/adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2
	cp deps/adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2 /Volumes/RPI-RP2


deploy-hid-lib:
	wget https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20220924/adafruit-circuitpython-bundle-7.x-mpy-20220924.zip -O deps/adafruit-circuitpython-bundle-7.x-mpy-20220924.zip
	unzip deps/adafruit-circuitpython-bundle-7.x-mpy-20220924.zip -d /tmp/hid-lib
	mkdir -p /Volumes/import\ time/lib
	cp -r /tmp/hid-lib/adafruit-circuitpython-bundle-7.x-mpy-20220924/lib/adafruit_hid /Volumes/import\ time/lib/


clean:
	rm -rf /Volumes/import\ time/*.py

deploy: clean
	cp src/*.py /Volumes/import\ time/

