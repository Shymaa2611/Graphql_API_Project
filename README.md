# Graphql_API_Project
steps:-
<p> 1-install strawberry-graphql and strawberry-graphql-django</p>
<p> 2- add  "strawberry" to INSTALLED_APPS</p>
<p> 3- create schema.py file and types.py file in your app</p>
<p> 4- add this in project/urls.py</p>
<p>  from strawberry.django.views import GraphQLView</p>
  <p>from api.schema import schema</p>
    <p> urlpatterns = [path("graphql", GraphQLView.as_view(schema=schema))]</p> 
     
    <p> run http://127.0.0.1:8000/graphql</p>
  

![Description](https://github.com/Shymaa2611/Graphql_API_Project/assets/137145389/5d84a4ce-4133-418a-b70e-cab27ac7c490)

![Description](https://github.com/Shymaa2611/Graphql_API_Project/assets/137145389/bdd2dcd4-df8a-44a8-aa20-a410937bb2ad)

   


   

