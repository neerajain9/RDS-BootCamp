# Refactoring the Code

> _**NOTE: In the deliverables I have included the PNGs from the previous Challenge for comparision.**_

## Overview of Project
Steve loved the outcomes we prepared for him. He realized if the number of stocks increases from a dozen to hundreds and to thousands, it takes long time to run the script to see the results.

### Purpose
To optimize the code to ensure that it runs more efficiently. COmpare the time it took to run the previous code and this code and analyze the difference and adapt better coding practices.

---
## Results
The results are amazing. Refer the following outputs with the timer count before and after refactoring the code.

### **2017 (Refactored Code)**


![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%202%20Challenge/VBA_Challenge_2017.png) 

### **2017 (Previous Code)**

![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%202%20Challenge/VBA_Challenge_2017%20(Previous%20Module).png) 

The above two snap shots (for year 2017) suggests that before refactoring it took it took 0.984375 seconds to run the analysis whereas the refactored code reduced the overall run time to 0.1953125 seconds. These code changes reduce the run time to 1/5th.

##
### **2018 (Refactored Code)**

![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%202%20Challenge/VBA_Challenge_2018.png) 

### **2018 (Previous Code)**

![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%202%20Challenge/VBA_Challenge_2018%20(Previous%20Module).png) 

The snap shots for year 2018 also suggests that before refactoring it took it took 1 seconds to run the analysis whereas the refactored code reduced the overall run time to 0.203125 seconds. These code changes reduce the run time to 1/5th.

**NOTE:** Considering the similar volume of data for year 2017 and 2018, the refactored code performed consistantly; **5 times faster** 

##
### Summary
**Advantages**
1. Factored code reduced the code run-time to 20% of the original unfactored code.
1. The length of the code is reduced to some extent as well.
1. The code is more structured and easier to follow through.

**Disadvantages**
1. The code could be more complex to debug.
1. The arrays/indexes requires carefull handling.
1. The code changes or additional fuctionalty may become challenging based on the business requirments.

---