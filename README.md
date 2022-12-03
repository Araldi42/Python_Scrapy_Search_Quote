# Python_Scrapy_Search_Quote
 This project aims to use, through Web Scraping, a price tracker of the USD/BRL - American Dollar Brazilian Real quotation, informing when the entered value is found and thus optimizing the decision making of businesses that depend on the current exchange rate for taking action 

-----------------------------------------------------------------------

HOW TO USE:

1- First you must have python installed on your machine
2- Then you must open a cmd from your machine
3- Go to the repository where the file "rastreia_cota.py" is installed on your machine
4- Write in cmd the command "python rastreia_cota.py"
5- Write in cmd program which value you are looking for (The value must be a float followed by only two characters after the separator)
After the previous steps are completed the scraping will start and will notify you when the value is found

Important: 
- The value of the input need's to be write using "." as separator
and the tracker only works until as 6:00 Pm Because it is usually the time when the workdays end and the trading floor ceases to be operated.
- Make sure you have installed all the libraries that are used in the script on your machine.

- the libraries are:
                     scrapy
                     pandas
                     time
                     subprocess
                     datetime
                     

-----------------------------------------------------------------------  
