# Graphql_API_Project
steps:-
   1-install strawberry-graphql and strawberry-graphql-django
   2- add  "strawberry" to INSTALLED_APPS
   3- create schema.py file and types.py file in your app
   4- add this in project/urls.py
      from strawberry.django.views import GraphQLView
      from api.schema import schema
      urlpatterns = [
       path("graphql", GraphQLView.as_view(schema=schema))
    ]
    
   run http://127.0.0.1:8000/graphql

   -http://127.0.0.1:8000/graphql.jpg
   - graphql_api.jpg
