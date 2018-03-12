import boto3
import json
import ast

lex_models = boto3.client('lex-models')
slots = json.load(open('DoctorAppointment.json'))

name='DoctorAppointment'
description='Intent to book an appointment to meet a doctor'
sampleUtterances = [
        "I would like to book an appointment",
        "Book an appointment",
        "Can you book an appointment"
    ]
confirmationPrompt = {
        "maxAttempts": 2,
        "messages": [
            {
                "content": "Shall I confirm your {appointment} appointment on {Date} at {Time} ?",
                "contentType": "PlainText"
            }
        ],
        "responseCard": "Shall I confirm your {appointment} appointment on {Date} at {Time} ?"
    }
rejectionStatement = {
        "messages": [
            {
                "content": "Okay, appointment is not schedueled.",
                "contentType": "PlainText"
            }
        ]
    }
followUpPrompt = {
        "prompt": {
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Do you want to see the list of registered doctors with AMZN Inc.?"
                }
            ],
            "maxAttempts": 2,
            "responseCard": "Dr.Abc Vision\nDr.Def Dental\nDr.Ghi General"
        },
        "rejectionStatement": {
        	"messages": [
        	{
        		"contentType": "PlainText",
        		"content": "Okay."
        	}
        	],
        	"responseCard": "Okay."
        }
    }
conclusionStatement = {
		"messages": [
		{
			"contentType": "PlainText",
			"content": "Your appoinment is scheduled on {Date} at {Time}"
		}
		],
		"responseCard": "Your appoinment is scheduled on {Date} at {Time}"
	}
fulfillmentActivity = {
	"type": "ReturnIntent"
}

slotType = lex_models.put_intent\
			(name=name\
				,description=description,\
				sampleUtterances=sampleUtterances,\
				#confirmationPrompt=confirmationPrompt,\
				rejectionStatement=rejectionStatement,\
				#followUpPrompt=followUpPrompt,\
				conclusionStatement=conclusionStatement,\
				fulfillmentActivity=fulfillmentActivity,\
				slots=slots)

#print()