# Unilab Demo API
რეპოზიტორია წარმოადგენს NLTK ბიბლიოთეკის გარშემო აწყობილ საცდელ API-ს


## Documentation

ვებ სერვისის გამოყენება შეგიძლიათ შესაბამის მისამართზე მოთხოვნის გასაგზავნად.

მოთხოვნის მისამართი და მოთხოვნის body შეგიძლიათ ნახოთ მეთოდების ჩამონათვალში

##Methods:

**TemSentenceTokenizer**
>
> სერვისი მოთხოვნილ წინადადებას უკეთებს ტოკენიზაციას და აბრუნებს ტოკენიზებულ სიას
> ``` 
> endpoint: _/TemSenTok_
> type: GET 
> body: {
> "sentence" : "This is my demo sentence"
> } 
> ```
> 
**MarvelFrequencyDistribution**
>
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს სიტყვების სიხშირის განაწილების სიას
> ``` 
> endpoint: _/FreqDist_
> type: GET 
> body: {
> "text" : "This is my demo text"
> } 
> ```