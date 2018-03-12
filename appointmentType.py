import boto3
import json

lex_models = boto3.client('lex-models')
abc = json.load(open('appointmentType_slotType.json'))

try:
	slotType = lex_models.put_slot_type\
	(name='appointmentType',\
		description='Consists of different types of appointments that a client can make',\
		enumerationValues=abc['enumerationValues'],createVersion=True)
except:
	print('SlotType already created')


