# Unilab Demo API
რეპოზიტორია წარმოადგენს NLTK ბიბლიოთეკის გარშემო აწყობილ საცდელ API-ს


## Documentation

ვებ სერვისის გამოყენება შეგიძლიათ შესაბამის მისამართზე მოთხოვნის გასაგზავნად.

მოთხოვნის მისამართი და მოთხოვნის body შეგიძლიათ ნახოთ მეთოდების ჩამონათვალში

## Instruction

> 1. დაამატეთ /resource დირექტორიაში ახალი ვებ API რესურსი რომელსაც ძირითად აპლიკაციაში შემოიყვანთ შესაბამის endpoint-ზე მისაწვდომად.
> 2. დაამატეთ README.md ფაილის მეთოდების ქვეშ თქვენს რესურსზე სამუშაოდ გამიზნული მოთხოვნის მაგალითი.

## Methods:

### Postman-ის კოლექციასთან სამუშაოდ:  [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/f5b1d9ac5458f02fa932)

[<img align="middle" width="150" src="https://edit.blog.postman.com/wp-content/uploads/2015/08/postman-logo-drawing-board.png">](https://app.getpostman.com/join-team?invite_code=78f92fcf5753f9fcc222ed95db9052ca) 

პოსტმენის ლოგოზე დაწოლით შენ შეძლებ შემოუერთდე ჩვენს პოსტმენის სამუშაო გუნდს, სადაც ერთად შევძლებთ API-ს საერთო კოლექციის და მის დოკუმენტაციის აწყობას.

[პროექტის დოკუმენტაცია შეგიძლიათ ნახოთ Postman-ზე](https://documenter.getpostman.com/view/12376335/TVK7718J)

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

**FrequencyDistribution**
>
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს სიტყვების სიხშირის განაწილების სიას
> ``` 
> endpoint: _/FreqDist_
> type: GET 
> body: {
> "text" : "This is my demo text"
> } 
> ```

**GroupingMultiplePatters**
>
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს სიმბოლოებისგან გაწმენდილ ტექსტს
> ``` 
> endpoint: _/GMultiplePatterns_
> type: GET 
> body: {
> "text" : "This is my demo sentence"
> } 
> ```

**Chunk_CleanSentences**
>
> Devides and clears the sentence of punctuation marks and builds a dependency tree on each sentence. Allocates its own names and verbs.
> ``` 
> endpoint: _/Chunk
> type: GET 
> body: {
> "text" : "Any Text"
> 
**SentenceTokenizer**
> 
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს წინადადებების დანომრილ სიას.
> ```
> endpoint: _/SentTok_
> type: GET
> body: {
> "text" : "It was many and many a year ago. In a kingdom by the sea. That a maiden there lived whom you may know By the name of Annabel Lee."

> >**PosTagging**
>
> მეთოდი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და შემდეგ აკეთებს წინადადებაში მისი ნაწილების ამოცნობას. გვიბრუნდება ტოკენიზირებული ტექსტი და შესაბამისი მეტყველების ნაწილები.
> ```
> endpoint: _/PosTag_
> type: GET
> body: {
> "text" : "This is my demo text"
> }
> ```
**DepTreeSvgMaker**
>
> Created dependency tree svg image and returns
> ``` 
> endpoint: _/DepTree
> type: GET 
> body: {
> "sentence" : "Any Text"

**SentToken**
>
> ტექსტში წინადადებების ტოკენიზაცია
>```
> endpoint: _/SentToken
> type: GET
> body: {
>"text" : "At least one sentence."
>}
>```