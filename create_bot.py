import boto3

lex_models = boto3.client('lex-models')

bot_name = 'Doctor_Appointment_Bot'
bot_description = "Bot used to schedule doctor appointment"
bot_intents = [
			{
			"intentName" : "DoctorAppointment",
			"intentVersion" : "$LATEST"
			},
			{
			"intentName" : "DoctorList",
			"intentVersion" : "$LATEST"
			}
		]
bot_clarificationPrompt = {
		"messages": [
		{
		"contentType": "PlainText",
		"content": "I didn't understand you, What would you like to do?"
		}
		],
		"maxAttempts": 3,
		"responseCard": "I didn't understand you, What would you like to do?"
	}

bot_abortStatement = {
		"messages": [
		{
		"contentType": "PlainText",
		"content": "Sorry, I'm not able to assist at this time"
		}
		],
		"responseCard": "Sorry, I'm not able to assist at this time"
}

bot_voiceId= "Salli"
bot_childDirected= False
bot_idleSessionTTLInSeconds= 600
locale='en-US'
processBehavior='BUILD'
createVersion=False

bot = lex_models.put_bot(name=bot_name,\
						description=bot_description,\
						intents=bot_intents,\
						clarificationPrompt=bot_clarificationPrompt,\
						abortStatement=bot_abortStatement,\
						voiceId=bot_voiceId,\
						childDirected=bot_childDirected,\
						idleSessionTTLInSeconds=bot_idleSessionTTLInSeconds,\
						locale=locale,\
						processBehavior=processBehavior)