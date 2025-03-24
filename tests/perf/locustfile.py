import random
from locust import task, between, run_single_user
from tests.perf.auth import get_token
from tests.perf.base import BaseDocsUser
from tests.perf.config import SITE_ID
from tests.perf.scenarios.social import SocialMediaScenarios


class SocialMediaUser(BaseDocsUser):
    wait_time = between(1, 3)

    def on_start(self):
        token = get_token()
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Site": SITE_ID,
        }

    @task(5)
    def view_react_comment_share(self):
        """Simulate the entire post engagement flow in sequence (no creation)."""
        scenarios = SocialMediaScenarios()
        posts = scenarios.view_all_posts(self)
        if posts:
            commentable_post_ids = [post["id"] for post in posts if post["commentAudience"] == "EVERYONE"]
            post_id = random.choice(commentable_post_ids)
            scenarios.react_to_post(self, post_id)
            scenarios.comment_on_post(self, post_id)
            scenarios.share_post(self, post_id)

    @task(2)
    def follow_view_posts(self):
        """Test how users consume and interact with followed users' content."""
        scenarios = SocialMediaScenarios()
        recommended_users = scenarios.view_recommended_users(self)
        if recommended_users:
            user_id = random.choice(recommended_users)
            scenarios.follow_user(self, user_id)
            scenarios.view_all_posts(self)


if __name__ == "__main__":
    run_single_user(SocialMediaUser)
