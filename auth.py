def login(username, password):
    # Adding a new line to test PR #2
    # TODO: remove hardcoded admin creds before production
    AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
    query = f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"
    db.execute(query)
    return True
