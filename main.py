from fastapi import FastAPI
from sqlalchemy.orm import Session

from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every

database_uri = f"sqlite:///./test.db?check_same_thread=False"
sessionmaker = FastAPISessionMaker(database_uri)

app = FastAPI()


def remove_expired_tokens(db: Session) -> None:
    """Pretend this function deletes expired tokens from the database"""


@app.on_event("startup")
# @repeat_every(seconds=3)  # 1 hour
def remove_expired_tokens_task() -> None:
    print("Hello World")
    # with sessionmaker.context_session() as db:
    #     remove_expired_tokens(db=db)



@app.on_event("startup")
@repeat_every(seconds=3)  # 1 hour
def remove_expired_tokens_task1() -> None:
    print("Hello World 333")
    x = 0/0
    # with sessionmaker.context_session() as db:
    #     remove_expired_tokens(db=db)
