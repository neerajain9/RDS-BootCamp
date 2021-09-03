# School District Analysis

## Overview
We have done a detailed analysis for the school district before. However, it has come to Education Board's attention about the academic dishonesty specifically for "Thomar High School". They have evidence that the school's ninth grade data both for reading and math grades has been altered.

### Purpose of this Analysis
The Education Board want to uphold state-testing standard and need further help. Since the data we have for ninth garde "Thomar High School" has been mis-appropriated, our previous analysis wouldn't be accurate. To help the Education Board make the decision based on the acutual data, we are now required to drop reading & math ninth grade data for "Thomas High School" from our analysis and then rerun the entire analysis with this known fact of partial data elimination.


## Analysis Results
1. **The district summary:** There's a very small change (1/10th, 1/5th, 3/10th) in District Summary Data. 

Refer before and after analysis report.

1. **The school summary:** After dropping ninth graders math and reading scores for Thomas High School, 
   1. The passing **math** percentage **dropped from 93.27% to 66.91%**
   1. The passing **reading** percentage **dropped from 97.30% to 69.66%**
   1. The passing **overall** percentage **dropped from 90.94% to 65.07%**
   1. The average math and the average reading scores delta is not significant as per analysis reports.

 Refer before and after analysis report.

1. **The top 5 performing schools, based on the overall passing rate:** Before dropping ninth graders reading and math scores from our analysis, Thomase High School **was ranked 2nd** based on its overall passing percentage of **90.948012%**. But after the drop, Thomase High School lost its ranking to **8th position** based on its overall passing percentage of **65.076453%**.

Refer before and after analysis report.

1. **The lowest 5 performing schools, based on the overall passing rate:** The bottom 5 performers stays **unchanged**. 

Refer before and after analysis report.

1. **The average math score for each grade level from each school:**  As we refer the before and after analysis report, we notice that the overall averages for all the schools but 9th grade math average for Thomas High School, remains intact. **The 9th grade math averages for Thomas High School now shows NaNs**. This confirms that we dropped the right set of data as per the requirements.

Refer before and after analysis report.

1. **The average reading score for each grade level from each school:** As we refer the before and after analysis report, we notice that the overall averages for all the schools but 9th grade reading average for Thomas High School, remains intact. **The 9th grade reading averages for Thomas High School now shows NaNs**. This confirms that we dropped the right set of data as per the requirements.

Refer before and after analysis report.

1. **The scores,** 
    1. **By school spending per student:** The impact of implemented change did not affect the spending ranges per student for Thomas High School and other schools. However, the passing percentages (math, reading, and overall) changed as expected and also discuused above in previous metrices.
       1. % Passing Math changed from 73% to 67%
       1. % Passing Reading changed from 84% to 77%
       1. % Overall Passing changed from 63% to 56%
       1. The avergae Math and Reading scores changed to the second decimal places (the report displays only to 1st decimal places so we notice no change)


    1. **By School Size:**  
       1. % Passing Math changed from 94% to 88%
       1. % Passing Reading changed from 97% to 91%
       1. % Overall Passing changed from 91% to 85%
       1. The avergae Math and Reading scores changed to the second decimal places (the report displays only to 1st decimal places so we notice no change)

    1. **By School Type:**  
       1. % Passing Math for Charter School changed from 94% to 90%
       1. % Passing Reading for Charter School changed from 97% to 93%
       1. % Overall Passing for Charter School changed from 90% to 87%
       1. The avergae Math and Reading scores changed to the second decimal places (the report displays only to 1st decimal places so we notice no change)
       **Note: Thomas High School is a Charter school**



Following is a [snippet of our analysis](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%203%20Challenge/analysis/Output%20on%20the%20terminal.png) that we ran electronically. [Click here](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%203%20Challenge/analysis/election_results.txt) to see the output text file.

![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%203%20Challenge/analysis/Output%20on%20the%20terminal.png)
![] 


## Election Audit Summary
Now, that we have run this amazing analysis/audit, the Election Commission now do not need to go through the painful manual analysis down the road.

The same script can be used to run the similar audit;  simply by replacing the "election_results.csv" file and executing this python script.

Like any audit/analysis there's always room to identify various aspects that could be helpful in certain ways to certain decision making groups. We think following changes/additions to the exisiting audit could bring some interesting facts that are hidden behind the data. We are presenting only couple of suggestions, however, we are sure there could be other avenue that may be explored.
1. It would be interesting to know if any specific candidate was more popular in a specific county. The popularity reasons could further be drilled down based on voter's demographics, candidate's residency in the county, candidate's work/efforts in making that county a better place to live, etc.
1. Also, the ratio of county votes against each other could be a significant pointer to establish an understanding the relationship with each county and the contesting candidate in that county. In other words, is there any co-relation that a candidate is more popular in one county than other?

## Conclusions:
Like in any analysis projects one needs to be more thoughtful to ask the right questions. And, how these questions are helpful in addressing certain concerns and/or improvements in the process overall. We are glad we could lend a hand and hope to have much deeper and meaningful analysis, impacting the decision making process, in other projects down the line.
