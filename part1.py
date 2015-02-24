
import pexpect
import re


#open and read the old primates command 
oldprimates = open('primates.nex').read()

#oopen the new file 
newprimates = open('newprimates.nex', 'w')

#close the new file? 
newprimates.close()

#spawn the file in mb 
child = pexpect.spawn('mb -i newprimates.nex')

#wait for promopt 
child.expect('MrBayes >')

#stop the analysis 
child.sendline(r"mcmc")

#wait for the prompt 
child.expect('Continue with analysis?', timeout = 60

#wait for the prompt 
child.expect('MrBayes >')

#print screen output
print child.before

#quit mrbayes
child.sendline('quit'( )
