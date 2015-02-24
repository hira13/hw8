import pexpect
import re


#start MrBayes with newprimates.nex 
child = pexpect.spawn('mb -i newprimates.nex')

#if MrBayes > than it will expect 
child.expect('MrBayes >')

#run the analysis
child.sendline(r'sumt')

#wiat for Mr.Bayes prompt
child.expect('MrBayes >')


#print everything before the prompt
print child.before

#run command sumpm 
child.sendline(r'sump')

#wait for prompt
child.expect('MrBayes >')

#print everything before mrbayes prompt
print child.before

#quit
child.sendline('quit')
