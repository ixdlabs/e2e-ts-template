import uuid

from assertpy import assert_that

from tests.perf.base import BaseDocsUser


class SocialMediaScenarios:
    def view_all_posts(self, user: BaseDocsUser) -> list[dict]:
        with user.rest_json("GET", "/api/v1/posts") as response:
            assert_that(response.js).is_not_none()
            assert_that(response.js).is_iterable()
            assert_that(response.js).contains("data")
            return response.js["data"]
        return []

    def react_to_post(self, user: BaseDocsUser, post_id: str):
        with user.rest_text("POST", f"/api/v1/posts/{post_id}/react", json={"reactionType": "LIKE"}) as response:
            assert_that(response.text).is_not_none()

    def comment_on_post(self, user: BaseDocsUser, post_id: str):
        payload = {"comment": "[TEST] Great post!"}
        with user.rest_text("POST", f"/api/v1/posts/{post_id}/comment", json=payload) as response:
            assert_that(response.text).is_not_none()

    def share_post(self, user: BaseDocsUser, post_id: str):
        payload = {"content": "[TEST] Good post!"}
        with user.rest_json("POST", f"/api/v1/posts/{post_id}/share", json=payload) as response:
            assert_that(response.js).is_not_none()

    def view_recommended_users(self, user: BaseDocsUser) -> list[str]:
        with user.rest_json("GET", "/api/v1/users/recommended-users") as response:
            assert_that(response.js).is_not_none()
            assert_that(response.js).is_iterable()
            return response.js
        return []

    def follow_user(self, user: BaseDocsUser, user_id: str):
        with user.rest_text("POST", f"/api/v1/users/{user_id}/follow") as response:
            assert_that(response.text).is_not_none()
