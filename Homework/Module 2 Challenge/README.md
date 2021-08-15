# Refactoring the Code

> _**NOTE: In the deliverables I have included the PNGs from the previous Challenge for comparision.**_

## Overview of Project
Steve loved the outcomes we prepared for him. He wonders, what if the number of stocks increases from a dozen to hundreds and to thousands; will the same code work and if it would then what would be the impact on its performance.

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
#### **Advantages and disadvantages (in General)**

**The major advantages** of refactoring is that it improves the quality of code and its performance, a better design, , more structured, and easy to understand, easy to maintain & debug. 

**The common disadvantages** includes the risk of making the code changes (without effecting the existing functionality), expensive, time consuming, and may introduce new bugs.

##
#### **Advantages (comparing refactored and original code)**
1. Refactored code leads to a better quality code, imporoves performance, and reduces the posibility of run-time errors. In this case the refactoring lead to run code 5 times faster than the original code.
1. Since the code is more structured and easier to follow through, the code maintenance is less expensive post-refactoring in comparison to the original code.
1. Since in Refactoring process we use more built-in functions so, it could possibly reduce the length of the code and improves the overall code and application design. The original code could be long, difficult to understand, cumbersent, and redundent.
1. Since the refactored code is structured, the debugging is easier, its more adaptive, it improves readability and reduces complexity, and it enhances the code reusability. The original code could be difficult to read, more complex, redundant, and many not be easily reused.

**Disadvantages**
1. The refactoring an exisiting code could be expeansive and more time consuming especially due to lacking documentation, if any. Original code is working fine and no changes are needed unless any bugs or needed additional functionality.
 1. Since, the working code is redone/re-engineered, it imposes certain business risk. To reduce this business risk, more and focused testing efforts may become necessary accounting toward the total cost. The original code was vigourously tested before, and over the period of time with bug fixes, it is almost bug free now. So, **why to break something that's working?** 
1. During the refactoring process developers should be proficient in reading and understanding other developer's code, document it (if original documentation is missing), and develop the strategy to refactor and improve the code, before starting to implement code changes. This is all time consuming and not cost effective. With the original code there's a very little to no management cost. 
1. It may introduce new bugs that never existed before in old/existing code. In original code, the bugs were ironed out over the period of time, since its original implementation.

**NOTE:** I am sure there are many more advantages and disadvantages of refactoring the code. 

At the other hand, there are certainly some advantages and disadvantages in keeping the original code too. 

##
#### **To conclude**

**The real question** is, why do we want to refactor some code? One (management) must weigh in these advantages and disadvantages and decide **if refactoring will bring them business value now and/or in the long run**. Based on the situation and business requirements, not all the time, refactoring is a good choice/decision/solution, however, we may still end up doing it or we may decide to rewrite the application/code.



---