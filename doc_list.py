import boto3

lex_models = boto3.client('lex-models')

name='DoctorList'
description='Intent to book an appointment to meet a doctor'
sampleUtterances = [
        "Show me the list of doctors registered with AMZN Inc.",
        "doctors list",
    ]
conclusionStatement = {
        "messages": [
        {
            "contentType": "PlainText",
            "content": "Below is the list of doctors that are registered with AMZN Inc. \n Dr Abc, Vision\n Dr Def, Dental\n Dr Ghi, General"
        }
        ],
        "responseCard": "Below is the list of doctors that are registered with AMZN Inc. \n Dr Abc, Vision\n Dr Def, Dental\n Dr Ghi, General"
    }
fulfillmentActivity = {
    "type": "ReturnIntent"
}

slotType = lex_models.put_intent\
            (name=name\
                ,description=description,\
                sampleUtterances=sampleUtterances,\
                conclusionStatement=conclusionStatement,\
                fulfillmentActivity=fulfillmentActivity)

