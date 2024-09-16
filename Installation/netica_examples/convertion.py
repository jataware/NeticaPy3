from Modules.NeticaPy3.NeticaPy import Netica
N=Netica()
mesg=bytearray()
env=N.NewNeticaEnviron_ns(b"",None,b"")
#env = N.NewNeticaEnviron_ns (b"",None,b"")
res = N.InitNetica2_bn (env, mesg)

print(mesg.decode("utf-8"))

net = N.NewNet_bn (b"Convertion", env)

converted = N. NewNode_bn (b"Converted", 2, net)
email     = N.NewNode_bn (b"Email", 2, net)
company   = N.NewNode_bn (b"Company", 2, net)
jobTitle  = N.NewNode_bn (b"Job_Title", 2, net)
purpose   = N.NewNode_bn (b"Purpose", 2, net)
activity  = N.NewNode_bn (b"Activity", 2, net)


N.SetNodeStateNames_bn (converted,b"Yes,         No")
N.SetNodeStateNames_bn (email,    b"Specific,    Generic")
N.SetNodeStateNames_bn (company,  b"Specified,   Not_Specified")
N.SetNodeStateNames_bn (jobTitle, b"Present,     Absent")
N.SetNodeStateNames_bn (purpose,  b"Specified,   Not_Specified")
N.SetNodeStateNames_bn (activity, b"Occured,     Not_Occured")

node_variables = {
    b"Email"     :   [b"Specific", b"Generic"],
    b"Company"   :   [b"Specified",b"Not_Specified"],
    b"Job_Title" :   [b"Present",  b"Absent"],
    b"Purpose"   :   [b"Specified",b"Not_Specified"],
    b"Activity"  :   [b"Occured",  b"Not_Occured"]
    }
node_names=list(node_variables)

N.AddLink_bn (converted, email)
N.AddLink_bn (converted, company)
N.AddLink_bn (converted, jobTitle)
N.AddLink_bn (converted, purpose)
N.AddLink_bn (converted, activity)


N.SetNodeProbs (converted, 0.1302, 0.8698)

N.SetNodeProbs (email, b"Yes", 0.8394, 0.1606)
N.SetNodeProbs (email, b"No",  0.5895, 0.4105)

N.SetNodeProbs (company, b"Yes", 0.6451, 0.3549)
N.SetNodeProbs (company, b"No",  0.1864, 0.8136)

N.SetNodeProbs (jobTitle, b"Yes", 0.6155, 0.3845)
N.SetNodeProbs (jobTitle, b"No",  0.1697, 0.8303)

N.SetNodeProbs (purpose, b"Yes", 0.40282, 0.59718)
N.SetNodeProbs (purpose, b"No",  0.13177, 0.86823)

N.SetNodeProbs (activity, b"Yes", 1.0, 0.0)
N.SetNodeProbs (activity, b"No",  0.32406, 0.67594)

N.CompileNet_bn (net)

#belief = N.GetNodeBelief (b"Converted", b"Yes", net)
#print """The probability of convertion is %g"""% belief

#for i in range(32):
#    x=map(int,bin(31-i)[2:].zfill(5))
#    msg="Given "
#    N.CompileNet_bn(net)
#    for j in  range(5):
#        N.EnterFinding (node_names[j], node_variables[node_names[j]][x[j]], net)
#        msg+="%s[%s], b" % (node_names[j], node_variables[node_names[j]][x[j]])
#    belief = N.GetNodeBelief (b"Converted", b"Yes", net)
#    print msg,b"the probability of convertion is %s"% belief

msg= "Given "
for j in  range(5):
    print("Choise for %s:\n-1 : Unknown" % node_names[j].decode('utf-8'))
    for k in range(len(node_variables[node_names[j]])):
        print(k," : ",node_variables[node_names[j]][k].decode('utf-8'))
    i = eval(input("Enter choice: "))
    if i>=0 and i<len(node_variables[node_names[j]]):
        N.EnterFinding (node_names[j], node_variables[node_names[j]][i], net)
        msg+="%s %s, " % (node_names[j].decode('utf-8'), node_variables[node_names[j]][i].decode('utf-8'))
belief = N.GetNodeBelief (b"Converted", b"Yes", net)
print(msg,"the probability of convertion is %s"% belief)

N.DeleteNet_bn (net)
res = N.CloseNetica_bn (env, mesg)

print(mesg.decode("utf-8"))
