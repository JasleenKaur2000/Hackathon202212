from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
import pickle

def index(response):
  return render(response,"index.html")

def case(i):
      switcher={
              0:'Database Developer',
              1:'Portal Administrator',
              2:'Systems Security Administrator',
              3:'Business Systems Analyst',
              4:'Software Systems Engineer',
              5:'Business Intelligence Analyst',
              6:'CRM Technical Developer',
              7:'Mobile Applications Developer',
              8:'UX Designer',
              9:'Quality Assurance Associate',
              10:'Web Developer',
              11:'Information Security Analyst',
              12:'CRM Business Analyst',
              13:'Technical Support',
              14:'Project Manager',
              15:'Information Technology Manager',
              16:'Programmer Analyst',
              17:'Design & UX',
              18:'Solutions Architect',
              19:'Systems Analyst',
              20:'Network Security Administrator',
              21:'Data Architect',
              22:'Software Developer',
              23:'E-Commerce Analyst',
              24:'Technical Services/Help Desk/Tech Support',
              25:'Information Technology Auditor',
              26:'Database Manager',
              27:'Applications Developer',
              28:'Database Administrator',
              29:'Network Engineer',
              30:'Software Engineer',
              31:'Technical Engineer',
              32:'Network Security Engineer',
              33:'Software Quality Assurance (QA) / Testing'
          }
      return switcher.get(i, "invalid prediction")

def home(response):
    # os = int(response.POST['os'])
    a=[response.POST['os'],response.POST['al'],response.POST['pc'], response.POST['sw'], response.POST['cn'], response.POST['ec'], response.POST['coa'], response.POST['mt'], response.POST['cs'], response.POST['hr'], response.POST['lq'], response.POST['hack'], response.POST['csr'], response.POST['psp'], response.POST['cw'], response.POST['cl'], response.POST['ex']]
    model = pickle.load(open(r"C:\Users\Amitesh\Desktop\final\Hackathon202212\ml\ml\predictionsmodel.sav", "rb"))
    # a = [55,59,24,89,61,55,32,51,96,7,6,2,5,7,1,0,0]
    predictedJob = model.predict([a])
    import math
    y = predictedJob[0]
    x = predictedJob[0]
    z = math.floor(((y-int(x))*100)%34)
    n = case(z)
    
    
    
    #def getPredictions():
        #a = [os, al, pc, sw, cn, ec, coa, mt, cs, hr, lq, hack, csr, psp, cw, cl, ex ]
    
    return render(response, "result.html", {'n':n})
    #HttpResponse(n)
  #  return pred[z]

       

# our result page view
# def result(request):
#     os = int(request.GET['os'])
#     al = int(request.GET['al'])
#     pc = int(request.GET['pc'])
#     sw = int(request.GET['sw'])
#     cn = int(request.GET['cn'])
#     ec = int(request.GET['ec'])
#     coa = int(request.GET['coa'])
#     mt = int(request.GET['mt'])
#     cs = int(request.GET['cs'])
#     hr = int(request.GET['hr'])
#     lq = int(request.GET['lq'])
#     hack = int(request.GET['hack'])
#     csr = int(request.GET['csr'])
#     psp = int(request.GET['psp'])
#     cw = int(request.GET['cw'])
#     cl = int(request.GET['cl'])
#     ex = int(request.GET['ex'])

#     #result = getPredictions(os, al, pc, sw, cn, ec, coa, mt, cs, hr, lq, hack, csr, psp, cw, cl, ex )

#     #return render(request, 'result.html', {'result':result})
#     return render("Hello World",'result.html')
    

# def myfunc():
#     a = "Hello"
#     return a


    # data ="<b>Hi There!! </b>"+str(a) 
    
    # return render(response,'index.html',context={"name":"ss"});