<div id="top"></div>

<p align="center">
  <img src="images/cover_imagev3.jpg">
</p>

<!-- ABOUT THE PROJECT -->
##  ORM-2-SQL Package

I built a Python package helps developers visualize their Django ORM queries as SQL queries and obtain additional statistics about them.

<!-- HOW TO USE -->
## Getting Started

This will be a simple guide on how you can add this middleware into your Django project.


### <ins>Requirements</ins>

Apart from Django and Python, the package will automatically install the
following packages:

- [sqlparse](https://pypi.org/project/sqlparse/)
- [Pygments](https://pygments.org/)


### <ins>Install from PyPI</ins>

```bash
pip install orm-2-sql-visualizer
```

### <ins>Add the Middleware</ins>

Go to your settings.py file inside your project directory. Add 

```python
MIDDLEWARE = [
    'orm-2-sql-visualizer.middleware.new_middleware',
]
```

### <ins>Results</ins>

For each ORM operation, the SQL query will be displayed. If you want to see the
query, run:

```bash
pytest -rP
```

Example:
```bash
===============================================
                [SQL Queries]
===============================================
SELECT "demo_app_product"."id",
       "demo_app_product"."name"
FROM "demo_app_product"
```

Additional stats will also be displayed along side of the queries:

```bash
===============================================
                 [SQL Stats]
===============================================
Total queries: 1
Total execution time: 0.000ms
Duplicate queries: 0
===============================================
```


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Erol Gelbul - [Website](erolgelbul.com)

Project Link: [ORM2SQL](https://github.com/ErolGelbul/orm_2_sql_visualizer)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
