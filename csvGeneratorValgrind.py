class csvGeneratorValgrind(object):
    
    def __init__(self):
        self.perf = ['I1  miss rate:', 'D1  miss rate:', 'LL miss rate:']
        self.csv = "logsValgrind.csv"

    def generate(self):
        import glob

        opened = open(self.csv, "w")

        opened.write('algorithm,entries,ix,iy,iz,dx,dy,dz,lx,ly,lz,i1_miss_rate,d1_miss_rate,ll_miss_rate\n')

        for filename in glob.glob("logsValgrind/*"):
            fileA = open(filename, "r")
            save = ('"' + filename.split("/", 1)[1].split("#", 1)[0] + '"')
            memoryDatas = filename.split("#")[1].split('x')
            memoryDatas.remove('')

            for data in memoryDatas:
                save += (',' + data)
            
            for line in fileA:
                for data in self.perf:
                    if data in line:
                        save += (',' + line.strip().split(":",1)[1].split("%",1)[0].strip())
            
            opened.write(save + "\n")
        
        opened.close()