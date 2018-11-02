#!/usr/bin/env python
# -*- coding: utf-8 -*-

import location_pb2
import requests
import random
import struct


macs = ["b4:5d:50:94:39:b3", "98:1:a7:e6:85:70"] #add multiple format parsing
save = True

SERVICE_URL = 'https://{}.apple.com/clls/wloc'
SERVICE_SHOST = ['iphone-services', 'gs-loc']
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'locationd/1756.1.15 CFNetwork/711.5.6 Darwin/14.0.0'}

URL = SERVICE_URL.format(SERVICE_SHOST[random.choice([True, False])])


class Header:	#TODO: allow passing parameters
	def __init__(self):
		self.HEADER = self.__data()
	
	def __data(self): 
		NUL_SQH = "\x00\x01"                                                                            # NUL SOH      /* 0x0001 start of header */
		NUL_NUL = "\x00\x00"                                                                            # NUL NUL      /* 0x0000 end of header */
		llength = "\x00\x05"                                                                            # [length]     /* length of the locale string in bytes */
		locale = "\x65\x6E\x5F\x55\x53"                                                                 # [locale]     /* en_US */
		ilength = "\x00\x13"                                                                            # [length]     /* length of the identifier string in bytes */
		identifier = "\x63\x6F\x6D\x2E\x61\x70\x70\x6c\x65\x2e\x6c\x6f\x63\x61\x74\x69\x6f\x6e\x64"     # [identifier] /* com.apple.locationd */
		vlength = "\x00\x0c"                                                                            # [length]     /* length of the version string in bytes
		version = "\x38\x2e\x34\x2e\x31\x2e\x31\x32\x48\x33\x32\x31"                                    # [version]    /* 8.4.1.12H321 ie. ios version and build */

		return NUL_SQH + llength + locale + ilength + identifier + vlength + version + NUL_NUL + NUL_SQH +  NUL_NUL

header = (Header().HEADER)


def query(URL, DATA, HEADERS):

	response = requests.post(url=URL, data=DATA, headers=HEADERS)
	data = response.text
	data_buffer= response.text[(data.find(b'\x00\x00\x00\x01\x00\x00') + 8):] #+2 bc of the size bytes

	return data_buffer, response


def reqpay(macs, noise=0, signal=100):

	Request = location_pb2.Request()
	Request.noise = noise
	Request.signal = signal
	for MAC in macs:
		Request.wifis.add(mac=MAC)

	message = (Request.SerializeToString())
	size = struct.pack('>h', len(message)) #big-endian Signed Short (16bit)
	
	return header + size + message

def resread(Buffer):

	Response = location_pb2.Response()
	Response.ParseFromString(Buffer)

	for Wifi in Response.wifis:

		mac = Wifi.mac
		print('BSID MAC: %s' % mac)
		channel = Wifi.channel

		lat = Wifi.location.latitude
		lng = Wifi.location.longitude
		accuracy = Wifi.location.accuracy
		altitude = Wifi.location.altitude

		print('\tLatitude: %s' % str(int(lat) * pow(10, -8)))
		print('\tLongitude: %s' % str(int(lng) * pow(10, -8)))
		print('\tAccuracy Radius: %s' % accuracy)
		print('\tAltitude: %s' % altitude)
		
		if Wifi.location.HasField('altitudeAccuracy'):
			print('\tAltitude Accuracy: %s' % Wifi.location.altitudeAccuracy)
		
		print('Channel: %s\n\n' % channel)




DATA = reqpay(macs, 0, 100)

Buffer = query(URL, DATA, HEADERS)[0]
resread(Buffer)





if save == True:
	with open('request.bin', 'wb') as f:
		f.write(DATA)
	#with open('responseb.bin', 'wb') as f:
	#	f.write(OUT[0])
else:
	pass










