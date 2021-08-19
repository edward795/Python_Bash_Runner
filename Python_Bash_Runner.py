#import required modules.
import os
import subprocess 

#custom function to run shell scripts by taking path and command as parameters.
def BashRunner(path,command,cwd,count):
    os.chdir(cwd)
    print("Moved to path {0}".format(path))
    print("Running job {0} ----> {1}.".format(count,command))
   
   #open a filw with context manager to autoclose the file.
    with open("scriptRunner.log","a+") as f:
        os.chdir(path)
        
        #run the shell script and process output & error.
        process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        process.wait()

        os.chdir(cwd)
        
        #write output or error if it exists to the log file.
        f.write("\n\n\n")
        f.write("***********************************************************************************")
        f.write("\n")
        f.write("######### Running Job {0} ----> {1} ###########.".format(count,command))
        f.write("\n")
        f.write("************************************************************************************")
        f.write("\n\n")

        while True:
            output,error=process.communicate() 
            if output:
                out=output.decode('utf-8')
                f.write("\n")
                f.write(str(out))
                
            if error:
                err=error.decode('utf-8')
                f.write("\n")
                f.write(str(err))

            result=process.poll()
            if result is not None:
                break
        print("*************************************************************")
        
        
    
#main function where program execution starts.
if __name__=='__main__':
        
        #read path & shell commands from text file and store them.
        cwd=os.getcwd()
        file_path=os.path.join(cwd,'jobs.txt')
        f=open(file_path,'r+')
        content=f.readlines()
        f.close() 
        
        #check if the log file exists or create it,if the file exists clear the file contents.
        log_path=os.path.join(cwd,'scriptRunner.log')
        if os.path.exists(log_path):
            file=open(log_path,'r+')
            file.truncate(0)
            file.close()
        else:
            with open('scriptRunner.log', 'w') as fp:
                pass

        #loop through path & commands and call thr script running function.
        count=1
        for i in content:
            data=i.split('|')
            p=data[0]
            c=data[1]
            path=str(p).strip()
            command=str(c).strip()
            BashRunner(path,command,cwd,count)
            count+=1




