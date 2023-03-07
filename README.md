<div id="top"></div>

<p align="center">
  <img src="images/cover_image.jpg">
</p>

<!-- ABOUT THE PROJECT -->
##  ORM-2-SQL Package

I built a Python package helps developers visualize their Django ORM queries as SQL queries and obtain additional statistics about them.

<!-- HOW TO USE -->
## Getting Started

This will be a simple guide on how you can add this middleware into your Django project.


### Requirements

Apart from Django and Python, the package will automatically install the
following packages:

- [sqlparse](https://pypi.org/project/sqlparse/)
- [Pygments](https://pygments.org/)


### Add the Middleware

Go to your settings.py file inside your project directory. Add 

```python
MIDDLEWARE = [
    'orm-2-sql-visualizer.middleware.new_middleware',
]
```


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Erol Gelbul - [Website](erolgelbul.com)

Project Link: [ORM2SQL](https://github.com/ErolGelbul/orm-2-sql-visualizer)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->