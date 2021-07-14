from fastapi import HTTPException, status


CREDENTIALS_EXCEPTION = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

TOKEN_EXCEPTION = HTTPException(status_code=400, detail="Inactive user")

USER_NOT_FOUND = HTTPException(status_code=404, detail="User not found")

INCORRECT_USERNAME_PASSWORD = HTTPException(status_code=400, detail="Incorrect username or password")

EMAIL_EXIST = HTTPException(status_code=400, detail="Email already registered")

ALREADY_LIKED = HTTPException(status_code=400, detail="User already liked/disliked this post")

DATE_VALUE_ERROR = HTTPException(status_code=400, detail="Date format error. Correct: YYYY-MM-DD")





