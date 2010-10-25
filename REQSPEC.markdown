# Requirement specification for Evenio

### 1st iteration

---

## Usertypes

We have three different users:

* Anonymous user
* Registered user
* Event publisher

### Anonymous users can:

* Create event
* Edit/delete event (if: has cookie or password)
* Broadcast event updates/event (if: has cookie or password)

* View event
* "Attend" to notify publisher (if: anonymous attendees allowed)
* Sign up for updates (email)
* Write comments (if: anonymous comments allowed)
* Report an event

### Registered users can:

* Create event
* Edit/delete own event
* Cancel recurrence of event
* Broadcast event updates/changes to attendees

* View event
* Write comments
* "Attend"
* Subscribe to categories & other usercalendars (include in own calendar view)
* Subscribe to event (optional: get notifications of new comments, optional: get changes/updates from publisher via email)
* Report event

### Event publishers can:

* Create event
* Edit/delete own event
* Cancel recurrence of event
* Broadcast event updates/changes to attendees
* "Surveil" event - receive e-mail when new comments are written
* Answer to comments on own event
* Edit profile

---

## Data models

We have these following datatypes:

* Event
* Registered user profile
* Event publisher profile

### A event contains:

* Title
* Publisher
* Date & time
* Location
* Description
* Category
* Picture (optional)
* Recurring (optional)
* Allow
  * Attendees
  * Anonymous attendees
  * Comments
  * Anonymous comments
  * Comments after event (not for anonymous event)

### Registered user profile contains:

* Username
* Password
* E-mail (optional: hide)

### Event publisher profile contains:

* Name
* Username
* Password
* E-mail
* Description
* Address (optional)
* Website (optional)
