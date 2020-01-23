# Graphical-Data-Faker

a Simple tool that will generate Personal details for use during development or testing.

> Only supports Python `3.7.*` for now

For now, this will only spoof:  
* `First Name`
* `Last Name`
* `RSA ID Number` (user can also specify age if required)
* `ZA Cell Numbers`
* `Email Address`  

Please note that by design, this is for use in South Africa only.

Next Steps:
* Create this a s a standalone executable. (OS independent)  
* Add functionality to generate Business details.
* Internationalize the functionality to cater for Passports, etc...

### Libraries Used
* `pyperclip`
* `random` (with randrange)
* `tkinter` (with ttk)
* `datetime`
* `faker`