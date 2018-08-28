import ssl
import sys

import paho.mqtt.client
import paho.mqtt.publish

def on_connect(client, userdata, flags, rc):
	print('connected')

def main():
	paho.mqtt.publish.single(
		topic='test',
		payload='hi',
		qos=2,
		hostname='45.35.48.219'
		#port=8883,
		#client_id='[clientid]'
		# auth={
		# 	'username': '[username]',
		# 	'password': '[password]'
		# },
		# tls={
		# 	'ca_certs': '/etc/ssl/certs/DST_Root_CA_X3.pem',
		# 	'tls_version': ssl.PROTOCOL_TLSv1_2
		# }
	)

if __name__ == '__main__':
	main()
	sys.exit(0)