



# Date
  
Module to manage dates  

*Read this in other languages: [English](Manual_Fechas.md), [Português](Manual_Fechas.pr.md), [Español](Manual_Fechas.es.md)*
  
![banner](imgs\Banner_fechas.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Date format
  
Change the format of a date
|Parameters|Description|example|
| --- | --- | --- |
|Date |Date to which the format will be changed|19/10/2000|
|Result |Variable where the result will be stored|date|
|Input format|Format that has the entered date|dd/mm/yyyy|
|Output format |Format that will have the date received|dd/mm/yyyy|
|Custom input |If the date format is different from the options above, it must be entered in this field.|%d/%m/%y|
|Custom output |If the format of the date to be received is different from the previous options, it must be entered in this field.|%d/%m/%y|

### Get weekday
  
Gets the day of the week of the entered date. By default 0 is Monday and 6 is Sunday.
|Parameters|Description|example|
| --- | --- | --- |
|Date |Field to enter the date.|19/10/2000|
|Start day Monday from 1|Activate it if you want Monday to be 1 instead of 0 as default.|False|
|Input format|Format that has the entered date.|dd/mm/yyyy|
|Result |Variable where the result will be saved.|date|

### Calculation over dates
  
Add and subtract values on a date
|Parameters|Description|example|
| --- | --- | --- |
|Date |Date to be used in the calculation|19/10/2000|
|Input format|Format that has the entered date.|dd/mm/yyyy|
|Result |Variable where the result will be stored|date|
|Amount to be subtracted or added|Number that will be subtracted or added from the entered date.|3|
|Type of date|Type of date you want to subtract or add|days|

### Get week number
  
Gets the number of the week.
|Parameters|Description|example|
| --- | --- | --- |
|Date |Date from which you want to get the number of the week|19/10/2000|
|Input format|Format that has the entered date.|dd/mm/yyyy|
|Result |Variable where the result will be stored|date|

### Get week number of month
  
Gets the number of the week of the month entered.
|Parameters|Description|example|
| --- | --- | --- |
|Date |Date from which you want to get the number of the week|19/10/2000|
|Input format|Format that has the entered date.|dd/mm/yyyy|
|Result |Variable where the result will be stored|date|

### Date comparation
  
Date comparation
|Parameters|Description|example|
| --- | --- | --- |
|Date 1 |Date 1 to compare|19/10/2000|
|Operation|Operation to be carried out between the dates entered.|<|
|Date 2 |Date 2 to compare|19/10/2000|
|Result |Variable where the result will be stored|result|
|Input format|Format that has the entered date|dd/mm/yyyy|
|Custom input |Complete in case you want to use another date format.|%d/%m/%y|

### Days between dates
  
This command allows you to obtain the number of days between two dates.
|Parameters|Description|example|
| --- | --- | --- |
|Date 1 |Date 1 to compare|30/10/2021|
|Date 2 |Date 2 to compare|10/10/2022|
|Input format|Format that has the entered date|dd/mm/yyyy|
|Custom input |Complete in case you want to use another date format.|%d/%m/%y|
|Result |Variable where the result will be stored|result|

### Get age from date of birth
  
Gets the age from a person's date of birth
|Parameters|Description|example|
| --- | --- | --- |
|Date |Date from which you want to obtain the person's age in the YYYY-MM-DD format|YYYY-MM-DD|
|Result |Variable where the result will be stored|result|
