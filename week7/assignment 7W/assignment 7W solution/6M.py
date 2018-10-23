from random import randint

# This code is exceptionally ugly, IMO
# I intended to clean it up, but I might not get to it before this solution is posted
# note to self for cleanup: use variables in a dictionary, not separate variables
# merge attributes and slots into dictionary
# if any are missing, ask about them

def handler(event, context):
    
    myApplicationId = "amzn1.ask.skill.84d829f9-db8e-452a-a1c5-e0472eef62ca"
    if event["session"]["application"]["applicationId"] != myApplicationId:
        return "403 Forbidden"
        
    outputSpeech = {"type": "PlainText", "text": "Hello World!"} # default
    sA = {}    
    r = {"outputSpeech":outputSpeech, "shouldEndSession":True}     

    if event["request"]["type"] == "IntentRequest": # check the type first
        if event["request"]["intent"]["name"] == "AMAZON.HelpIntent":
            outputSpeech["text"] = "This is all the help you get."
            
        elif event["request"]["intent"]["name"] == "RandomNumberIntent":
            try:
                low = int(event["request"]["intent"]["slots"]["low"]["value"])
            except:
                low = 0
            try:
                high = int(event["request"]["intent"]["slots"]["high"]["value"])
            except:
                high = 10
            outputSpeech["text"] = str(randint(low,high))
            
        elif event["request"]["intent"]["name"] == "AnswerIntent":
            
            # load available session attributes into variables
            a,b,op = None, None, None
            if 'op' in event["session"]["attributes"]:
                op = event["session"]["attributes"]["op"]
            if 'a' in event["session"]["attributes"]:
                a = event["session"]["attributes"]["a"]
            if 'b' in event["session"]["attributes"]:
                b = event["session"]["attributes"]["b"]

            # based on session attributes, determine which question was answered
            try:
                if op is None:
                    if event["request"]["intent"]["slots"]["op"]["value"] in ["add","multiply"]:
                        op = event["request"]["intent"]["slots"]["op"]["value"]
                elif a is None:
                    a = int(event["request"]["intent"]["slots"]["num"]["value"])
                else:
                    b = int(event["request"]["intent"]["slots"]["num"]["value"])
            except:
                pass
                
            sA = {'a':a, 'b':b, 'op':op}
            
            # based on what is missing, prompt
            if op is None:
                outputSpeech["text"] = "Sorry, I didn't catch that. Please repeat the operation."
                r['shouldEndSession'] = False
            elif a is None:
                outputSpeech["text"] = "Sorry, I didn't catch the first number. Please repeat it."
                r['shouldEndSession'] = False
            elif b is None:
                outputSpeech["text"] = "I didn't catch the second number. Please repeat it."
                r['shouldEndSession'] = False
            else: # if nothing is missing, answer the question
                try:
                    add = lambda a,b: a+b
                    multiply = lambda a,b: a*b
                    ops = {"add": add, "multiply":multiply}
                    outputSpeech["text"] = ops[op](a,b)
                except: # not sure if this can be reached
                    outputSpeech["text"] = "Oh, I'm not very good at math. Goodbye."

        elif event["request"]["intent"]["name"] == "DoArithmeticIntent":
            
            # get slots if they were understood, otherwise prompt
            try: 
                b = int(event["request"]["intent"]["slots"]["b"]["value"])
            except:
                outputSpeech["text"] = "I didn't catch the second number. Please repeat it."
                r['shouldEndSession'] = False
                b = None
                
            try:
                a = int(event["request"]["intent"]["slots"]["a"]["value"])
            except:
                outputSpeech["text"] = "I didn't catch the first number. Please repeat it."
                r['shouldEndSession'] = False
                a = None
                
            try:
                op = event["request"]["intent"]["slots"]["op"]["value"]
                add = lambda a,b: a+b
                multiply = lambda a,b: a*b
                ops = {"add": add, "multiply":multiply}
                op_fun = ops[op] # this is dumb. but I wanted it to raise an error
            except:
                outputSpeech["text"] = "I didn't catch the operation to perform. Please repeat it."
                r['shouldEndSession'] = False
                op = None
                
            sA = {'a':a, 'b':b, 'op':op}
                
            try: # here goes nothin'
                outputSpeech["text"] = ops[op](a,b)
            except:
                pass
    
    response = {"version":"1.0", "response":r, "sessionAttributes":sA}
    return response