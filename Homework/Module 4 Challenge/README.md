# School District Analysis

## Overview
We have done a detailed analysis for the school district before. However, it has come to Education Board's attention about the academic dishonesty specifically for "Thomar High School". They have evidence that the school's ninth grade data both for reading and math grades has been altered.

### Purpose of this Analysis
The Education Board wants to uphold state-testing standard and need further help. Since the data we have for ninth garde "Thomar High School" has been mis-appropriated, our previous analysis wouldn't be accurate. To help the Education Board make the decision based on the acutual data, we are now required to drop reading & math ninth grade data for "Thomas High School" from our analysis and then rerun the entire analysis with this known fact of partial data elimination.


## Analysis Results
1. **The district summary:** There's a very small change (1/10th, 1/5th, 3/10th) in District Summary Data. 

[Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/District%20Summary_new.png)

![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/District%20Summary_new.png)

2. **The school summary:** After dropping ninth graders math and reading scores for Thomas High School, 
   1. The passing **math** percentage **dropped from 93.27% to 66.91%**
   1. The passing **reading** percentage **dropped from 97.30% to 69.66%**
   1. The passing **overall** percentage **dropped from 90.94% to 65.07%**
   1. The average math and the average reading scores delta is not significant as per analysis reports.

 [Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/School%20Summary_New.png)
 ![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/School%20Summary_New.png)

3. **The top 5 performing schools, based on the overall passing rate:** Before dropping ninth graders reading and math scores from our analysis, Thomase High School **was ranked 2nd** based on its overall passing percentage of **90.948012%**. But after the drop, Thomase High School lost its ranking to **8th position** based on its overall passing percentage of **65.076453%**.

[Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/Top%205%20Schools_New.png)
![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/Top%205%20Schools_New.png)

4. **The lowest 5 performing schools, based on the overall passing rate:** The bottom 5 performers stays **unchanged**. 

[Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/Bottom%205%20Schools_New.png)
![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/Bottom%205%20Schools_New.png)

5. **The average math score for each grade level from each school:**  As we refer the before and after analysis report, we notice that the overall averages for all the schools but 9th grade math average for Thomas High School, remains intact. **The 9th grade math averages for Thomas High School now shows NaNs**. This confirms that we dropped the right set of data as per the requirements.

[Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/The%20Average%20Math%20Scores_New.png)
![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/The%20Average%20Math%20Scores_New.png)

6. **The average reading score for each grade level from each school:** As we refer the before and after analysis report, we notice that the overall averages for all the schools but 9th grade reading average for Thomas High School, remains intact. **The 9th grade reading averages for Thomas High School now shows NaNs**. This confirms that we dropped the right set of data as per the requirements.

[Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/The%20Average%20Reading%20Scores_New.png)
![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/The%20Average%20Reading%20Scores_New.png)

7. **The scores,** 
    1. **By school spending per student:** The impact of implemented change did not affect the spending ranges per student for Thomas High School and other schools. However, the passing percentages (math, reading, and overall) changed as expected and also discuused above in previous metrices.
       1. % Passing Math changed from 73% to 67%
       1. % Passing Reading changed from 84% to 77%
       1. % Overall Passing changed from 63% to 56%
       1. The avergae Math and Reading scores changed to the second decimal places (the report displays only to 1st decimal places so we notice no change)
       
       [Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/The%20Scores%20by%20School%20Spending%20Per%20Student_New.png)
       ![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/The%20Scores%20by%20School%20Spending%20Per%20Student_New.png)


    1. **By School Size:**  
       1. % Passing Math changed from 94% to 88%
       1. % Passing Reading changed from 97% to 91%
       1. % Overall Passing changed from 91% to 85%
       1. The avergae Math and Reading scores changed to the second decimal places (the report displays only to 1st decimal places so we notice no change)

       [Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/The%20Scores%20by%20School%20Spending%20by%20School%20Size_New.png)
       ![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/The%20Scores%20by%20School%20Spending%20by%20School%20Size_New.png)

    1. **By School Type:**  
       1. % Passing Math for Charter School changed from 94% to 90%
       1. % Passing Reading for Charter School changed from 97% to 93%
       1. % Overall Passing for Charter School changed from 90% to 87%
       1. The avergae Math and Reading scores changed to the second decimal places (the report displays only to 1st decimal places so we notice no change)
       **Note: Thomas High School is a Charter school**
       
       [Refer before and after analysis report.](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%204%20Challenge/Analysis/The%20Scores%20by%20School%20Spending%20by%20School%20Type_New.png)
       ![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%204%20Challenge/Analysis/The%20Scores%20by%20School%20Spending%20by%20School%20Type_New.png)



## Summary
It is interesting to observe the changes the district analysis after the math and reading scores have been replaced. Following are the key changes:
1. Though the district summary did not have a major impact, however, the school summary had a big impact. The overall passing percentage dropped from ~91% to ~65%. Individual percentages for math and reading were also dropped with the similar magnitude.
1. Thomas High School, which used to be at 2nd position in the top 5 performing schools now stands at 8th position.
1. The scores by school spending per student were dropped by approximately 7%.
1.  The scores by school spending based in school size were dropped by approximately 6%.
1. The scores by school spending based in school type (Charter) were dropped by approximately 3%-4%.

## Conclusions:
We only replaced 461 rows for 9th grade and one school only, however, the analysis highlighted some interesting facts. The magnitude of the impact is quite surprising. We really enjoyed re-dong this analysis and there was enormous learning in this process. 
