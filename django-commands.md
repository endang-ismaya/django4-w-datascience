# Django First Setup

## 1. Create GitHub repository

- public/private
- .gitignore for python

  ```bash
  # Endang
  .vscode/
  mynotes.txt
  resources/
  debug_logs/
  ```

- MIT License

## 2. Clone GitHub Repo

## 3. Setting up files/linter

- .flake8

  ```bash
  [flake8]
  max-line-length = 120
  
  exclude =
      migrations
      __pycache__
      manage.py
      settings.py
      env
      .env
      output
      old
      build
      dist
      .git
  
  per-file-ignores =
      # imported but unused
      __init__.py: F401
  ```

- .prettierignore

  ```bash
  *.html
  ```

- .prettierrc

  ```bash
  {
      "singleQuote": false,
      "tabWidth": 4,
      "overrides": [
          {
              "files": ["*.css", "*.html"],
              "options": {
                  "tabWidth": 4
              }
          }
      ],
      "bracketSpacing": true,
      "printWidth": 80
  }
  ```

- .djlintrc

  ```bash
  {
      "indent": "2",
      "max_attribute_length": "500",
      "ignore": "H021,H019"
  }
  
  ```

- mynotes.txt

- .vscode/settings.json

  ```json
  {
      "python.formatting.provider": "black",
      "emmet.includeLanguages": {
          "django-html": "html"
      },
      "files.associations": {
          "**/*.html": "html",
          "**/templates/**/*.html": "django-html",
          "**/templates/**/*": "django-txt",
          "**/requirements{/**,*}.{txt,in}": "pip-requirements",
          "*.css": "tailwindcss"
      },
      "editor.quickSuggestions": {
          "strings": true
      },
      "tailwindCSS.includeLanguages": {
          "plaintext": "html"
      },
      "editor.detectIndentation": false,
      "[django-html]": {
          "editor.defaultFormatter": "monosans.djlint",
          "editor.trimAutoWhitespace": true,
          "editor.tabSize": 2
      },
      "[json]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode",
          "editor.tabSize": 4
      },
      "json.schemaDownload.enable": true,
      "[html][django-html][handlebars][hbs][mustache][jinja][jinja-html][nj][njk][nunjucks][twig]": {
          "editor.defaultFormatter": "monosans.djlint"
      },
      "todo-tree.general.tags": ["BUG", "HACK", "FIXME", "TODO", "XXX", "[ ]", "[x]"],
      "todo-tree.highlights.defaultHighlight": {
          "icon": "alert",
          "type": "text",
          "foreground": "#d6a960",
          "background": "#0B2447",
          "opacity": 50,
          "iconColour": "#FFD93D"
      },
      "todo-tree.highlights.customHighlight": {
          "TODO": {
              "icon": "alert",
              "type": "line",
              "gutterIcon": true
          },
          "FIXME": {
              "icon": "bell",
              "type": "line",
              "gutterIcon": true
          }
      }
  }
  ```

## 4. Install the requirements

- flake8, black, and Django

  ```bash
  pipenv install flake8 --dev
  
  pipenv install black --dev --pre
  
  pipenv install djlint --dev
  
  pipenv install django
  ```

- django-dotenv

  ```bash
  pipenv install django-dotenv
  ```

- Pillow

  ```bash
  pipenv install Pillow
  ```

## 5. Setup Project with .env

- Select python interpreter to pipenv

- Create Project

  ```bash
  django-admin startproject _project .
  ```

- Create File and Folder Folders

  ```bash
  touch _project/.env
  mkdir _project/static
  mkdir apps
  mkdir templates
  mkdir media
  
  ```

- .env

  ```bash
  DJANGO_SECRET_KEY="django-insecure-@+*pmku!_t*cz!r3@qp_42ry18=mbt-v7$ga7*!u7u*4^x)vxr"
  DEBUG=True
  ```

- settings.py

  ```python
  import os
  import dotenv
  
  # environment
  dotenv.read_dotenv()
  
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
  
  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = os.environ.get("DEBUG") == "True"
  ```

- settings.py templates and static

  ```python
  TEMPLATES = [
      {
          "BACKEND": "django.template.backends.django.DjangoTemplates",
          "DIRS": [os.path.join(BASE_DIR, "templates")],
          "APP_DIRS": True,
          "OPTIONS": {
              "context_processors": [
                  "django.template.context_processors.debug",
                  "django.template.context_processors.request",
                  "django.contrib.auth.context_processors.auth",
                  "django.contrib.messages.context_processors.messages",
              ],
          },
      },
  ]
  
  STATIC_URL = "static/"
  STATIC_ROOT = os.path.join(BASE_DIR, "static")
  STATICFILES_DIRS = [os.path.join(BASE_DIR, "_project", "static")]
  
  # MEDIA
  MEDIA_URL = "/media/"
  MEDIA_ROOT = os.path.join(BASE_DIR, "media")
  
  ```

- Project's URL

  ```python
  """
  Project URLs
  """
  from django.contrib import admin
  from django.urls import path, include
  
  from django.conf.urls.static import static
  from django.conf import settings
  
  urlpatterns = [
      path("admin/", admin.site.urls),
  ]
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
