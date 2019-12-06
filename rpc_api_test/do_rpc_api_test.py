# -*-encoding: utf-8-*-
import unittest
import json
import requests
import re
import os
URL = "http://127.0.0.1:8765"
import time
os.popen("canonchain --daemon --rpc --rpc_control --network=4 --data_path=rpc_api_test --witness --witness_account=rpc_api_test/czr_3tiy2jgoUENkszPjrHjQGfmopqwV5m9BcEh2Grb1zDYgSGnBF7.json --password=123 &")
time.sleep(0.3)

#Judge account number, czr_start, remove I, O, l, 0, length greater than or equal to 50
def is_account(str):
	if re.findall(r'czr_[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{50,}$',str):
		return True
	else:
		return False

#judge none
def is_none(str):
	if len(str) == 0:
		return True
	else:
		return False

# judge int
def is_int(target):
	if isinstance(target, int):
		return True
	elif isinstance(target, float):
		return False

#judge gas
def is_gas(str):
	if str.isdigit():
		return True
	else:
		return False

#judge balancd
def is_balance(str):
	if str.isdigit():
		return True
	else:
		return False

#judge hex
def is_hex(str,is_lens=None):
	if is_lens is None:
		if re.findall(r"^[A-F0-9]*$",str) and len(str) % 2 == 0:
			return True
		else:
			return False
	else:
		if re.findall(r"^[A-F0-9]{{{0}}}$".format(is_lens),str):
			return True
		else:
			return False
		
#judge signature		
def is_signature(str):
	if is_hex(str,128):
		return True
	else:
		return False

#judge str
def is_str(i):
	if re.findall("\d+(\.\d+)?",i):
		return True
	else:
		return False

#judge json
def try_load_json(jsonstr):
	try:
		json_data = json.loads(jsonstr)
		return True,json_data
	except ValueError as e:
		return False,None

class Test_rpc(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		Test_rpc.import_account = "czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9QP"
		Test_rpc.import_password = "1234qwer"
		Test_rpc.to_account = "czr_3TaSCeWHVRZnii8mvtnhDYQ1725MbN3jMjQ8ZkZa9H4jEcnxK6"
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"account": "czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u"
	}
	'''
	def test_account_import(self):
		data = {
			"action": "account_import",
			"json": "{\"account\":\"czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u\",\"kdf_salt\":\"774DDE2B6D01D6A2B000BB42F8118E2C\",\"iv\":\"5EF469016DB117B4437FB46D37BFA925\",\"ciphertext\":\"2B9567F4184B4D0A4AD9D5A3BF94805662B562167AFBEC575B06C23F708F0CA0\"}"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)

		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)

		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertEqual(json_data['msg'], 'OK', json_data['code'])
		json_account = json_data['account']
		self.assertTrue(is_account(json_account), json_account)

		data1 = {
			"action": "account_import",
			"json": "{\"account\":\"czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9QP\",\"kdf_salt\":\"15809FA0CF4A35DF563C52F52C2352E3\",\"iv\":\"EE39EECB963A43159AC71283685CE995\",\"ciphertext\":\"F529D75CE5AE2CC0D4B4353185F565FF3EA640B87532CEA73B00676415D582D7\"}"
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)

		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)

		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertEqual(json_data['msg'], 'OK', json_data['code'])
		json_account = json_data['account']
		self.assertTrue(is_account(json_account),json_account)

		data3 = {
			"action": "account_import",
			"json": "{\"account\":\"czr_3TaSCeWHVRZnii8mvtnhDYQ1725MbN3jMjQ8ZkZa9H4jEcnxK6\",\"kdf_salt\":\"B3092CC162E4119FF802FEDBDB36CCC9\",\"iv\":\"78B3327FC7EE6ADCB9AEDF13C8E11985\",\"ciphertext\":\"6A73BD25D457E71DC6710E234F0F51F00A68FACC60A28EE2FD0C0E0B288BB657\"}"
		}
		response = requests.post(url=URL, data=json.dumps(data3))
		self.assertEqual(response.status_code, 200)

		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)

		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertEqual(json_data['msg'], 'OK', json_data['code'])
		json_account = json_data['account']
		self.assertTrue(is_account(json_account), json_account)

		data2 = {
			"action": "account_import",
			"json": "{\"account\":\"czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh\",\"kdf_salt\":\"15809FA0CF4A35DF563C52F52C2352E3\",\"iv\":\"EE39EECB963A43159AC71283685CE995\",\"ciphertext\":\"F529D75CE5AE2CC0D4B4353185F565FF3EA640B87532CEA73B00676415D582D7\"}"
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)

		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)

		self.assertEqual(json_data['code'], 2, json_data['msg']) #Invalid json
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"account": "czr_4M943gNHekWpfTmRFJHUYTYV65gnkjN5zAjqTeRTbnNCXfeJrw"
	}
	'''
	def test_account_create(self):
		data = {
			"action": "account_create",
			"password": Test_rpc.import_password
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_account = json_data['account']
		self.assertTrue(is_account(json_account),json_account)

		data1 = {
			"action": "account_create",
			"password": ''
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Password can not be empty
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"hash": "CDE1EC247CAC41C321024DCEBF065662A46A49A119EF0641C0547111FBCB315D"
	}
	'''
	def test_send_block(self):
		data = {
			"action": "send_block",
			"from": 'czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u',
			"to": Test_rpc.import_account,
			"amount": "1000000000000000000",
			"password": '12345678',
			"gas": "21000",
			"gas_price": "1000000000000",
			"data": ""
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_hash = json_data['hash']
		self.assertTrue(is_hex(json_hash),json_hash)

		data4 = {
			"action": "block",
			"hash": json_hash
		}
		response = requests.post(url=URL, data=json.dumps(data4))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_datas = json_data['block']
		self.assertTrue(len(json_data['block']) > 0, json_data)
		self.assertTrue(is_hex(json_datas['hash']), json_datas)
		self.assertTrue(is_int(json_datas['type']), json_datas)
		self.assertTrue(is_signature(json_datas['signature']), json_datas)
		self.assertTrue(is_account(json_datas['from']), json_datas)
		json_data1 = json_datas['content']
		self.assertTrue(is_account(json_data1['to']), json_data1)
		self.assertTrue(is_gas(json_data1['amount']), json_data1)
		self.assertTrue(is_hex(json_data1['previous']), json_data1)
		self.assertTrue(is_int(json_data1['gas']), json_data1)
		self.assertTrue(is_gas(json_data1['gas_price']), json_data1)
		self.assertTrue(is_hex(json_data1['data_hash']), json_data1)
		self.assertTrue(is_int(json_data1['version']), json_data1)
		self.assertTrue(is_none(json_data1['data']), json_data1)

		data1 = {
			"action": "send_block",
			"from": Test_rpc.to_account,
			"to": Test_rpc.import_account,
			"amount": "1000000000000000000",
			"password": '1234qwer',
			"gas": "21000",
			"gas_price": "1000000000000",
			"data": ""
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 11, json_data['msg'])  # code 11 means insufficient balance

		data2 = {
			"action": "send_block",
			"from": Test_rpc.to_account,
			"to": Test_rpc.import_account,
			"amount": "1000000000000000000",
			"password": '1234',
			"gas": "21000",
			"gas_price": "1000000000000",
			"data": ""
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 10, json_data['msg']) #Wrong password

	'''
	{
	"code": 0,
	"msg": "OK",
	"balances": {
		"czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u": "1000000000000000000", //1CZR
		"czr_4m7NiSx2sBG4Hmdq1Yt6EGKqFQ3rmtBXCsmJZZp4E3pm84LkG9": "1000000000000000000"	 //1CZR
		}
	}
	'''
	def test_accounts_balances(self):
		data = {
			"action": "accounts_balances",
			"accounts": [
				Test_rpc.import_account,
				Test_rpc.to_account
			]
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_balances = json_data['balances']
		self.assertTrue(len(json_balances)>0,json_balances)
		for i in json_balances:
			self.assertTrue(is_balance(i),json_balances)
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"balance": "1000000000000000000"
	}
	'''
	def test_account_balance(self):
		data = {
			"action": "account_balance",
			"account": Test_rpc.import_account
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_balance = json_data['balance']
		self.assertTrue(is_balance(json_balance),json_balance)

		data = {
			"action": "accounts_balances",
			"accounts": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9'
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid account
	
	'''
	{
    "code": 0,
    "msg": "OK",
    "output": "692A70D2E424A56D2C6C27AA97D1A86395877B3A2C6C27AA97D1A86395877B5C"
	}
	'''
	def test_call(self):
		data = {
			"action": "call",
			"from": Test_rpc.import_account,
			"to": Test_rpc.to_account
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_output = json_data['output']
		self.assertTrue(is_hex(json_output),json_output)

		data1 = {
			"action": "call",
			"from": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9',
			"to": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9QP'
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid from account
	
	'''
	{
    "code": 0,
    "msg": "OK",
    "account_code": "61016B610030600B82828239805160001A6073146000811461002057610022565BFE5B5030600052607381538281F3FE7300000000000000000000000000000000000000003014608060405260043610610052576000357C010000000000000000000000000000000000000000000000000000000090048063DCE4A44714610057575B600080FD5B6100996004803603602081101561006D57600080FD5B81019080803573FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF169060200190929190505050610114565B6040518080602001828103825283818151815260200191508051906020019080838360005B838110156100D95780820151818401526020810190506100BE565B50505050905090810190601F1680156101065780820380516001836020036101000A031916815260200191505B509250505060405180910390F35B6060813B6040519150601F19601F602083010116820160405280825280600060208401853C5091905056FEA165627A7A7230582027C83370D70C11D17B94A12CCB8F7856B88ED68CFC6363465293981CB633B25C0029"
	}
	'''
	def test_account_code(self):
		data = {
			"action": "account_code",
			"account": Test_rpc.import_account
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_account_code = json_data['account_code']
		self.assertTrue(is_hex(json_account_code),json_account_code)

		data1 = {
			"action": "account_code",
			"account": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9'
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid account

	'''
	{
	"code": 0,
	"msg": "OK"
	}
	'''
	def test_account_lock(self):
	
		data = {
			"action": "account_lock",
			"account": Test_rpc.import_account
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data1 = {
			"action": "account_lock",
			"account": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9'
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid account
	
	'''
	{
	"code": 0,
	"msg": "OK"
	}
	'''
	def test_account_unlock(self):
		data = {
			"action": "account_unlock",
			"account": Test_rpc.import_account,
			"password": Test_rpc.import_password
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data1 = {
			"action": "account_unlock",
			"account": Test_rpc.import_account,
			"password": ''
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 3, json_data['msg']) #Wrong password

		data2 = {
			"action": "account_unlock",
			"account": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCAknXvh9',
			"password": Test_rpc.import_password
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid account
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"json": "{\"account\":\"czr_4GHUc91PYAddCiDHtwFnFDcsQrqdXW58Ps75rpHJsxAnJrQR1d\",\"kdf_salt\":\"37685A5B3413EC419CE4B5B79E0BB020\",\"iv\":\"F046EA90EA24A6CF0CB74BE8C560367B\",\"ciphertext\":\"4A2E6EE4CF04162D2A4DA6116C23CD94487837731055A1BC0FCBDA7E0D7C65A4\"}"
	}
	'''
	def test_account_export(self):
		data = {
			"action": "account_export",
			"account": Test_rpc.import_account
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		data_json = json_data['json']
		
		try:
			json_object = json.loads(data_json)
		except ValueError as e:
			self.assertTrue(False,e,data_json)
		
		json_account = json_object['account']
		self.assertTrue(is_account(json_account),json_account)
		
		json_kdf_salt = json_object['kdf_salt']
		self.assertTrue(is_hex(json_kdf_salt,32),json_kdf_salt)
		
		json_iv = json_object['iv']
		self.assertTrue(is_hex(json_iv,32),json_iv)
		
		json_ciphertext = json_object['ciphertext']
		self.assertTrue(is_hex(json_ciphertext,64),json_ciphertext)

		data1 = {
			"action": "account_export",
			"account": ''
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 2, json_data['msg']) #Account not found
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"valid": 1
	}
	'''
	def test_account_validate(self):
		data = {
			"action": "account_validate",
			"account": Test_rpc.import_account
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertEqual(json_data['valid'], 1)

		data1 = {
			"action": "account_validate",
			"account": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANs'
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertEqual(json_data['valid'], 0) #账号不合�?
	
	'''
	{
	"code": 0,
	"msg": "OK"
	}  
	'''
	def test_account_password_change(self):
		new_password = "1234qwer"
		data = {
			"action": "account_password_change",
			"account": Test_rpc.import_account,
			"old_password": Test_rpc.import_password,
			"new_password": new_password
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		
		#change password to old one 
		data1 = {
			"action": "account_password_change",
			"account": Test_rpc.import_account,
			"old_password": new_password,
			"new_password": Test_rpc.import_password
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data2 = {
			"action": "account_password_change",
			"account": Test_rpc.import_account,
			"old_password": '',
			"new_password": Test_rpc.import_password
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 5, json_data['msg']) # Wrong old password

	def test_account_list(self):
		data = {
			"action": "account_list"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertTrue(len(json_data['accounts']) > 0, json_data)
		for i in json_data['accounts']:
			self.assertTrue(is_account(i),json_data['accounts'])

	def test_account_block_list(self):
		data = {
			"action": "account_block_list",
			"account": Test_rpc.import_account,
			"limit": 100
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_datas = json_data['blocks']
		for i in json_datas:
			self.assertTrue(is_hex(i['hash']), json_datas)
			self.assertTrue(is_int(i['type']), json_datas)
			self.assertTrue(is_signature(i['signature']), json_datas)
			self.assertTrue(is_account(i['from']), json_datas)
			json_data1 = i['content']
			self.assertTrue(is_account(json_data1['to']) ,json_data1)
			self.assertTrue(is_gas(json_data1['amount']), json_data1)
			self.assertTrue(is_hex(json_data1['previous']), json_data1)
			self.assertTrue(is_int(json_data1['gas']), json_data1)
			self.assertTrue(is_gas(json_data1['gas_price']), json_data1)
			self.assertTrue(is_hex(json_data1['data_hash']), json_data1)
			self.assertTrue(is_int(json_data1['version']), json_data1)
			self.assertTrue(is_none(json_data1['data']), json_data1)


		data1 = {
			"action": "account_block_list",
			"account": 'czr_4HTGGzsHKaDXpngAW5T1d1D98S5ysVEsfxaUZANsCA',
			"limit": 100
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid account
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"gas": "21000"
	}
	'''
	def test_estimate_gas(self):
		data = {
			"action": "estimate_gas",
			"from": Test_rpc.import_account,
			"to": Test_rpc.to_account,
			"amount": "1000000000000000000",
			"gas": "21000",
			"gas_price": "1000000000000"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_gas = json_data['gas']
		self.assertTrue(is_gas(json_gas),json_gas)

		data1 = {
			"action": "estimate_gas",
			"from": Test_rpc.import_account,
			"to": Test_rpc.to_account,
			"amount": "1000000000000000000",
			"gas": "2",
			"gas_price": "1000000000000"
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 9, json_data['msg']) #Gas not enough or execute fail

		data2 = {
			"action": "estimate_gas",
			"from": Test_rpc.import_account,
			"to": Test_rpc.to_account,
			"amount": "1000000000000000000",
			"gas": "21000",
			"gas_price": ""
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 7, json_data['msg']) #Invalid gas price format

	def test_generate_offline_block(self):
		data = {
			"action": "generate_offline_block",
			"from": "czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u",
			"to": Test_rpc.import_account,
			"amount": "1000000000000000000",
			"gas": "21000",
			"gas_price": "1000000000",
			"data": ""
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertTrue(is_hex(json_data['hash']), json_data)
		self.assertTrue(is_account(json_data['from']), json_data)
		self.assertTrue(is_account(json_data['to']), json_data)
		self.assertTrue(is_gas(json_data['amount']), json_data)
		self.assertTrue(is_hex(json_data['previous']), json_data)
		self.assertTrue(is_gas(json_data['gas']), json_data)
		self.assertTrue(is_gas(json_data['gas_price']), json_data)
		self.assertTrue(is_none(json_data['data']), json_data)

		data1 = {
			"action": "generate_offline_block",
			"from": "czr_3TaSCeWHVRZnii8mvtnhDYQ1725MbN3jMjQ8ZkZa9H4jEcnxK6",
			"to": Test_rpc.import_account,
			"amount": "1000000000000000000",
			"gas": "21000",
			"gas_price": "1000000000",
			"data": ""
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 8, json_data['msg']) #Insufficient balance

	def test_send_offline_block(self):
		data = {
			"action": "send_offline_block",
			"previous": "0000000000000000000000000000000000000000000000000000000000000000",
			"from": "czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u",
			"to": "czr_3w6RT4KJ5CGocZRUqwuxUfUciLggCTAgpccLrMwxqgJuSB2iW6",
			"amount": "1000000000000000000",
			"gas": "21000",
			"gas_price": "1000000000",
			"data": "",
			"signature": "71408627FF461C9DE076A38B71953A3045C95D1E1E841A2224E4AC3E503C0D0046FE8FEEB6E72B257B7743F53AFEC1CE80699D5E125C60794D6D09823C3B1E0C"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		self.assertTrue(is_hex(json_data['hash']), json_data)

		data1 = {
			"action": "send_offline_block",
			"previous": "0000000000000000000000000000000000000000000000000000000000000000",
			"from": "czr_3TaSCeWHVRZnii8mvtnhDYQ1725MbN3jMjQ8ZkZa9H4jEcnxK6",
			"to": "czr_3w6RT4KJ5CGocZRUqwuxUfUciLggCTAgpccLrMwxqgJuSB2iW6",
			"amount": "1000000000000000000",
			"gas": "21000",
			"gas_price": "1000000000",
			"data": "",
			"signature": "71408627FF461C9DE076A38B71953A3045C95D1E1E841A2224E4AC3E503C0D0046FE8FEEB6E72B257B7743F53AFEC1CE80699D5E125C60794D6D09823C3B1E0C"
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 14, json_data['msg']) # Invalid signature

		data2 = {
			"action": "send_offline_block",
			"previous": "0000000000000000000000000000000000000000000000000000000000000000",
			"from": "czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u",
			"to": "",
			"amount": "1000000000000000000",
			"gas": "21000",
			"gas_price": "1000000000",
			"data": "",
			"signature": "71408627FF461C9DE076A38B71953A3045C95D1E1E841A2224E4AC3E503C0D0046FE8FEEB6E72B257B7743F53AFEC1CE80699D5E125C60794D6D09823C3B1E0C"
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 14, json_data['msg']) # Invalid block
	
	'''
	{
	"code": 0,
	"msg": "OK",
	"signature": "E09CDD795E6959C3B85FDCA0EA56BCFBBC7BE05A0D0AB6B1A0C6DD23FF0AA36F635C70CB731DAC07909A572132128120EBC12862D4BEC2FE70E9A6060F32CA0C"
	}
	'''
	def test_sign_msg(self):
		data = {
			"action": "sign_msg",
			"public_key": Test_rpc.import_account,
			"password": Test_rpc.import_password,
			"msg": "CB09A146D83668AE13E951032D2FD94F893C9A0CA0822ED40BBE11DC0F167D1B"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_sign = json_data['signature']
		self.assertTrue(is_signature(json_sign),json_sign)

		data1 = {
			"action": "sign_msg",
			"public_key": Test_rpc.import_account,
			"password": 'czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u',
			"msg": "CB09A146D83668AE13E951032D2FD94F893C9A0CA0822ED40BBE11DC0F167D1B"
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 3, json_data['msg']) #Wrong password

		data2 = {
			"action": "sign_msg",
			"public_key": 'czr_33EuccjKjcZgwbHYp8eLhoFiaKGARVigZojeHzySD9fQ1ysd7u',
			"password": '12345678',
			"msg": ""
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 2, json_data['msg']) #Invalid msg format

	def test_block(self):
		data = {
			"action": "block",
			"hash": "412254AB895FD2E6ADE6F9076CA8297516F2845C989A13AC008CD5D70157AFFB"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data1 = {
			"action": "block",
			"hash": ""
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid hash format
		
	def test_blocks(self):
		data = {
			"action": "blocks",
			"hashes": [
				"412254AB895FD2E6ADE6F9076CA8297516F2845C989A13AC008CD5D70157AFFB",
				"B222C88AB9729B4DEF3F5E12962DB12A2FA80C9B50A4003CD67CE024428DAC61"
			]
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data = {
			"action": "blocks",
			"hashes": ''
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid hash format

	def test_block_state(self):
		data = {
			"action": "block_state",
			"hash": "412254AB895FD2E6ADE6F9076CA8297516F2845C989A13AC008CD5D70157AFFB"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data1 = {
			"action": "block_state",
			"hash": ""
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) #Invalid hash format

	def test_block_states(self):
		data = {
			"action": "block_states",
			"hashes": [
				"412254AB895FD2E6ADE6F9076CA8297516F2845C989A13AC008CD5D70157AFFB",
				"B222C88AB9729B4DEF3F5E12962DB12A2FA80C9B50A4003CD67CE024428DAC61"
			]
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data1 = {
			"action": "block_states",
			"hashes": ''
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) # Invalid hash format

	def test_block_traces(self):
		data = {
			"action": "block_traces",
			"hash": "412254AB895FD2E6ADE6F9076CA8297516F2845C989A13AC008CD5D70157AFFB"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data1 = {
			"action": "block_traces",
			"hash": ""
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg'])# Invalid hash format

	def test_stable_blocks(self):
		data = {
			"action": "stable_blocks",
			"limit": 100,
			"index": 15577
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])

		data1 = {
			"action": "stable_blocks",
			"limit": '',
			"index": ''
		}
		response = requests.post(url=URL, data=json.dumps(data1))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 1, json_data['msg']) # Invalid index format

		data2 = {
			"action": "stable_blocks",
			"limit": '',
			"index": 15577
		}
		response = requests.post(url=URL, data=json.dumps(data2))
		self.assertEqual(response.status_code, 200)
		is_json, json_data = try_load_json(response.text)
		self.assertTrue(is_json, response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 2, json_data['msg']) # Invalid limit format


	def test_status(self):
		data = {
			"action": "status"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
	
	'''
	{
    "code": 0,
    "msg": "OK",
    "witness_list": [
        "czr_321JDA7Brgbnm64iY2Xh8yHMEqEgBDutnoTKVLcxW2DJvJLUsS",
        "czr_32RmC9FsxjgLkgRQ58j3CdLg79cQE3KaY2wAT1QthBTU25vpd3",
        "czr_3MnXfV9hbmxVPdgfrPqgUiH6N7VbkSEhn5VqBCzBcxzTzkEUxU",
        "czr_3SrfL6LnPbtyf6sanrgtKs1BTYDN8taacGBVG37LfZVqXvRHbf",
        "czr_3igvJpdDiV4v5HxEzCifFcUpKvWsk3qWYNrTrbEVQztKbpyW1z",
        "czr_3tiy2jgoUENkszPjrHjQGfmopqwV5m9BcEh2Grb1zDYgSGnBF7",
        "czr_47E2jJ9rXVk5GRBcTLQMLQHXqsrnVcV5Kv2CWQJ6dnUaugnvii",
        "czr_49BvoaSgGnyfPdaHfrSdac74fcxV4cUdysskHSQPQ8XisShN3P",
        "czr_4HhYojuHanxQ57thkSxwy5necRtDFwiQP7zqngBDZHMjqdPiMS",
        "czr_4MYTD6Xctkb6fEL8xUZxUwY6eqYB7ReEfB61YFrMHaZxsqLCKd",
        "czr_4URkteqck9rM8Vo6VzWmvKtMWoSH8vo4A1rADNAFrQHxAR23Tb",
        "czr_4ZJ8hBdR6dLv4hb1RPCmajdZf7ozkH1sHU18kT7xnXj4mjxxKE",
        "czr_4aBXjWXyN7WVGqMKH7FgnSoN9oePeEPiZsrtc2AMYyuTRJoNpb",
        "czr_4iig3fTcXQmz7bT2ztJPrpH8usrqGTN5zmygFqsCJQ4HgiuNvP"
    ]
	}
	'''
	def test_witness_list(self):
		data = {
			"action": "witness_list"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		json_witness_list = json_data['witness_list']
		self.assertTrue(len(json_witness_list)>0,json_witness_list)
		for i in json_data['witness_list']:
			self.assertTrue(is_account(i),json_witness_list)
		
	
	'''
	{
	"code": 0,
	"msg": "OK"
	}
	'''
	def test_account_remove(self):
		data = {
			"action": "account_remove",
			"account": Test_rpc.import_account,
			"password": Test_rpc.import_password
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
	
	'''
	{
    "code": 0,
    "msg": "OK",
    "version": "0.9.7",
    "rpc_version": "1",
    "store_version": "4"
	}
	'''
	def test_version(self):
		data = {
			"action": "version"
		}
		response = requests.post(url=URL, data=json.dumps(data))
		self.assertEqual(response.status_code, 200)
		is_json,json_data = try_load_json(response.text)
		self.assertTrue(is_json,response.text)
		json_data = json.loads(response.text)
		self.assertEqual(json_data['code'], 0, json_data['msg'])
		
		json_version = json_data['version']
		self.assertTrue(is_str(json_version),json_version)
		
		json_rpc_version = json_data['rpc_version']
		self.assertTrue(is_str(json_rpc_version),json_rpc_version)
		
		json_store_version = json_data['store_version']
		self.assertTrue(is_str(json_store_version),json_store_version)

if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(Test_rpc("test_account_import"))
	suite.addTest(Test_rpc("test_account_create"))
	suite.addTest(Test_rpc("test_send_block"))
	suite.addTest(Test_rpc("test_accounts_balances"))
	suite.addTest(Test_rpc("test_account_balance"))
	suite.addTest(Test_rpc("test_call"))
	suite.addTest(Test_rpc("test_account_code"))
	suite.addTest(Test_rpc("test_account_lock"))
	suite.addTest(Test_rpc("test_account_unlock"))
	suite.addTest(Test_rpc("test_account_export"))
	suite.addTest(Test_rpc("test_account_validate"))
	suite.addTest(Test_rpc("test_account_password_change"))
	suite.addTest(Test_rpc("test_account_list"))
	suite.addTest(Test_rpc("test_account_block_list"))
	suite.addTest(Test_rpc("test_estimate_gas"))
	suite.addTest(Test_rpc("test_generate_offline_block"))
	suite.addTest(Test_rpc("test_send_offline_block"))
	suite.addTest(Test_rpc("test_sign_msg"))
	suite.addTest(Test_rpc("test_block"))
	suite.addTest(Test_rpc("test_blocks"))
	suite.addTest(Test_rpc("test_block_state"))
	suite.addTest(Test_rpc("test_block_states"))
	suite.addTest(Test_rpc("test_block_traces"))
	suite.addTest(Test_rpc("test_stable_blocks"))
	suite.addTest(Test_rpc("test_status"))
	suite.addTest(Test_rpc("test_witness_list"))
	suite.addTest(Test_rpc("test_version"))
	suite.addTest(Test_rpc("test_account_remove"))
	result = unittest.TextTestRunner(verbosity=3).run(suite)
	if result.wasSuccessful():
		exit(0)
	else:
		exit(1)

