{
  "metadata": {
    "schemaVersion": "1.0",
    "importType": "LEX",
    "importFormat": "JSON"
  },
  "resource": {
    "name": "RoboAdvisor",
    "version": "1",
    "intents": [
      {
        "name": "RecommendPortfolio",
        "version": "3",
        "fulfillmentActivity": {
          "codeHook": {
            "uri": "arn:aws:lambda:us-east-1:293276706374:function:recommendportfolio",
            "messageVersion": "1.0"
          },
          "type": "CodeHook"
        },
        "sampleUtterances": [
          "I want to save money for my retirement",
          "I'm {age} and I would like to invest for my retirement",
          "I'm {age} and i want to invest for my retirement",
          "I want the best option to invest for my retirement",
          "I worried about my retirement",
          "I want to invest for my retirement"
        ],
        "slots": [
          {
            "sampleUtterances": [],
            "slotType": "AMAZON.NUMBER",
            "obfuscationSetting": "NONE",
            "slotConstraint": "Required",
            "valueElicitationPrompt": {
              "messages": [
                {
                  "contentType": "PlainText",
                  "content": "How old are you?"
                }
              ],
              "maxAttempts": 2
            },
            "priority": 2,
            "name": "age"
          },
          {
            "sampleUtterances": [],
            "slotType": "AMAZON.US_FIRST_NAME",
            "obfuscationSetting": "NONE",
            "slotConstraint": "Required",
            "valueElicitationPrompt": {
              "messages": [
                {
                  "contentType": "PlainText",
                  "content": "Thank you for trusting me to help, could you please give me your name"
                }
              ],
              "maxAttempts": 2
            },
            "priority": 1,
            "name": "firstname"
          },
          {
            "sampleUtterances": [],
            "slotType": "AMAZON.NUMBER",
            "obfuscationSetting": "NONE",
            "slotConstraint": "Required",
            "valueElicitationPrompt": {
              "messages": [
                {
                  "contentType": "PlainText",
                  "content": "How much do you want to invest?"
                }
              ],
              "maxAttempts": 2
            },
            "priority": 3,
            "name": "investmentamount"
          },
          {
            "sampleUtterances": [],
            "slotType": "risklevel",
            "slotTypeVersion": "1",
            "obfuscationSetting": "NONE",
            "slotConstraint": "Required",
            "valueElicitationPrompt": {
              "messages": [
                {
                  "contentType": "PlainText",
                  "content": "e.g. What city?"
                },
                {
                  "contentType": "PlainText",
                  "content": "What level of investment risk would you like to take?"
                }
              ],
              "responseCard": "{\"version\":1,\"contentType\":\"application/vnd.amazonaws.card.generic\",\"genericAttachments\":[{\"imageUrl\":\"https://umn.bootcampcontent.com/University-of-Minnesota-Boot-Camp/uofm-virt-fin-pt-12-2021-u-c/-/raw/master/02-Homework/13-AWS-Lex/Instructions/Icons/low.png\",\"subTitle\":\"No risk at all\",\"title\":\"None\",\"buttons\":[{\"text\":\"none\",\"value\":\"Low\"},{\"text\":\"none\",\"value\":\"Low\"}]},{\"imageUrl\":\"https://umn.bootcampcontent.com/University-of-Minnesota-Boot-Camp/uofm-virt-fin-pt-12-2021-u-c/-/raw/master/02-Homework/13-AWS-Lex/Instructions/Icons/medium.png\",\"subTitle\":\"Just a bit of risk\",\"title\":\"Very Low or Low\",\"buttons\":[{\"text\":\"Very Low\",\"value\":\"Low\"},{\"text\":\"Very Low\",\"value\":\"Low\"}]},{\"imageUrl\":\"https://umn.bootcampcontent.com/University-of-Minnesota-Boot-Camp/uofm-virt-fin-pt-12-2021-u-c/-/raw/master/02-Homework/13-AWS-Lex/Instructions/Icons/medium.png\",\"subTitle\":\"Let's start becoming wild\",\"title\":\"Medium\",\"buttons\":[{\"text\":\"Medium\",\"value\":\"Low\"},{\"text\":\"Medium\",\"value\":\"Low\"}]},{\"imageUrl\":\"https://umn.bootcampcontent.com/University-of-Minnesota-Boot-Camp/uofm-virt-fin-pt-12-2021-u-c/-/raw/master/02-Homework/13-AWS-Lex/Instructions/Icons/none.png\",\"subTitle\":\"I have no fear!\",\"title\":\"High or very High\",\"buttons\":[{\"text\":\"High\",\"value\":\"High\"},{\"text\":\"High\",\"value\":\"High\"}]}]}",
              "maxAttempts": 2
            },
            "priority": 4,
            "defaultValueSpec": {
              "defaultValueList": []
            },
            "name": "slotFour"
          }
        ],
        "conclusionStatement": {
          "messages": [
            {
              "groupNumber": 1,
              "contentType": "PlainText",
              "content": "I will be pleased to assist you in the future."
            },
            {
              "groupNumber": 1,
              "contentType": "PlainText",
              "content": "Would you like me to search for the best investment portfolio for you now?"
            }
          ]
        }
      }
    ],
    "slotTypes": [
      {
        "description": "risk level",
        "name": "risklevel",
        "version": "1",
        "enumerationValues": [
          {
            "value": "High",
            "synonyms": [
              "Maximum"
            ]
          },
          {
            "value": "Low",
            "synonyms": [
              "Minimal"
            ]
          }
        ],
        "valueSelectionStrategy": "TOP_RESOLUTION"
      }
    ],
    "voiceId": "Salli",
    "childDirected": false,
    "locale": "en-US",
    "idleSessionTTLInSeconds": 300,
    "clarificationPrompt": {
      "messages": [
        {
          "contentType": "PlainText",
          "content": "Sorry, can you please repeat that?"
        }
      ],
      "maxAttempts": 5
    },
    "abortStatement": {
      "messages": [
        {
          "contentType": "PlainText",
          "content": "Sorry, I could not understand. Goodbye."
        }
      ]
    },
    "detectSentiment": false,
    "enableModelImprovements": false
  }
}