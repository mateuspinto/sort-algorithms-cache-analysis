class csvGenerator(object):
    
    def __init__(self):
        self.perf = ['cache-references', 'cache-misses', 'task-clock', 'cycles', 'instructions']
        self.csv = "logs.csv"

    def generate(self):
        import glob

        opened = open(self.csv, "w")

        opened.write('algorithm,entries,cache-references,cache-references-relat,cache-misses,cache-misses-relat,task-clock,task-clock-relat,cycles,cycles-relat,instructions,instructions-relat,elapsed-seconds\n')

        for filename in glob.glob("logs/*"):
            fileA = open(filename, "r")
            save = '"' + filename.split("/", 1)[1].split("#", 1)[0] + '",' + filename.split("#")[1] + ','
            
            for line in fileA:
                for data in self.perf:
                    if data in line:
                        swap = line.strip()
                        save += (swap.split(" ",1)[0].replace(".","").replace(",","."))
                        save += ("," + swap.split("#")[1].strip().split()[0].replace(".","").replace(",",".") + ",")
                if "elapsed" in line:
                    save += (line.strip().split()[0].replace(".","").replace(",","."))
            
            opened.write(save + "\n")
        
        opened.close()

a = csvGenerator()
a.generate()