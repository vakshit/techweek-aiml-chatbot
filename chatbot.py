import aiml
import os
import webbrowser
#webbrowser.open("https://www.google.com")
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "active.xml")
    kernel.bootstrap(learnFiles = "death.xml")
    kernel.bootstrap(learnFiles = "hospital.xml")
    kernel.bootstrap(learnFiles = "main.xml")
    kernel.bootstrap(learnFiles = "total.xml")
    kernel.bootstrap(learnFiles = "startup.xml")
# kernel now ready for use
I = input (">>>") 
while I!= "exit":
    print (kernel.respond(I))
    print ("")
    I =input (">>>")

# kernel.saveBrain("bot_brain.brn")