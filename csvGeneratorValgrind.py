class csvGeneratorValgrind(object):
    
    def __init__(self):
        self.perf = ['D1  miss rate:']
        self.csv = "logsValgrind.csv"

    def generate(self):
        import glob

        opened = open(self.csv, "w")

        opened.write('algorithm,entries,dx,dy,dz,d1_miss_rate\n')

        for filename in glob.glob("logsValgrind/*"):
            fileA = open(filename, "r")
            save = ('"' + filename.split("/", 1)[1].split("#", 1)[0] + '"')
            memoryDatas = filename.split("#")[1].split('.',1)[0].split('x')

            save += (',' + memoryDatas[0] + ',' + memoryDatas[1] + ',' + memoryDatas[2] + ',' + memoryDatas[3])
            
            for line in fileA:
                for data in self.perf:
                    if data in line:
                        save += (',' + line.strip().split(":",1)[1].split("%",1)[0].strip())
            
            opened.write(save + "\n")
        
        opened.close()