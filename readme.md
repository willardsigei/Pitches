# Pitches

#### Author: [Kipngeno Sigei](https://github.com/willardsigei)


* Link to live site: https://pitche--app.herokuapp.com/

## Description
This is an application that allows one to read other peoples pitches or create their own. Also one can post a comment and like or dislike the viewed pitches.

## User Stories
The user would like to.... :
* see the pitches other people have posted.
* vote on the pitch they liked and give it a downvote or upvote.
* view the pitches I have created in my profile page
* submit a pitch in any category.
* view the different categories.



## Behaviour Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View Pitch category | Click on any category | Taken to the clicked category 
| Click on `Click    new pitch` | Redirected to the login page if not logged in | Signs In/ Signs Up |
| Click on `Click create new pitch` | If logged in, display form to add a pitch | Redirected to the home page |
| Click add comment button | Redirects to the comment page | Displays a comment form and a like and dislike button
| Click on Sign Out | Redirects to the home page | Signs user out |
| Click on profile | Redirects to the profile page | User adds bio and profile picture and views pitches the user has made|

## Built With

* [Python3.8](https://docs.python.org/3/)
* Flask
* Boostrap

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)