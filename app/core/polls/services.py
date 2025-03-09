from app.core.polls.errors import PollsBadRequestError, PollsNotFoundError


class PollService:

    @classmethod
    def create(cls, q: str | None) -> object | Exception:
        """
        Create a poll example
        :return:
        """
        if not q:
            raise PollsBadRequestError("Poll Bad request")

        if q == "0":
            raise PollsNotFoundError("Poll not found")

        if q == "1":
            return {"id": "1", "name": "Poll 1"}

        return {"id": q, "name": f"Poll {q}"}
