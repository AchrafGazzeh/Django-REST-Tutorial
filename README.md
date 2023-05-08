# Django-REST-Tutorial

This is a Django app that allows users to create, view, and manage code snippets. It includes the following views

## Installation

1. Clone the repository:

```https://github.com/AchrafGazzeh/Django-REST-Tutorial```

2. Run the migrations:

```python manage.py migrate```

3. Start the development server:

```python manage.py runserver```



# Django Snippets App

This is a Django app that allows users to create, view, and manage code snippets. It includes the following views:

## SnippetViewSet

This viewset automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for snippets. Additionally, it provides an extra `highlight` action.

### Usage

To access the `SnippetViewSet`, go to `/snippets/`.

### Permissions

This viewset requires authentication for creating, updating, and deleting snippets. Only the owner of a snippet can update or delete it.

## UserViewSet

This viewset automatically provides `list` and `retrieve` actions for users.

### Usage

To access the `UserViewSet`, go to `/users/`.

## api_root

This function-based view returns a JSON response with links to the `UserViewSet` and `SnippetViewSet`.

### Usage

To access the `api_root`, go to `/`.

## Models

This app includes the following models:

### Snippet

This model represents a code snippet. It includes the following fields:

- `created`: A `DateTimeField` that automatically sets the date and time the snippet was created.
- `title`: A `CharField` that stores the title of the snippet.
- `code`: A `TextField` that stores the code of the snippet.
- `linenos`: A `BooleanField` that determines whether or not to display line numbers for the snippet.
- `language`: A `CharField` that stores the programming language of the snippet.
- `style`: A `CharField` that stores the Pygments style to use for highlighting the snippet.
- `owner`: A `ForeignKey` that links to the `auth.User` model to associate the snippet with its owner.
- `highlighted`: A `TextField` that stores the highlighted HTML representation of the snippet.

### Usage

To create a new snippet, go to `/snippets/create/`. To view a specific snippet, go to `/snippets/<snippet_id>/`, where `<snippet_id>` is the ID of the snippet you want to view. To update or delete a snippet, go to `/snippets/<snippet_id>/update/` or `/snippets/<snippet_id>/delete/`, respectively.

## Swagger API

This app includes a Swagger API that provides documentation for the REST API. To access the Swagger API, go to `/docs/`. This will display the Swagger UI, which provides an interactive interface for exploring the API. The Swagger API includes information about the available endpoints, request and response formats, and authentication requirements. You can also access the API schema directly by going to `/api_schema/`. This will display the API schema in JSON format, which can be useful for developers who are integrating with the API or for anyone who wants to learn more about how the app works.
