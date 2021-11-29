import os

flag=1
val=0
while flag:
    print('Welcome to Big Data Processing Application:')
    print('Please type the number that corresponds to which appplication you would like to run:')
    print('1.Apache Hadoop')
    print('2.Apache Spark')
    print('3.Jupyter Notebook')
    print('4.SonarQube and SonarScanner')
    print('5.Terminate application')
    
    try:
        val=int(input('Enter your choice: '))
    except EOFError:
        continue

    if val==1:
        print('Hadoop: Go to ip and port: 35.225.164.126:50070')
    if val==2:
        print('Spark: Go to ip and port:  34.132.23.141:8080')
    if val==3:
        print('Jupyter: Go to ip and port: 34.136.83.235:8888')
    if val==4:
        print('Go to ip and port: 104.197.32.45:9000')
    if val==5:
        print('Bye!')
        os._exit(1)
    
