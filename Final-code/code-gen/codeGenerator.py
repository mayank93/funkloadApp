TEMPLATE_FILE = 'Template.conf'
def createCode(URL, nb_time, duration, cycles, destFile):
        s = ''
	conf_file = open(TEMPLATE_FILE, 'r').read()
	l = cycles.split(",")
        s = ':'.join(l)
	stress_file_mapped = conf_file % (URL, nb_time, s, duration)
        destHandle = open(destFile, 'w+')
        with open(destFile, 'w+') as d:
            d.write(stress_file_mapped)

createCode('localhost', '20', '10', '50,75,100', 'newConf.conf')
