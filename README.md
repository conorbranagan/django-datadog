# Django Datadog

A simple Django middleware for submitting timings and exceptions to Datadog.

## Installation

Download the code into your project and install it.

```bash
git clone git://github.com/conorbranagan/django-datadog.git
cd django-datadog
python setup.py install
```

Add `datadog` to your list of installed apps.

```python
INSTALLED_APPS += ('datadog')
```

Add the following configuration to your projects' `settings.py` file:

```python
DATADOG_API_KEY = 'YOUR_API_KEY'
DATADOG_APP_KEY = 'YOUR_APP_KEY'
DATADOG_APP_NAME = 'my_app' # Used to namespace metric names
```

The API and app keys can be found at https://app.datadoghq.com/account/settings#api

Add the Datadog request handler to your middleware in `settings.py`.

```python
MIDDLEWARE_CLASSES += ('datadog.middleware.DatadogMiddleware')
```

## Usage

Once the middlewhere installed, you'll start receiving events in your Datadog
stream in the case of an app exception. Here's an example:

![example django exception](https://dl.dropbox.com/u/126553/django-datadog.png)

You will also have new timing metrics available:

- `my_app.request_time.{avg,max,min}`
- `my_app.errors`

Metrics are tagged with `path:/path/to/view`

Note: `my_app` will be replaced by whatever value you give for `DATADOG_APP_NAME`.
