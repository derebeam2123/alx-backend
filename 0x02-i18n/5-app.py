```
users = {
	1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
	2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
	3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
	4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```

This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

| __msgid__       | __English__ 	                   | __French__                                       |
| --------------- | -------------------------------------- | ------------------------------------------------ |
| `logged_in_as`  | `"You are logged in as %(username)s."` | `"Vous êtes connecté en tant que %(username)s."` |
| `not_logged_in` | `"You are not logged in."`             | `"Vous n'êtes pas connecté."`                    |
