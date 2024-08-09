from dao.questions import get_question_by_id
from flask import request
from flask_restful import Resource
from dao.user import validate_user
import os
import subprocess


class Solution(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        code = request_data["code"]
        language = request_data["language"]
        question_id = request_data["question_id"]
        extention = ""
        if language=="python":
            extention = ".py"
        elif language=="c":
            extention =".c"
        elif language=="cpp":
            extention =".cpp"
        f = open("program"+extention, "w")
        f.write(code)
        f.close()

        print(code)
        question = get_question_by_id(question_id)
        testcases = question["test_cases"]
        
        counter = 0
        passed_testcases = 0
        try:
            if language=="python":
                
                for testcase in testcases:
                    counter=counter+1
                    proc = subprocess.Popen(['python3 program.py "'+str(testcase["input"])+'"'], stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()
                    if err!=None:
                        return "Error:\n"+err
                    output = out.decode("utf-8") 
                    answer = output.replace('\n','')
                    print(answer,str(testcase["output"]))
                    if answer == str(testcase["output"]):
                        passed_testcases = passed_testcases+1

            elif language=="c":
                proc = subprocess.Popen(['gcc program.c'], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                if err!=None:
                    return "Error:\n"+err
                for testcase in testcases:
                    counter=counter+1
                    procs= subprocess.Popen(['./a.out '+str(testcase["input"])], stdout=subprocess.PIPE, shell=True)
                    (out, err) = procs.communicate()
                    output = out.decode("utf-8") 
                    answer = output.replace('\n','')
                    print("Output: ",str(testcase["output"]),"answer: ", type(answer))
                    if answer == str(testcase["output"]):
                        passed_testcases = passed_testcases+1
            elif language=="cpp":
                for testcase in testcases:
                    counter=counter+1
                    proc = subprocess.Popen(['g++ program.cpp'], stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()
                    if err!=None:
                        return "Error:\n"+err
                    proc = subprocess.Popen(['./a.out "'+str(testcase["input"])+'"'], stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()

                    output = out.decode("utf-8") 
                    answer = output.replace('\n','')
                    print(output,answer)
                    if answer == str(testcase["output"]):
                        passed_testcases = passed_testcases+1
            return "Total "+str(passed_testcases)+"/"+str(counter)+" testcases passed"
        except:
            return "Exception"