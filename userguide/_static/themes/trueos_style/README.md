#TrueOS Style 

###Creating a new theme for iX docs.

**Instructions for using trueos_style:**

* Edit the Sphinx project's conf.py file:

* Change this value to trueos_style prior to generating docs:
```
  html_theme = 'trueos_style'
```
* No additional html_options yet.

* Be sure Sphinx knows the path to the custom theme:
```
  html_theme_path = ['themes']
```
#trueos_style is intended to be used in many iX stystems sphinx generated handbooks, with small style changes here and there.
