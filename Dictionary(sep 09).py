Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Dictionary
#dict{}
a={"name":"Bhavika","city":"Vij"}
print(a)
{'name': 'Bhavika', 'city': 'Vij'}
type(a)
<class 'dict'>
#Methods
a={"Year":2026,"Month":"Sep","date":09}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a={"Year":2026,"Month":"Sep","date":9}
a.values()
dict_values([2026, 'Sep', 9])
a.items()
dict_items([('Year', 2026), ('Month', 'Sep'), ('date', 9)])
#accessing particular value
a["Year"]
2026
a.get("Year")
2026
a["date"]
9
a.get["Month"]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.get["Month"]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.get("Month")
'Sep'
#to add data into a dictionary
#update
a.update({"Mailid":"bhavika@gmail.com"})
a
{'Year': 2026, 'Month': 'Sep', 'date': 9, 'Mailid': 'bhavika@gmail.com'}
a.update({"Gender":"Female", "Country":"India"})
a
{'Year': 2026, 'Month': 'Sep', 'date': 9, 'Mailid': 'bhavika@gmail.com', 'Gender': 'Female', 'Country': 'India'}
#setdefault
#by default it consider the data as a key-value pair
a={"hour":3,"min":10}
a.setdefault("sec",50)
50
a
{'hour': 3, 'min': 10, 'sec': 50}
#pop()
a={"country":"India", "city":"Vij"}
a.pop("city")
'Vij'
a
{'country': 'India'}
#popitem()
a={"Fruits":"Grapes","Vegetables":"Tomato","Nuts":"Badam"}
a.popitem()
('Nuts', 'Badam')
a
{'Fruits': 'Grapes', 'Vegetables': 'Tomato'}
#copy()
a.copy()
{'Fruits': 'Grapes', 'Vegetables': 'Tomato'}
a
{'Fruits': 'Grapes', 'Vegetables': 'Tomato'}
len(a)
2
a.count("Fruits")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.count("Fruits")
AttributeError: 'dict' object has no attribute 'count'
>>> a
{'Fruits': 'Grapes', 'Vegetables': 'Tomato'}
>>> a.clear()
>>> a
{}
>>> 
>>> #It doesn't allow duplicate keys
>>> #if it contains duplicate keys it always picks last one, so that it doesn't has index method and count
>>> a={"Name":"Bhavika","course":"Python","Name":"Bhavike"}
>>> a
{'Name': 'Bhavike', 'course': 'Python'}
>>> a={"Name":"Bhavika","course":"Python","Name1":"Bhavika"}
>>> aa
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    aa
NameError: name 'aa' is not defined. Did you mean: 'a'?
>>> a
{'Name': 'Bhavika', 'course': 'Python', 'Name1': 'Bhavika'}
>>> #passing multiple values to a single key
>>> a={"idnos":[10,20,30],"Names":["Bhavika","sailaja","varshitha"],"Places":["Swiss","Australia","Germany"]}
>>> a
{'idnos': [10, 20, 30], 'Names': ['Bhavika', 'sailaja', 'varshitha'], 'Places': ['Swiss', 'Australia', 'Germany']}
>>> a.values()
dict_values([[10, 20, 30], ['Bhavika', 'sailaja', 'varshitha'], ['Swiss', 'Australia', 'Germany']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('Names', ['Bhavika', 'sailaja', 'varshitha']), ('Places', ['Swiss', 'Australia', 'Germany'])])
>>> a.keys()
dict_keys(['idnos', 'Names', 'Places'])
