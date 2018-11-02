#!/usr/bin/env python
# -*- coding: utf-8 -*-

import location_pb2
import urllib2
import random
import time
import argparse
import struct
import sys


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

	req = urllib2.Request(URL, DATA)

	req.add_header("User-Agent", HEADERS['User-Agent'])
	req.add_header("Content-type", HEADERS['Content-Type'])

	#req.add_header("Accept","*/*")
	#req.add_header("Accept-Language","en-us")
	#req.add_header("Accept-Encoding","gzip, deflate")
	#req.add_header("Accept-Charset","utf-8")

	handle = urllib2.urlopen(req)
	data = handle.read()
	data_buffer= data[(data.find(b'\x00\x00\x00\x01\x00\x00') + 8):] #+2 bc of the size bytes

	return data_buffer, data

	"""
	response = requests.post(url=URL, data=DATA, headers=HEADERS)
	data = response.text
	data_buffer= response.text[(data.find(b'\x00\x00\x00\x01\x00\x00') + 8):] 

	return data_buffer, response
	"""


def reqpay(macs, noise=0, signal=100):

	Request = location_pb2.Request()
	Request.noise = noise
	Request.signal = signal
	for MAC in macs:
		Request.wifis.add(mac=MAC)

	message = (Request.SerializeToString())
	size = struct.pack('>h', len(message)) #big-endian Signed Short (16bit)
	
	return header + size + message


def resread(Buffer, KML):

	Response = location_pb2.Response()
	Response.ParseFromString(Buffer)

	narray = []

	for Wifi in Response.wifis:
		if Wifi.location.latitude != 18446744055709551616:
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

			if KML == True:
				narray.append([mac, lat, lng])

	
	if KML == True:
		with open("KML.kml", "w") as f:
			f.write("<KML_File>\n")
			f.write("<Document>\n")
			for array in narray:
				f.write("\t<Placemark>\n")
				f.write("\t\t<decription>" + str(array[0]) + "</description>\n")
				f.write("\t\t<Point>\n")
				f.write("\t\t\t<coordinates>" + str(array[1]) + str(array[2]) + "</coordinates>\n")
				f.write("\t\t</Point>\n")
				f.write("\t</Placemark>\n")
			f.write("</Document>\n")
			f.write("</kml>\n")


def dbcall(macs, noise, signal, save, KML):
	DATA = reqpay(macs, 0, 100)

	Buffer = query(URL, DATA, HEADERS)[0]
	resread(Buffer, KML)

	if save:
		with open('buffer.bin', "wb") as f:
  			f.write(Buffer)

dbcall([str(sys.argv[1])], 0 ,100, False, True)


"""
def parsein():

	global MACS, SIGNAL, NOISE, KML, SAVE

	parser = argparse.ArgumentParser(description='https://github.com/zadewg/GS-LOC/')
	parser.add_argument('-m','--mac', nargs='+', help='Mac Address', required=True)
	parser.add_argument('-n','--noise', help='Mac Address', required=False)
	parser.add_argument('-g','--signal', help='Mac Address', required=False)
	parser.add_argument('-k','--kml', nargs='+', help='Generate KML file', action='store_true')
	parser.add_argument('-s','--save', help='File to write to', action='store_true')
	args = vars(parser.parse_args())

	MACS = args['mac']
	NOISE = args['noise'] or False
	SIGNAL = args['signal'] or False
	SAVE = args['save'] 
	KML = args['kml'] 


def main():

	print("   ________  _________         .____    ________  _________    ")
	print("  /  _____/ /   _____/         |    |   \_____  \ \_   ___ \   ")
	print(" /   \  ___ \_____  \   ______ |    |    /   |   \/    \  \/   ")
	print(" \    \_\  \/        \ /_____/ |    |___/    |    \     \____  ")
	print("  \______  /_______  /         |_______ \_______  /\______  /  ")
	print("         \/        \/                  \/       \/        \/   ")

	print("\n github.com/zadewg/GS-LOC/ :: Ofensive Intelligence Gathering")
	print("\n Apple Geolocation Services RE. Database Scraper     \n\n\n\n")

	time.sleep(2)
	#parsein()
	dbcall(MACS, 0 ,100, False, True)

"""




