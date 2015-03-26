import matplotlib.pyplot as plt
import sys

#filename = 'OverNightFiveMinutes.txt'
#filename = 'AtWork5Minutes9Hours.txt'
#filename = 'RainySaturday3Hours.txt'
#filenames = ['OverNightFiveMinutes.txt', 'AtWork5Minutes9Hours.txt', 
#	'RainySaturday3Hours.txt']

if(len(sys.argv)>1):
    try:
        filename = str(sys.argv[1])

        #for filename in filenames:
        data_points = []
        nums = []
        count = 0
        with open(filename, "r") as data:    
            for line in data:
                data_points.append(line.split(',')[0])
                nums.append(count)
                count += 1
        
        plt.plot(nums, data_points, 'ro')
        plt.axis([0,288,500,900])
        plt.title(filename)
        plt.savefig(filename+".png")
        plt.show()        
        
        
    except:
        print 'Bad input, enter a file name as an argument.'
else:
    print 'Try again, use a filename as an argument.' 


